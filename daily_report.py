#!/usr/bin/env python3
"""Daily per-repository report, and the lead's roll-up of many reports.

  daily_report.py report --out EVAL/<tag>/out --work KIT_HOME/work [--intern NAME]
      writes <repo>-report.md and <repo>-report.json next to each <repo>-diff.json.
  daily_report.py rollup DIR [DIR ...] [--md rollup.md] [--csv rollup.csv]
      reads every *-report.json under the folders (latest per intern and repo) and writes one table.

A report holds: repository and commit, language version, framework versions,
which engine is more accurate (and how sure), the gaps (machine counts and the
patterns people confirmed), how many rows people verified, speed and memory,
and where the work stands (the Status block of the differences sheet).
Versions are read from the repository's own files; the intern can correct them
in the Status block ("- framework: django 5.1").
"""
import argparse
import collections
import csv
import datetime
import json
import pathlib
import re
import subprocess
import sys
import tomllib

SKIP_DIRS = {".git", "node_modules", "vendor", "third_party", "dist", "build", ".venv", "venv", "__pycache__"}
EXT = {"python": (".py",), "go": (".go",), "typescript": (".ts", ".tsx", ".mts", ".cts")}
PY_FW = ["django", "flask", "fastapi", "starlette", "tornado", "aiohttp", "pyramid", "sanic", "quart", "falcon",
         "bottle", "celery", "sqlalchemy", "pydantic", "click", "typer", "djangorestframework", "httpx", "requests"]
GO_FW = ["github.com/gin-gonic/gin", "github.com/labstack/echo", "github.com/gofiber/fiber", "github.com/go-chi/chi",
         "github.com/gorilla/mux", "github.com/spf13/cobra", "github.com/urfave/cli", "gorm.io/gorm", "xorm.io/xorm",
         "google.golang.org/grpc", "github.com/go-kit/kit", "github.com/beego/beego", "connectrpc.com/connect"]
TS_FW = ["next", "react", "vue", "@angular/core", "svelte", "nuxt", "express", "fastify", "@nestjs/core", "koa", "hono",
         "@remix-run/node", "@prisma/client", "@trpc/server", "typeorm", "typescript"]
VERDICTS = ["confirmed", "oracle wrong", "dev wrong", "v2 right after all", "?"]
CELL_SPLIT = re.compile(r"(?<!\\)\|")


# ------------------------------------------------------------------ versions

def walk(root, names, depth=3):
    """Files with these names, up to `depth` folders down, skipping vendored and built code."""
    out = []

    def rec(d, n):
        try:
            entries = sorted(d.iterdir())
        except OSError:
            return
        for p in entries:
            if p.is_dir():
                if n < depth and p.name not in SKIP_DIRS and not p.name.startswith("."):
                    rec(p, n + 1)
            elif p.name in names:
                out.append(p)
    rec(root, 0)
    return sorted(out, key=lambda p: (len(p.relative_to(root).parts), str(p)))


def read(p):
    try:
        return p.read_text(errors="replace")
    except OSError:
        return ""


def norm(n):
    return re.sub(r"[-_.]+", "-", n).lower()


def py_versions(src):
    lang, fw, project = [], {}, ""
    for p in walk(src, {"pyproject.toml"}, 1):
        try:
            d = tomllib.loads(read(p))
        except tomllib.TOMLDecodeError:
            continue
        proj = d.get("project", {})
        project = project or f"{proj.get('name', '')} {proj.get('version', '')}".strip()
        if proj.get("requires-python"):
            lang.append(f"requires-python {proj['requires-python']} ({p.name})")
        poetry = d.get("tool", {}).get("poetry", {})
        if poetry.get("dependencies", {}).get("python"):
            lang.append(f"python {poetry['dependencies']['python']} (poetry)")
        deps = list(proj.get("dependencies", []))
        for group in proj.get("optional-dependencies", {}).values():
            deps += group
        deps += [f"{k}{v if isinstance(v, str) else ''}" for k, v in poetry.get("dependencies", {}).items()]
        for dep in deps:
            m = re.match(r"\s*([A-Za-z0-9_.\-]+)\s*(\[.*?\])?\s*([^;]*)", dep)
            if m and norm(m.group(1)) in PY_FW:
                fw.setdefault(norm(m.group(1)), f"{m.group(3).strip() or 'any'} (pyproject)")
    for p in walk(src, {"setup.cfg", "setup.py"}, 1):
        m = re.search(r"python_requires\s*=\s*['\"]?([^'\"\n,]+)", read(p))
        if m:
            lang.append(f"python_requires {m.group(1).strip()} ({p.name})")
    for p in walk(src, {".python-version", "runtime.txt"}, 1):
        lang.append(f"{read(p).strip()} ({p.name})")
    for p in sorted(src.glob("requirements*.txt")) + sorted(src.glob("requirements/*.txt")):
        if re.search(r"dev|test|doc|lint|typing|build|ci", p.name):
            continue  # tooling, not what the application runs on
        for line in read(p).splitlines():
            m = re.match(r"\s*([A-Za-z0-9_.\-]+)\s*(\[.*?\])?\s*([=<>!~]=?[^#;\s]*)?", line)
            if m and norm(m.group(1)) in PY_FW:
                fw.setdefault(norm(m.group(1)), f"{m.group(3) or 'any'} ({p.name})")
    for lock in ("poetry.lock", "uv.lock"):
        text = read(src / lock)
        for name in list(fw):
            m = re.search(r'name = "' + re.escape(name) + r'"\s*\nversion = "([^"]+)"', text, re.I)
            if m:
                fw[name] = f"{m.group(1)} ({lock})"
    return lang, fw, project


def go_versions(src):
    text = read(src / "go.mod")
    lang = []
    m = re.search(r"^go\s+(\S+)", text, re.M)
    if m:
        lang.append(f"go {m.group(1)} (go.mod)")
    m = re.search(r"^toolchain\s+(\S+)", text, re.M)
    if m:
        lang.append(f"toolchain {m.group(1)} (go.mod)")
    fw = {}
    for mod in GO_FW:
        m = re.search(r"^\s*(?:require\s+)?" + re.escape(mod) + r"(/v\d+)?\s+(v\S+)", text, re.M)
        if m:
            fw[mod + (m.group(1) or "")] = m.group(2)
    module = re.search(r"^module\s+(\S+)", text, re.M)
    return lang, fw, module.group(1) if module else ""


def ts_versions(src):
    lang, fw, project = [], {}, ""
    locks = {n: read(src / n) for n in ("package-lock.json", "pnpm-lock.yaml", "yarn.lock")}
    for p in walk(src, {"package.json"}, 3):
        try:
            d = json.loads(read(p))
        except json.JSONDecodeError:
            continue
        rel = str(p.relative_to(src))
        if rel == "package.json":
            project = f"{d.get('name', '')} {d.get('version', '')}".strip()
            if isinstance(d.get("engines"), dict) and d["engines"].get("node"):
                lang.append(f"node {d['engines']['node']} (engines)")
            if d.get("packageManager"):
                lang.append(f"{d['packageManager']} (packageManager)")
        if not isinstance(d, dict):
            continue
        deps = {**(d.get("devDependencies") or {}), **(d.get("dependencies") or {})}
        if not all(isinstance(x, str) for x in deps.values()):
            deps = {k: v for k, v in deps.items() if isinstance(v, str)}
        for name in TS_FW:
            if name in deps and name not in fw:
                fw[name] = f"{deps[name]} ({rel})"
    for name in list(fw):
        v = None
        if locks["package-lock.json"]:
            try:
                v = json.loads(locks["package-lock.json"]).get("packages", {}).get(f"node_modules/{name}", {}).get("version")
            except json.JSONDecodeError:
                pass
        if not v and locks["pnpm-lock.yaml"]:
            m = re.search(r"^\s+'?" + re.escape(name) + r"'?:\s*\n\s+specifier: [^\n]*\n\s+version: ([^\s(]+)",
                          locks["pnpm-lock.yaml"], re.M)
            v = m.group(1) if m else None
        if not v and locks["yarn.lock"]:
            m = re.search(r'^"?' + re.escape(name) + r'@[^\n]*:\n\s+version:? "?([^"\s]+)', locks["yarn.lock"], re.M)
            v = m.group(1) if m else None
        if v:
            fw[name] = f"{v} (lockfile)"
    if "typescript" in fw:
        lang.append(f"typescript {fw.pop('typescript')}")
    return lang, fw, project


def git_version(src):
    try:
        return subprocess.run(["git", "-C", str(src), "describe", "--tags", "--always"], capture_output=True,
                              text=True, timeout=10).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def framework_text(fw, project, lang, version):
    own = project.split()[0] if project else ""
    known = PY_FW if lang == "python" else GO_FW if lang == "go" else TS_FW
    others = {k: v for k, v in fw.items() if norm(k) != norm(own)}
    parts = [f"{k} {v}" for k, v in others.items()]
    if own and (norm(own) in [norm(k) for k in known] or not parts):
        parts.insert(0, f"the repo itself: {own} {version}".strip() + (" (a library)" if not others else ""))
    return "; ".join(parts) or "none detected"


def lines_of_code(src, lang):
    n = files = 0
    for p in src.rglob("*"):
        if p.suffix in EXT[lang] and not (set(p.relative_to(src).parts[:-1]) & SKIP_DIRS) and p.is_file():
            files += 1
            n += read(p).count("\n")
    return n, files


# ------------------------------------------------------------------ the sheet

def read_sheet(path):
    status, rows, kind, in_status = {}, [], None, False
    for line in path.read_text().splitlines():
        if line.startswith("## "):
            in_status = line.startswith("## Status")
            continue
        m = re.match(r"<!-- kind: (\w+) -->", line)
        if m:
            kind = m.group(1)
            continue
        if in_status:
            m = re.match(r"- ([a-z ]+):\s*(.*)", line)
            if m:
                status[m.group(1).strip()] = m.group(2).strip()
            continue
        if kind and re.match(r"^\| *\d+ *\|", line):
            c = [x.strip().replace("\\|", "|") for x in CELL_SPLIT.split(line)[1:-1]]
            if len(c) > 10:  # a "|" typed in the cause cell
                c = c[:8] + [" / ".join(c[8:-1]), c[-1]]
            if len(c) == 10:
                rows.append({"group": kind, "where": c[1].strip("`"), "oracle": c[3], "notes": c[6],
                             "verdict": c[7].lower(), "cause": c[8], "reason_true": c[9].lower()})
    return status, rows


def given(value):
    """A Status value the intern wrote, not the placeholder."""
    v = re.sub(r"\s{2,}\(.*$", "", (value or "").strip())        # drop the hint in brackets
    v = re.sub(r"\s{2,}(write a value|for example).*$", "", v)
    v = re.sub(r"^\(auto\)\s*", "", v).strip()                 # "(auto) 3.12" -> "3.12"
    return v


# ------------------------------------------------------------------ report

def pct(x):
    return "n/a" if not x or x.get("value") is None else f"{100 * x['value']:.1f}%"


def ci(x):
    return "" if not x or not x.get("ci95") else f" [{100 * x['ci95'][0]:.1f}–{100 * x['ci95'][1]:.1f}]"


def compare(dev, v2):
    """Who is ahead on one metric, and whether the 95% intervals separate."""
    if not dev or not v2 or dev.get("value") is None or v2.get("value") is None:
        return "not measurable"
    lead = "v2" if v2["value"] > dev["value"] else "dev" if dev["value"] > v2["value"] else "neither"
    apart = v2["ci95"][0] > dev["ci95"][1] or dev["ci95"][0] > v2["ci95"][1]
    return f"{lead} ahead (clear)" if apart and lead != "neither" else f"{lead} ahead (within noise)" if lead != "neither" else "equal"


def decide(acc, d, ver):
    """One line for "which engine is more accurate", led by recall (the share of real calls
    each engine gets right), with the caveats a reader needs."""
    rec = acc["calls_recall"]["verdict"]
    site = (acc["calls_precision_v2_site"] or {}).get("value")
    gap_v = ver.get("gap", {})
    parts = [f"CALLS recall: {rec}"]
    if site is not None:
        parts.append(f"v2 precision at call sites {100 * site:.1f}%")
    parts.append(f"net {acc['net_calls_v2_minus_dev']:+d} calls for v2 (machine)")
    if gap_v.get("verified"):
        parts.append(f"{gap_v['confirmed']} of {gap_v['verified']} judged gap rows confirmed")
    else:
        parts.append("no gap rows judged yet")
    multi = d.get("flags", {}).get("dev_multi_gap", 0)
    if multi:
        parts.append(f"{multi} gaps where dev had several targets")
    return "; ".join(parts) + ". Line precision is not a fair ranking (decorator edges, different lines judged)."


def build(out, work, diff_path, intern):
    d = json.loads(diff_path.read_text())
    name, lang = d["repo"], d["language"]
    s = json.loads((out / f"{name}.json").read_text())
    status, rows = read_sheet(out / f"{name}-differences.md")
    src = work / name / "src"
    if lang == "python":
        lang_v, fw, project = py_versions(src)
    elif lang == "go":
        lang_v, fw, project = go_versions(src)
    else:
        lang_v, fw, project = ts_versions(src)
    loc, files = lines_of_code(src, lang)

    # Verdicts per group: sampled, verified (any verdict), and each verdict.
    ver = {}
    for g in d["samples"]:
        rs = [r for r in rows if r["group"] == g]
        c = collections.Counter(r["verdict"] for r in rs if r["verdict"])
        ver[g] = {"population": d.get("rows", d["counts"]).get(g, 0), "sampled": len(rs),
                  "verified": sum(n for v, n in c.items() if v in VERDICTS and v != "?"),
                  **{v: c.get(v, 0) for v in VERDICTS},
                  "other": sum(n for v, n in c.items() if v not in VERDICTS)}

    # Stratum of each sampled row, from the samples in diff.json.
    stratum_of = {(g, f"{x['file']}:{x['line']}", x["oracle"]): x.get("stratum", "-")
                  for g, xs in d["samples"].items() for x in xs}

    def estimate(g):
        """Real rows in group g: per stratum, its row count x the confirmed share of its judged
        sample rows (the sample is stratified, so a flat share would be biased). Only when the
        judged strata hold at least 80% of the group's rows and 10 rows are judged."""
        pops = d.get("strata", {}).get(g)
        if not pops:
            return None
        judged = collections.defaultdict(lambda: [0, 0])
        for r in rows:
            if r["group"] == g and r["verdict"] in VERDICTS and r["verdict"] != "?":
                k = stratum_of.get((g, r["where"], r["oracle"]), "-")
                judged[k][0] += r["verdict"] == "confirmed"
                judged[k][1] += 1
        covered = sum(pops.get(k, 0) for k in judged)
        if sum(n for _, n in judged.values()) < 10 or covered < 0.8 * sum(pops.values()):
            return None
        est = sum(pops.get(k, 0) * c / n for k, (c, n) in judged.items())
        return round(est * sum(pops.values()) / covered)

    # Patterns: confirmed rows grouped by cause.
    pats = collections.defaultdict(lambda: {"rows": 0, "groups": collections.Counter(), "miss": collections.Counter(),
                                            "files": set(), "reason_false": 0})
    for r in rows:
        if r["verdict"] == "confirmed" and r["group"] in ("gap", "v2_wrong", "both_miss") and r["cause"]:
            p = pats[r["cause"].lower()]
            p["rows"] += 1
            p["groups"][r["group"]] += 1
            p["miss"][(r["notes"].split(";")[0].split(" (")[0] or "-")] += 1
            p["files"].add(r["where"].rsplit(":", 1)[0])
            p["reason_false"] += r["reason_true"] == "no"
    patterns = [{"cause": k, "rows": v["rows"], "groups": dict(v["groups"]), "v2_miss": dict(v["miss"]),
                 "files": len(v["files"]), "reason_false": v["reason_false"],
                 "silent": v["miss"].get("silent", 0) > 0}
                for k, v in sorted(pats.items(), key=lambda kv: -kv[1]["rows"])]

    v2c, lg = s["v2"]["calls"], s["legacy"]["calls"]
    acc = {
        "calls_recall": {"dev": lg["recall"], "v2": v2c["line_level"]["recall"],
                         "verdict": compare(lg["recall"], v2c["line_level"]["recall"])},
        "calls_precision_line": {"dev": lg["precision"], "v2": v2c["line_level"]["precision"],
                                 "verdict": compare(lg["precision"], v2c["line_level"]["precision"])},
        "calls_precision_v2_site": v2c["precision"]["overall"],
        "imports_in_repo_precision": {"dev": s["legacy"]["imports"]["in_repo"]["precision"],
                                      "v2": s["v2"]["imports"]["in_repo"]["precision"]},
        "imports_in_repo_recall": {"dev": s["legacy"]["imports"]["in_repo"]["recall"],
                                   "v2": s["v2"]["imports"]["in_repo"]["recall"]},
        "net_calls_v2_minus_dev": d["counts"]["v2_gain"] - d["counts"]["gap"],
        "gap_estimated_real": estimate("gap"),
        "v2_gain_estimated_real": estimate("v2_gain"),
    }
    perf = {e: {"wall_s_run2": s[k]["perf"]["wall_s"][-1], "peak_mib_run2": round(s[k]["perf"]["peak_rss_bytes"][-1] / 1048576),
                "deterministic": s[k]["determinism"]["identical"]} for e, k in (("dev", "legacy"), ("v2", "v2"))}
    gaps_machine = [m for m in d["v2_misses"] if m[0] == "gap"]
    m = re.search(r"on (\d{4}-\d{2}-\d{2})", read(out.parent / "manifest.toml"))
    acc["decision"] = decide(acc, d, ver)
    rep = {
        "schema": 1, "date": datetime.date.today().isoformat(), "run_date": m.group(1) if m else "",
        "scoring_mode": s["v2"]["calls"].get("mode", ""),
        "intern": given(status.get("intern")) or intern or "",
        "repo": name, "url": d.get("url") or s.get("url", ""), "commit": d["commit"],
        "language": lang, "lines_of_code": loc, "files": files, "project": project,
        "language_version": given(status.get("language version")) or
                            ("declared: " + "; ".join(lang_v) if lang_v else "not declared"),
        "framework": given(status.get("framework")) or framework_text(fw, project, lang, git_version(src)),
        "language_version_detected": lang_v, "framework_detected": fw,
        "engines": {"dev": d["engines"]["legacy"], "v2": d["engines"]["v2"]},
        "oracle": f"{s['oracle'].get('tool', 'scip')} {s['oracle'].get('version', '')}".strip(),
        "counts": d["counts"], "flags": d.get("flags", {}), "check": d["check"].get("ok"),
        "accuracy": acc, "perf": perf,
        "v2_accounting_ok": s["v2"]["u12_accounting"]["ok"], "v2_files_failed": s["v2"]["files"]["failed"],
        "gaps_by_v2_miss": gaps_machine, "patterns": patterns, "verdicts": ver,
        "rows_verified": sum(v["verified"] for v in ver.values()),
        "rows_sampled": sum(v["sampled"] for v in ver.values()),
        "status": {k: given(status.get(k)) for k in ("stage", "next", "blocked by", "issues filed")},
    }
    rep["status"]["stage"] = given(status.get("stage")) or ("not started" if rep["rows_verified"] == 0 else "verifying")
    return rep


def to_md(r):
    a, c, v = r["accuracy"], r["counts"], r["verdicts"]
    est = lambda x: "n/a (judge 10+ rows, covering the strata that hold 80% of the group)" if x is None else str(x)
    L = [f"# Daily report: {r['repo']} ({r['date']}, {r['intern'] or 'intern?'})", "",
         "| Item | Value |", "|---|---|",
         f"| Repository | {r['url']} @ `{r['commit'][:12]}` ({r['lines_of_code']:,} lines in {r['files']} {r['language']} files) |",
         f"| Language version | {r['language_version']} |",
         f"| Framework | {r['framework']} |",
         f"| Engines | dev `{r['engines']['dev'][:12]}`, v2 `{r['engines']['v2'][:12]}`, oracle {r['oracle']} |",
         f"| Where we are | {r['status']['stage']}. Next: {r['status']['next'] or '-'}. Blocked by: {r['status']['blocked by'] or '-'} |",
         f"| Issues filed | {r['status']['issues filed'] or '-'} |",
         f"| Counts check against scores | {'OK' if r['check'] else 'MISMATCH'}; scoring mode {r['scoring_mode']}; run {r['run_date']} |",
         "", "## Which engine is more accurate", "",
         f"**{a['decision']}**", "",
         "| Metric | dev | v2 | Result |", "|---|---|---|---|",
         f"| CALLS recall | {pct(a['calls_recall']['dev'])}{ci(a['calls_recall']['dev'])} | {pct(a['calls_recall']['v2'])}{ci(a['calls_recall']['v2'])} | {a['calls_recall']['verdict']} |",
         f"| CALLS precision, line level | {pct(a['calls_precision_line']['dev'])}{ci(a['calls_precision_line']['dev'])} | {pct(a['calls_precision_line']['v2'])}{ci(a['calls_precision_line']['v2'])} | {a['calls_precision_line']['verdict']} |",
         f"| CALLS precision, v2 at exact call sites | - | {pct(a['calls_precision_v2_site'])} | v2 only |",
         f"| IMPORTS in-repo precision | {pct(a['imports_in_repo_precision']['dev'])} | {pct(a['imports_in_repo_precision']['v2'])} | n dev {(a['imports_in_repo_precision']['dev'] or {}).get('n')}, v2 {(a['imports_in_repo_precision']['v2'] or {}).get('n')} |",
         f"| IMPORTS in-repo recall | {pct(a['imports_in_repo_recall']['dev'])} | {pct(a['imports_in_repo_recall']['v2'])} | |",
         "",
         f"Net: v2 gets {a['net_calls_v2_minus_dev']:+d} calls against dev (v2 gain {c['v2_gain']} minus gap {c['gap']}). "
         f"Estimated real after human checks: gaps {est(a['gap_estimated_real'])}, v2 gains {est(a['v2_gain_estimated_real'])}.",
         "", "## Speed and memory (run 2)", "",
         "| | dev | v2 |", "|---|---|---|",
         f"| Wall time | {r['perf']['dev']['wall_s_run2']} s | {r['perf']['v2']['wall_s_run2']} s |",
         f"| Peak memory | {r['perf']['dev']['peak_mib_run2']} MiB | {r['perf']['v2']['peak_mib_run2']} MiB |",
         f"| Same output both runs | {r['perf']['dev']['deterministic']} | {r['perf']['v2']['deterministic']} |",
         f"| v2 accounting ok / files failed | | {r['v2_accounting_ok']} / {r['v2_files_failed']} |",
         "", "## Gaps", "",
         f"Calls the oracle found: {sum(c[k] for k in ('both_right', 'gap', 'v2_gain', 'both_miss'))}. Both right {c['both_right']}, "
         f"gap {c['gap']}, v2 gain {c['v2_gain']}, both miss {c['both_miss']}. Wrong edges: v2 {c['v2_wrong']}, dev {c['dev_wrong']}.",
         "", "How v2 missed the gap calls (machine):", "", "| v2 miss | reason | calls |", "|---|---|---|"]
    L += [f"| {m} | {rs} | {n} |" for _, m, rs, n in r["gaps_by_v2_miss"]] or ["| - | - | 0 |"]
    L += ["", "Patterns people confirmed (rows with verdict `confirmed` and a cause):", "",
          "| Cause | Rows | Groups | v2 miss | Files | False v2 reason |", "|---|---|---|---|---|---|"]
    L += [f"| {p['cause']} | {p['rows']} | {json.dumps(p['groups'])} | {json.dumps(p['v2_miss'])} | {p['files']} | {p['reason_false']} |"
          for p in r["patterns"]] or ["| none yet | | | | | |"]
    L += ["", "## Verified by people", "",
           f"{r['rows_verified']} of {r['rows_sampled']} sampled rows have a verdict (not counting `?`).", "",
          "| Group | Rows in repo | Sampled | Verified | Confirmed | Oracle wrong | Dev wrong | v2 right | ? | Misspelt |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    L += [f"| {g} | {x['population']} | {x['sampled']} | {x['verified']} | {x['confirmed']} | {x['oracle wrong']} | "
          f"{x['dev wrong']} | {x['v2 right after all']} | {x['?']} | {x['other']} |" for g, x in v.items()]
    L += ["", f"Machine flags: {json.dumps(r['flags'])}", ""]
    return "\n".join(L) + "\n"


def failed_report(repo, manifest, intern, why):
    eng = manifest.get("engines", {})
    return {"schema": 1, "failed": True, "date": datetime.date.today().isoformat(), "intern": intern,
            "repo": repo["name"], "url": repo.get("url", ""), "commit": repo.get("commit", ""),
            "language": repo.get("language", ""), "engines": {"dev": eng.get("legacy", ""), "v2": eng.get("v2", "")},
            "status": {"stage": "FAILED", "blocked by": why, "next": "", "issues filed": ""}}


def cmd_report(a):
    out, work = a.out.resolve(), a.work.resolve()
    try:
        manifest = tomllib.loads(read(out.parent / "manifest.toml"))
    except tomllib.TOMLDecodeError:
        manifest = {}
    names = [r["name"] for r in manifest.get("repos", [])] or [p.name[: -len("-diff.json")] for p in out.glob("*-diff.json")]
    if not names:
        sys.exit(f"no repositories found in {out}: run graph-eval.sh run first")
    for name in names:
        p = out / f"{name}-diff.json"
        try:
            if not p.exists() or not (out / f"{name}.json").exists():
                raise FileNotFoundError("the run has no result for this repository (see run.log)")
            r = build(out, work, p, a.intern)
        except Exception as e:  # one bad repository must not stop the others
            print(f"{name}: FAILED report: {type(e).__name__}: {e}", file=sys.stderr)
            repo = next((x for x in manifest.get("repos", []) if x["name"] == name), {"name": name})
            r = failed_report(repo, manifest, a.intern, f"{type(e).__name__}: {e}")
            (out / f"{name}-report.json").write_text(json.dumps(r, indent=2, sort_keys=True) + "\n")
            (out / f"{name}-report.md").write_text(f"# Daily report: {name}: FAILED\n\n{r['status']['blocked by']}\n")
            continue
        (out / f"{name}-report.json").write_text(json.dumps(r, indent=2, sort_keys=True) + "\n")
        (out / f"{name}-report.md").write_text(to_md(r))
        print(f"{name}: {out / (name + '-report.md')}  ({r['rows_verified']} of {r['rows_sampled']} rows verified, stage {r['status']['stage']})")


def cmd_rollup(a):
    reps = {}
    for d in a.dirs:
        for p in pathlib.Path(d).rglob("*-report.json"):
            try:
                r = json.loads(p.read_text())
            except (OSError, json.JSONDecodeError):
                continue
            k = (r.get("intern", ""), r["repo"])
            if k not in reps or (r["date"], p.stat().st_mtime) > reps[k][0]:
                reps[k] = ((r["date"], p.stat().st_mtime), r)
    rs = sorted((r for _, r in reps.values()), key=lambda r: (r["language"], r["repo"], r["intern"]))
    if not rs:
        sys.exit("no *-report.json found")
    cols = ["date", "intern", "repo", "language", "language_version", "framework", "lines", "dev", "v2",
            "recall dev", "recall v2", "recall result", "prec line dev", "prec line v2", "prec v2 site",
            "gap", "v2 gain", "both miss", "v2 wrong", "gap est. real", "patterns", "silent patterns",
            "verified", "sampled", "v2 peak MiB", "dev peak MiB", "v2 s", "dev s", "deterministic", "check", "stage", "blocked by"]
    table = []
    for r in rs:
        if r.get("failed"):
            table.append([r["date"], r["intern"], r["repo"], r["language"]] + ["-"] * (len(cols) - 6)
                         + ["FAILED", r["status"]["blocked by"][:80]])
            continue
        a_, c = r["accuracy"], r["counts"]
        table.append([r["date"], r["intern"], r["repo"], r["language"], r["language_version"], r["framework"],
                      r["lines_of_code"], r["engines"]["dev"][:8], r["engines"]["v2"][:8],
                      pct(a_["calls_recall"]["dev"]), pct(a_["calls_recall"]["v2"]), a_["calls_recall"]["verdict"],
                      pct(a_["calls_precision_line"]["dev"]), pct(a_["calls_precision_line"]["v2"]),
                      pct(a_["calls_precision_v2_site"]), c["gap"], c["v2_gain"], c["both_miss"], c["v2_wrong"],
                      a_["gap_estimated_real"] if a_["gap_estimated_real"] is not None else "-",
                      len(r["patterns"]), sum(p["silent"] for p in r["patterns"]), r["rows_verified"], r["rows_sampled"],
                      r["perf"]["v2"]["peak_mib_run2"], r["perf"]["dev"]["peak_mib_run2"],
                      r["perf"]["v2"]["wall_s_run2"], r["perf"]["dev"]["wall_s_run2"],
                      f"{r['perf']['dev']['deterministic']}/{r['perf']['v2']['deterministic']}",
                      "OK" if r["check"] else "MISMATCH", r["status"]["stage"], r["status"]["blocked by"] or "-"])
    if a.csv:
        with open(a.csv, "w", newline="") as fh:
            csv.writer(fh).writerows([cols] + table)
    esc = lambda x: str(x).replace("|", "\\|")
    L = [f"# Graph v2 vs dev: where we are ({datetime.date.today().isoformat()})", "",
         f"{len(rs)} repository reports. Engines seen: v2 {sorted({r['engines']['v2'][:12] for r in rs})}, "
         f"dev {sorted({r['engines']['dev'][:12] for r in rs})}.", "",
         "| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    L += ["| " + " | ".join(esc(x) for x in row) + " |" for row in table]
    allp = collections.defaultdict(lambda: [0, set(), False])
    for r in rs:
        for p in r.get("patterns", []):
            x = allp[p["cause"]]
            x[0] += p["rows"]
            x[1].add(r["repo"])
            x[2] |= p["silent"]
    L += ["", "## Confirmed gap patterns across repositories", "", "| Cause | Rows | Repositories | Silent |", "|---|---|---|---|"]
    L += [f"| {esc(k)} | {v[0]} | {', '.join(sorted(v[1]))} | {'yes' if v[2] else 'no'} |"
          for k, v in sorted(allp.items(), key=lambda kv: (-len(kv[1][1]), -kv[1][0]))] or ["| none yet | | | |"]
    text = "\n".join(L) + "\n"
    if a.md:
        pathlib.Path(a.md).write_text(text)
        print(f"wrote {a.md}" + (f" and {a.csv}" if a.csv else ""))
    else:
        print(text)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("report")
    r.add_argument("--out", required=True, type=pathlib.Path)
    r.add_argument("--work", required=True, type=pathlib.Path)
    r.add_argument("--intern", default="")
    u = sub.add_parser("rollup")
    u.add_argument("dirs", nargs="+")
    u.add_argument("--md")
    u.add_argument("--csv")
    a = ap.parse_args()
    cmd_report(a) if a.cmd == "report" else cmd_rollup(a)


if __name__ == "__main__":
    main()
