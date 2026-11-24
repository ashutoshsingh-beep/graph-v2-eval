#!/usr/bin/env python3
"""Call-by-call differences: oracle (SCIP) vs old engine (dev) vs graph v2.

Reads what scip_eval.py already built under --work (no new builds) and writes,
per repository, a sheet of sampled differences for a person to verify.

Recall side: every in-repo call the oracle found ("obligation", one per file,
line and oracle target set) goes in exactly one group:
  both_right  both engines have a right edge on that line (not in the sheet)
  gap         dev right, v2 not
  v2_gain     v2 right, dev not
  both_miss   neither
Each v2 miss also gets a miss type, read at the exact call site (byte span):
  no_node       v2 has no node for the oracle's target, so no edge can be right
  wrong_target  v2 has a resolved in-repo edge at this call site, to another target
  external      v2 has an external edge at this call site
  reported      v2 has only unresolved edges at this call site (with a reason)
  silent        v2 has no edge at this call site at all

Precision side: every in-repo edge of an engine on a line where the oracle has a
call is right (its target meets one of that line's obligations) or wrong:
  v2_wrong    wrong v2 edges       dev_wrong   wrong dev edges
Edges on lines where the oracle has no call with a mapped target are not scored:
  v2_unscored, dev_unscored (a small sample, to look at what the oracle cannot see)

The counts are checked against the published scores in <repo>.json: v2 recall =
(both_right + v2_gain) / obligations, dev recall = (both_right + gap) /
obligations, precision = right edges / scored edges. A mismatch is printed and
stored under "check" in <repo>-diff.json.

usage: graph_diff.py --engine-repo CODEPARSER --manifest M --work W --out OUT
                     [--history EVAL_DIR] [--per-kind 25]

--history: a folder holding earlier runs (<tag>/out/<repo>-differences.md). The
newest earlier sheet for each repo is read, and the verdict, cause and reason
cells of every row that is identical today (same group, line, oracle, dev and v2
text) are copied over, together with the sheet's Status block.
"""
import argparse
import collections
import json
import pathlib
import random
import re
import sys
import tomllib

GROUPS = {
    # kind: (heading, help, sample size factor)
    "gap": ("Gaps: dev is right, v2 is not",
            "What v2 loses against the old engine. Check: is the oracle target right, does dev's edge really go there, and is v2 really wrong?"),
    "v2_wrong": ("Wrong v2 edges",
                 "A v2 edge on a line where the oracle has a call, whose target is none of that line's oracle targets. "
                 "`at call site: no` means the edge sits on no call the oracle saw (for example a decorator line). Check: is v2's target wrong?"),
    "v2_gain": ("v2 gains: v2 is right, dev is not",
                "What v2 adds. Verify a few so the gain is real."),
    "both_miss": ("Both miss",
                  "Neither engine has a right edge. Check the oracle target first; real rows are shared blind spots."),
    "dev_wrong": ("Wrong dev edges",
                  "A dev edge whose target is none of the line's oracle targets. Check a few: this is where dev's precision goes."),
    "v2_unscored": ("v2 edges the score cannot judge",
                    "v2 edges on lines where the oracle has no call with a target v2 has a node for. Not in any score. "
                    "Look for calls the oracle misses (v2 right, oracle silent) and for v2 edges that are plainly wrong."),
    "dev_unscored": ("dev edges the score cannot judge",
                     "The same for dev."),
}
GROUPS["both_right"] = ("Both right (spot check)",
                        "The machine says both engines are right. Check a few: if these are wrong, every score is too high.")
ORDER = ["gap", "v2_wrong", "v2_gain", "both_miss", "dev_wrong", "v2_unscored", "dev_unscored", "both_right"]
SAMPLE = {"gap": 1.0, "v2_wrong": 1.0, "v2_gain": 1.0, "both_miss": 1.0, "dev_wrong": 0.6,
          "v2_unscored": 0.4, "dev_unscored": 0.4, "both_right": 0.4}
# A line that defines a function; its name is the group that matched.
DEF_NAME = re.compile(r"^(?:async\s+)?def\s+(\w+)|^func\s+(?:\([^)]*\)\s*)?(\w+)|"
                      r"^(?:export\s+)?(?:default\s+)?(?:async\s+)?function\s*\*?\s*(\w+)")
STATUS_DEFAULT = [
    "- intern: ",
    "- stage: not started   (not started | verifying | grouping patterns | done)",
    "- language version: (auto)   write a value here to correct the detected one",
    "- framework: (auto)   write a value here to correct the detected one",
    "- next: ",
    "- blocked by: ",
    "- issues filed: ",
]
COLS = "| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |"
CELL_SPLIT = re.compile(r"(?<!\\)\|")


def load_scip_eval(engine_repo):
    sys.path.insert(0, str(pathlib.Path(engine_repo) / "scripts" / "accuracy"))
    import scip_eval  # noqa: PLC0415
    import scip_wire  # noqa: PLC0415
    return scip_eval, scip_wire


def latest_run(wd, prefix, artifact):
    runs = sorted(p for p in wd.glob(prefix + "*") if (p / artifact).exists())
    if not runs:
        raise SystemExit(f"no saved {prefix}* build with {artifact} in {wd}: run graph-eval.sh run first")
    return runs[-1] / artifact


def short(target, n=90):
    return target if len(target) <= n else target[: n - 1] + "…"


def line_text(src, f, ln):
    try:
        return src.text(f, ln).strip()[:120]
    except (OSError, KeyError, IndexError, SystemExit):
        return "(file not in the checkout)"


def ratio(k, n):
    return round(k / n, 4) if n else None


def row_key(kind, row):
    return (kind, f"`{row['file']}:{row['line']}`", *[esc(row[x]) for x in ("oracle", "dev", "v2")])


def pick(kind, rows, n, rng, keep):
    """Rows a person already judged first, then a stratified draw: one row per
    stratum in turn (largest strata first), so one big pattern cannot fill the sheet."""
    kept = [r for r in rows if row_key(kind, r) in keep][:n]
    rest = [r for r in rows if row_key(kind, r) not in keep]
    strata = collections.defaultdict(list)
    for r in rest:
        strata[r.get("stratum", "-")].append(r)
    order = sorted(strata, key=lambda k: (-len(strata[k]), k))
    for k in order:
        rng.shuffle(strata[k])
    out = list(kept)
    while len(out) < n and any(strata.values()):
        for k in order:
            if strata[k] and len(out) < n:
                out.append(strata[k].pop())
    return sorted(out, key=lambda r: (r["file"], r["line"]))


class SitesView:
    """An oracle view whose `sites` are another site table (REFERENCES), so
    scip_eval.line_obligations, which reads `.sites`, builds that relation's
    obligations."""

    def __init__(self, sites):
        self.sites = sites


# relation -> (oracle site attribute, v2 edge list, dev edge list, noun, published key)
RELATIONS = {
    "calls": ("sites", "calls", "calls", "calls", "calls"),
    # REFERENCES: a name used, not called. dev's READS / WRITES are its REFERENCES.
    "references": ("ref_sites", "refs", "refs", "references", "references"),
}


def diff_repo(E, W, repo, cfg, work, out, per_kind, keep, relation="calls"):
    site_attr, v2_attr, dev_attr, noun, pub_key = RELATIONS[relation]
    name, lang = repo["name"], repo["language"]
    wd = work / name
    src_path = wd / "src"
    tool = E.INDEXERS[lang]
    index = E.CACHE / f"{name}@{repo['commit']}@{tool}-{cfg['indexers'][tool]}.scip"
    if not index.exists():
        raise SystemExit(f"no cached SCIP index at {index}")
    _, docs = W.read_index(index.read_bytes())
    src = E.Source(src_path)
    module_path = ""
    if lang == "go":
        m = re.search(r"^module\s+(\S+)", (src_path / "go.mod").read_text(), re.M)
        module_path = m.group(1) if m else ""
    oracle = E.Oracle(docs, src, lang, module_path)

    v2sha, devsha = cfg["engines"]["v2"][:12], cfg["engines"]["legacy"][:12]
    v2 = E.V2(latest_run(wd, f"v2-{v2sha}-run", "out/graph.jsonl").parent, lang)
    leg = E.Legacy(latest_run(wd, f"legacy-{devsha}-run", "export.jsonl"))
    if not hasattr(oracle, site_attr) or not hasattr(v2, v2_attr) or not hasattr(leg, dev_attr):
        raise SystemExit(f"{relation}: the scorer at this v2 commit has no {relation} support")
    osites = getattr(oracle, site_attr)
    view = oracle if relation == "calls" else SitesView(osites)
    v2_all, dev_all = getattr(v2, v2_attr), getattr(leg, dev_attr)

    # Engine edges as scip_eval scores them: (file, line, target), in-repo only.
    v2_edges = [(e["file"], src.line_of(e["file"], e["end"]), e) for e in v2_all
                if e["tier"] not in ("unresolved", "external")]
    dev_edges = [(leg.file_of(c["source"]), c["site_line"], c) for c in dev_all if c.get("site_line")]
    # scip_eval's Legacy.file_of returns "file::<path>" for a call whose source is a file node
    # (module-level code), so those dev edges never meet a line. Kept as the scorer does, counted here.
    scorer_notes = {"dev_edges_with_file_source_never_scored": sum(f.startswith("file::") for f, _, _ in dev_edges),
                    f"dev_{noun}_without_site_line": sum(1 for c in dev_all if not c.get("site_line"))}
    v2_line, v2_line_edges = collections.defaultdict(set), collections.defaultdict(list)
    for f, ln, e in v2_edges:
        v2_line[(f, ln)].add(e["target"])
        v2_line_edges[(f, ln)].append(e)
    dev_line = collections.defaultdict(set)
    for f, ln, c in dev_edges:
        dev_line[(f, ln)].add(c["target"])
    v2_site = collections.defaultdict(list)
    for e in v2_all:
        v2_site[(e["file"], e["end"])].append(e)

    v2_obl, _, _, _ = E.line_obligations(view, lambda t: v2.accepted(t))
    dev_obl, _, _, _ = E.line_obligations(view, lambda t: leg.accepted(t, src))
    # The oracle sites (byte spans) behind each obligation.
    ends = collections.defaultdict(set)
    for (f, end), site in osites.items():
        targets = tuple(sorted(site["targets"]))
        if any(t[0] == "repo" for t in targets):
            ends[((f, site["line"]), targets)].add((f, end))

    def oracle_text(targets):
        return "; ".join(sorted(E.describe(t, src) for t in targets if t[0] == "repo"))

    def edges_text(es):
        return "; ".join(sorted({f"{e['tier']} {short(e['target'])}" for e in es})) or "no edge"

    rows = collections.defaultdict(list)
    counts = collections.Counter()
    miss_types = collections.Counter()  # (group, miss type, reason) for v2 misses
    for ob in sorted(v2_obl, key=repr):
        key, targets = ob
        v2_ids, dev_ids = v2_obl[ob], dev_obl.get(ob, frozenset())
        v2_ok = bool(v2_line.get(key, set()) & v2_ids)
        dev_ok = bool(dev_line.get(key, set()) & dev_ids)
        kind = {(True, True): "both_right", (False, True): "gap",
                (True, False): "v2_gain", (False, False): "both_miss"}[(v2_ok, dev_ok)]
        counts[kind] += 1
        text = line_text(src, key[0], key[1])
        dev_targets = dev_line.get(key, set())
        flags = []
        # The line defines a function with the oracle target's own name (an overload stub, a
        # per-platform re-definition): the oracle read a definition as a call.
        dm = DEF_NAME.match(text) if relation == "calls" else None
        if dm and any(t[0] == "repo" and t[3] == next(g for g in dm.groups() if g) for t in targets):
            flags.append("oracle reads a definition as a call")
            counts[f"def_line_{kind}"] += 1
        if dev_ok and len(dev_targets) > 1:
            flags.append(f"dev has {len(dev_targets)} targets on this line")
            counts[f"dev_multi_{kind}"] += 1
        if not dev_ids:
            flags.append("dev has no node for the target")
        at_site = [e for s in sorted(ends[ob]) for e in v2_site.get(s, ())]
        miss, reason = "", "-"
        if not v2_ok:
            unres = [e for e in at_site if e["tier"] == "unresolved"]
            if not v2_ids:
                miss = "no_node"
            elif any(e["tier"] not in ("unresolved", "external") for e in at_site):
                miss = "wrong_target"
            elif any(e["tier"] == "external" for e in at_site):
                miss = "external"
            elif unres:
                miss = "reported"
            else:
                miss = "silent"
            if unres:
                reason = ", ".join(sorted({e["reason"] or "?" for e in unres}))
            miss_types[(kind, miss, reason if miss == "reported" else "-")] += 1
        v2_on_line = v2_line_edges.get(key, [])
        miss_text = (miss + (f" ({reason})" if miss == "reported" else "")) if miss else ""
        if kind == "v2_gain":
            stratum = "dev no node" if not dev_ids else ("dev wrong edge" if dev_targets else "dev no edge")
        else:
            stratum = miss_text or "-"
        rows[kind].append({
            "file": key[0], "line": key[1], "source": text,
            "oracle": oracle_text(targets),
            "dev": "; ".join(sorted(short(t) for t in dev_targets)) or "no edge",
            "v2": edges_text(at_site if at_site else v2_on_line) if (at_site or v2_on_line) else "no edge",
            "miss": "; ".join(([miss_text] if miss_text else []) + flags),
            "stratum": stratum,
        })

    # Precision side, exactly as scip_eval's line_view judges in-repo edges.
    ok_at = collections.defaultdict(set)
    obl_at = collections.defaultdict(list)
    for (key, targets), alts in v2_obl.items():
        if alts:
            ok_at[key] |= alts
            obl_at[key].append(targets)
    dev_ok_at = collections.defaultdict(set)
    dev_obl_at = collections.defaultdict(list)
    for (key, targets), alts in dev_obl.items():
        if alts:
            dev_ok_at[key] |= alts
            dev_obl_at[key].append(targets)

    def judge(edges, ok_map, obl_map, kind, other_line, desc):
        right = scored = 0
        seen = collections.Counter()
        for f, ln, e in edges:
            tgt = e["target"]
            if (f, ln) not in ok_map:
                counts[kind.replace("wrong", "unscored")] += 1
                seen[("u", f, ln, desc(e))] += 1
                continue
            scored += 1
            if tgt in ok_map[(f, ln)]:
                right += 1
                continue
            counts[kind] += 1
            seen[("w", f, ln, desc(e))] += 1
        for (w, f, ln, d), n in sorted(seen.items()):
            obls = obl_map.get((f, ln), [])
            rows[kind if w == "w" else kind.replace("wrong", "unscored")].append({
                "file": f, "line": ln, "source": line_text(src, f, ln),
                "oracle": "; ".join(sorted({oracle_text(t) for t in obls})) or "no oracle call with a target",
                "dev" if kind == "v2_wrong" else "v2": "; ".join(sorted(short(t) for t in other_line.get((f, ln), ()))) or "no edge",
                "v2" if kind == "v2_wrong" else "dev": d + (f" ×{n}" if n > 1 else ""),
                "miss": "", "stratum": d.rsplit("(", 1)[-1] if kind == "v2_wrong" else "-",
            })
        return right, scored

    def v2_desc(e):
        at = "yes" if (e["file"], e["end"]) in osites else "no"
        return f"{e['tier']} {short(e['target'])} (at {'call' if relation == 'calls' else 'reference'} site: {at})"


    v2_right, v2_scored = judge(v2_edges, ok_at, obl_at, "v2_wrong", dev_line, v2_desc)
    dev_right, dev_scored = judge(dev_edges, dev_ok_at, dev_obl_at, "dev_wrong", v2_line, lambda c: short(c["target"]))

    obligations = sum(counts[k] for k in ("gap", "v2_gain", "both_miss", "both_right"))
    mine = {
        "v2_recall": [counts["both_right"] + counts["v2_gain"], obligations],
        "dev_recall": [counts["both_right"] + counts["gap"], obligations],
        "v2_precision": [v2_right, v2_scored],
        "dev_precision": [dev_right, dev_scored],
    }
    check = {"mode": "skipped: no <repo>.json"}
    scores_file = out / f"{name}.json"
    s = json.loads(scores_file.read_text()) if scores_file.exists() else None
    if s and relation == "calls":
        pub = {
            "v2_recall": s["v2"]["calls"]["line_level"]["recall"],
            "dev_recall": s["legacy"]["calls"]["recall"],
            "v2_precision": s["v2"]["calls"]["line_level"]["precision"],
            "dev_precision": s["legacy"]["calls"]["precision"],
        }
        sampled = s["v2"]["calls"].get("mode") != "all"
        bad = {k: {"here": mine[k], "published": [pub[k]["k"], pub[k]["n"]]}
               for k in mine if [pub[k]["k"], pub[k]["n"]] != mine[k]}
        check = {"mode": "sampled score: counts differ by design" if sampled else "full",
                 "ok": not bad or sampled, "mismatches": bad,
                 "v2_site_precision": s["v2"]["calls"]["precision"]["overall"]}
    elif s and relation == "references":
        # v2 REFERENCES are published at the exact site, not by line: only dev's line figures compare.
        leg_pub = s["legacy"].get("references") or {}
        if "precision" in leg_pub:
            pub = {"dev_recall": leg_pub["recall"], "dev_precision": leg_pub["precision"]}
            sampled = len(osites) >= cfg["sample_threshold"]
            bad = {k: {"here": mine[k], "published": [pub[k]["k"], pub[k]["n"]]}
                   for k in pub if [pub[k]["k"], pub[k]["n"]] != mine[k]}
            check = {"mode": "full (dev only; v2 is published by exact site)", "ok": not bad or sampled, "mismatches": bad,
                     "v2_site_precision": (s["v2"].get("references") or {}).get("precision", {}).get("overall")}
        else:
            check = {"mode": "skipped: <repo>.json has no dev REFERENCES score"}

    rng = random.Random(f"{cfg['seed']}:{name}:diff" + ("" if relation == "calls" else f":{relation}"))
    picked = {k: pick(k, rows.get(k, []), max(5, round(per_kind * SAMPLE[k])), rng, keep) for k in ORDER}
    all_rows = [(k, r) for k in ORDER if k != "both_right" for r in rows.get(k, [])]
    return all_rows, {
        "relation": relation,
        "repo": name, "language": lang, "commit": repo["commit"], "url": repo.get("url", ""),
        "engines": cfg["engines"], "obligations": obligations,
        "counts": {k: counts.get(k, 0) for k in ORDER},
        # Rows per group (wrong and unscored rows merge equal edges on one line, so rows <= edges),
        # and rows per sampling stratum, so a report can weight a stratified sample back.
        "rows": {k: len(rows.get(k, [])) for k in ORDER},
        "strata": {k: dict(collections.Counter(r.get("stratum", "-") for r in rows.get(k, []))) for k in ORDER},
        "flags": {k: v for k, v in sorted(counts.items()) if k.startswith(("def_line_", "dev_multi_"))},
        "rates": {k: ratio(*v) for k, v in mine.items()},
        "fractions": mine,
        "check": check,
        "scorer_notes": scorer_notes,
        "v2_misses": [[g, m, r, n] for (g, m, r), n in miss_types.most_common()],
        "samples": picked,
    }


# ------------------------------------------- all relations, v2 against dev (no oracle)

V2_TYPES = ["CALLS", "IMPORTS", "REFERENCES", "EXTENDS", "CONTAINS", "TESTS", "ASSERTS",
            "MOCKS", "HANDLES", "ACCESSES", "INVOKES", "NAVIGATES", "COVERS"]
# The old engine's edge types on graph v2's thirteen (ADR 0001). None: no v2 counterpart.
DEV_TO_V2 = {
    "CALLS": "CALLS", "DECORATES": "CALLS",
    "USES": "REFERENCES", "READS": "REFERENCES", "WRITES": "REFERENCES", "HAS_TYPE": "REFERENCES",
    "ACCEPTS": "REFERENCES", "RETURNS": "REFERENCES",
    "IMPORTS": "IMPORTS", "DEPENDS_ON": "IMPORTS",
    "EXTENDS": "EXTENDS", "IMPLEMENTS": "EXTENDS", "OVERRIDES": "EXTENDS", "INHERITS": "EXTENDS",
    "CONTAINS": "CONTAINS", "HAS_METHOD": "CONTAINS", "BELONGS_TO": "CONTAINS",
    # v2 makes a pytest fixture lookup a REFERENCES edge (rule fixture.pytest_lookup), not TESTS.
    "USES_FIXTURE": "REFERENCES",
    "TEST_COVERS_ROUTE": "TESTS",
    "MOCKS_MODULE": "MOCKS",
    "ROUTE_HANDLER": "HANDLES", "LISTENS_SIGNAL": "HANDLES", "MIDDLEWARE": "HANDLES",
    "ACCESSES_MODEL": "ACCESSES", "MAPS_TO_TABLE": "ACCESSES",
    "FETCHES_API": "INVOKES", "CROSS_SERVICE": "INVOKES", "PUBLISHES_EVENT": "INVOKES", "SUBSCRIBES_EVENT": "INVOKES",
    "NAVIGATES_TO": "NAVIGATES",
}
DEV_REVERSED = {"BELONGS_TO"}  # stored child -> parent; v2 CONTAINS is parent -> child
V2_SIG = re.compile(r"#[0-9a-f]{8}$")
V2_NON_SYMBOL = ("surface", "data", "framework", "pkg", "unresolved")
PAIR_GROUPS = {
    "only_v2": ("Only v2 has it", "v2 has this edge, dev does not. Check: is the edge real in the code (v2 gain) or wrong (v2 wrong)?"),
    "only_dev": ("Only dev has it", "dev has this edge, v2 does not. Check: is it real (a v2 gap) or wrong (dev wrong)?"),
    "both": ("Both have it (spot check)", "Both engines agree. Check a few: an agreement can still be wrong."),
}
PAIR_COLS = "| # | from | to | v2 | dev | where | verdict | cause |"


def v2_key(node_id):
    """(file, dotted name) of a v2 symbol or file id; ("", id) for a surface, data, package or stub."""
    parts = node_id.split("::", 3)
    if len(parts) < 4 or parts[0] in V2_NON_SYMBOL:
        return ("", node_id)
    path, desc = parts[2], V2_SIG.sub("", parts[3])
    mod = path.rsplit(".", 1)[0]
    if desc.startswith(mod + "/"):
        desc = desc[len(mod) + 1:]
    elif desc in (mod, mod + "/"):
        desc = ""
    s = re.sub(r"[#/`]", ".", desc.replace("().", ".").replace("()", ""))
    return (path, re.sub(r"\.+", ".", s).strip("."))


def dev_key(node_id):
    """(file, dotted name) of a dev id: kind::file::Scope::name, or path:line:col for a file or folder."""
    if "::" in node_id:
        p = node_id.split("::")
        return (p[1], ".".join(p[2:]))
    return (re.sub(r":\d+:\d+$", "", node_id), "")


def structure_only(rel, a, b):
    """A pair one engine has by design and the other never makes: CONTAINS into a
    v2 Condition node (`<callable>::cond<n>`), or CONTAINS from or to a folder or
    file (dev; v2 keeps file membership in its ids). Counted, not compared."""
    if rel != "CONTAINS":
        return None
    if "::cond" in b[1]:
        return "CONTAINS to a condition (v2 only)"
    if not a[1] or not b[1]:
        return "CONTAINS from or to a folder or file (dev only)"
    return None


MATCH_DROP = re.compile(r"[^A-Za-z0-9_$]+")
# Readable name of each match key, from the first engine that named it.
DISPLAY = {}


def match_key(k):
    """The key pairs are matched on: the file and the name with only letters, digits,
    `_` and `$` kept. The engines spell test names differently (v2:
    `"Command.parse"#"when x"`, dev: `Commandparse  when x`) and join scopes with
    different separators; the letters are the same."""
    m = (k[0], MATCH_DROP.sub("", k[1]))
    DISPLAY.setdefault(m, k)
    return m


def key_text(k):
    k = DISPLAY.get(k, k)
    return f"{k[0]}::{k[1]}" if k[0] and k[1] else (k[0] or k[1])


def read_v2_pairs(graph):
    """{v2 type: {(from key, to key): (file, line) of one edge}} plus skipped counts."""
    pairs, skipped, lines = collections.defaultdict(dict), collections.Counter(), {}
    with open(graph) as fh:
        for ln in fh:
            d = json.loads(ln)
            r = d.get("row") or {}
            if d.get("section") != "edges":
                continue
            t = r.get("type")
            if r.get("resolution") in ("unresolved", "external"):
                skipped[f"{t} {r.get('resolution')}"] += 1
                continue
            sp = r.get("span") or {}
            a, b = v2_key(r["source"]), v2_key(r["target"])
            why = structure_only(t, a, b)
            if why:
                skipped[why] += 1
                continue
            pairs[t].setdefault((match_key(a), match_key(b)), (sp.get("file", ""), sp.get("start_byte")))
    return pairs, skipped


def read_dev_pairs(export):
    """{v2 type: {(from key, to key): dev type}} from the export's "edge" rows, and unmapped type counts."""
    pairs, unmapped, seen = collections.defaultdict(dict), collections.Counter(), False
    with open(export) as fh:
        for ln in fh:
            d = json.loads(ln)
            if d.get("kind") != "edge":
                continue
            seen = True
            t = d.get("label", "")
            v2t = DEV_TO_V2.get(t)
            if not v2t:
                unmapped[t] += 1
                continue
            a, b = dev_key(d["source"]), dev_key(d["target"])
            if t in DEV_REVERSED:
                a, b = b, a
            why = structure_only(v2t, a, b)
            if why:
                unmapped[why] += 1
                continue
            pairs[v2t].setdefault((match_key(a), match_key(b)), t)
    return pairs, unmapped, seen


def parse_pair_sheet(path):
    cells, group = {}, None
    if not path or not path.exists():
        return cells
    for line in path.read_text().splitlines():
        m = re.match(r"<!-- group: (\w+) -->", line)
        if m:
            group = m.group(1)
            continue
        if group and re.match(r"^\| *\d+ *\|", line):
            c = [x.strip() for x in CELL_SPLIT.split(line)[1:-1]]
            if len(c) == 8 and any(c[6:]):
                cells[(group, c[1], c[2])] = (c[6], c[7])
    return cells


def diff_pairs(repo, cfg, v2_graph, dev_export, src, out, history, per_kind):
    """Every v2 edge type against the old engine's edges mapped onto it, matched by
    (file, dotted name) of both ends. No oracle: a person judges the sampled rows.
    Writes <repo>-<relation>-pairs-differences.md per relation with edges and
    <repo>-relations.md with the counts of all thirteen."""
    name = repo["name"]
    v2p, v2_skipped = read_v2_pairs(v2_graph)
    devp, unmapped, has_edges = read_dev_pairs(dev_export)
    if not has_edges:
        raise SystemExit("the old engine export has no edge rows: rebuild it with the current exporter")
    rng = random.Random(f"{cfg['seed']}:{name}:pairs")
    summary, all_rows = [], []

    def where(loc):
        if not loc or not loc[0] or loc[1] is None:
            return "-"
        try:
            return f"{loc[0]}:{src.line_of(loc[0], loc[1])}"
        except (SystemExit, Exception):
            return loc[0]

    for rel in V2_TYPES:
        v, dv = v2p.get(rel, {}), devp.get(rel, {})
        groups = {"both": sorted(set(v) & set(dv)), "only_v2": sorted(set(v) - set(dv)), "only_dev": sorted(set(dv) - set(v))}
        union = len(set(v) | set(dv))
        summary.append((rel, len(v), len(dv), *(len(groups[g]) for g in ("both", "only_v2", "only_dev")),
                        f"{100 * len(groups['both']) / union:.1f}%" if union else "-"))
        if not union:
            continue
        sheet = out / f"{name}-{rel.lower()}-pairs-differences.md"
        prev = sheet if sheet.exists() else previous_sheet(history, out, name, f"{rel.lower()}-pairs-differences.md")
        carried = parse_pair_sheet(prev)
        dev_types = collections.Counter(dv.values())
        L = [f"# {name} ({repo['language']}): {rel}, graph v2 against dev", "",
             f"Engines: v2 `{cfg['engines']['v2'][:12]}`, dev `{cfg['engines']['legacy'][:12]}`. No oracle: you judge each row.", "",
             "## Counts", "",
             f"v2 {len(v)} pairs, dev {len(dv)} pairs (dev types: {', '.join(f'{t} {n}' for t, n in dev_types.most_common()) or 'none'}).",
             f"Both {len(groups['both'])}, only v2 {len(groups['only_v2'])}, only dev {len(groups['only_dev'])}; "
             f"agreement {summary[-1][-1]} of the union.",
             "Pairs are matched on (file, name with only letters and digits) of both ends, so the engines' different "
             "spellings of one test or scope meet; an edge to a route, data or package node "
             "(v2) has no dev counterpart. v2 unresolved and external edges are left out.", "",
             "Verdict: `confirmed` (the group is right), `v2 wrong`, `dev wrong`, `both wrong`, or `?`. Cause: one short phrase.", ""]
        for g in ("only_v2", "only_dev", "both"):
            rows = groups[g]
            picked = sorted(rows if len(rows) <= per_kind else rng.sample(rows, per_kind))
            title, help_ = PAIR_GROUPS[g]
            L += [f"## {title} ({len(picked)} of {len(rows)})", f"<!-- group: {g} -->", "", help_, "", PAIR_COLS,
                  "|---|---|---|---|---|---|---|---|"]
            for i, (a, b) in enumerate(picked, 1):
                fa, fb = esc(f"`{key_text(a)}`"), esc(f"`{key_text(b)}`")
                vd, cs = carried.get((g, fa, fb), ("", ""))
                L.append(f"| {i} | {fa} | {fb} | {'yes' if (a, b) in v else 'no'} | {dv.get((a, b), 'no')} | "
                         f"{esc(where(v.get((a, b))))} | {vd} | {cs} |")
            L.append("")
            all_rows += [(rel, g, key_text(a), key_text(b)) for a, b in rows]
        sheet.write_text("\n".join(L) + "\n")

    S = [f"# {name}: all relations, graph v2 against dev", "",
         "| relation | v2 pairs | dev pairs | both | only v2 | only dev | agreement |", "|---|---|---|---|---|---|---|"]
    S += [f"| {rel} | {a} | {b} | {c} | {d} | {e} | {f} |" for rel, a, b, c, d, e, f in summary]
    S += ["", f"dev edges not compared (no v2 counterpart, or structure v2 does not keep as edges): {dict(unmapped.most_common()) or 'none'}.",
          f"v2 edges not compared (unresolved, external, or structure dev never makes): {dict(v2_skipped.most_common()) or 'none'}.",
          "Sheets: `<repo>-<relation>-pairs-differences.md` for every relation with edges."]
    (out / f"{name}-relations.md").write_text("\n".join(S) + "\n")
    with open(out / f"{name}-relations-rows.tsv", "w") as fh:
        fh.write("relation\tgroup\tfrom\tto\n")
        fh.writelines(f"{r}\t{g}\t{a}\t{b}\n" for r, g, a, b in all_rows)
    return summary, unmapped


# ------------------------------------------------------------------ the sheet

def parse_sheet(path):
    """(kind, file:line, oracle, dev, v2) -> (verdict, cause, reason), and the Status lines."""
    cells, status, kind, in_status = {}, [], None, False
    for line in path.read_text().splitlines():
        if line.startswith("## "):
            in_status = line.startswith("## Status")
            continue
        m = re.match(r"<!-- kind: (\w+) -->", line)
        if m:
            kind = m.group(1)
            continue
        if in_status and line.startswith("- "):
            status.append(line)
            continue
        if kind and re.match(r"^\| *\d+ *\|", line):
            c = [x.strip() for x in CELL_SPLIT.split(line)[1:-1]]
            if len(c) > 10:  # a "|" typed in the cause cell
                c = c[:8] + [" / ".join(c[8:-1]), c[-1]]
            if len(c) == 10 and any(c[7:]):
                cells[(kind, c[1], c[3], c[4], c[5])] = (c[7], c[8], c[9])
    return cells, status


def esc(x):
    return x.replace("|", "\\|")


def write_sheet(path, r, carried, status):
    c = r["counts"]
    f = r["fractions"]
    pct = lambda kn: f"{100 * kn[0] / kn[1]:.1f}% ({kn[0]}/{kn[1]})" if kn[1] else "n/a"
    rel = r.get("relation", "calls")
    REL, what = rel.upper(), ("calls" if rel == "calls" else "references (a name used, not called)")
    L = [f"# {r['repo']} ({r['language']}): graph differences to verify"
         + ("" if rel == "calls" else f", {REL}"), "",
         f"Repo `{r['url']}` at `{r['commit']}`. Old engine `{r['engines']['legacy'][:12]}`, graph v2 `{r['engines']['v2'][:12]}`.", "",
         "## Status", "",
         "Fill this in. `graph-eval.sh report` reads it, and the next run copies it forward.", ""]
    L += status or STATUS_DEFAULT
    L += ["", "## Counts", "",
          f"In-repo {what} found by the oracle: {r['obligations']}. Both right {c['both_right']}, gap {c['gap']}, "
          f"v2 gain {c['v2_gain']}, both miss {c['both_miss']}.",
          f"Scored edges: v2 {f['v2_precision'][1]} ({c['v2_wrong']} wrong), dev {f['dev_precision'][1]} ({c['dev_wrong']} wrong). "
          f"Not scored: v2 {c['v2_unscored']}, dev {c['dev_unscored']}.",
          f"{REL} recall: dev {pct(f['dev_recall'])}, v2 {pct(f['v2_recall'])}. "
          f"{REL} precision: dev {pct(f['dev_precision'])}, v2 {pct(f['v2_precision'])}.",
          *([] if rel == "calls" else [
              "dev's REFERENCES are its READS / WRITES: module-level variables only, so its recall is low by design. "
              "v2 REFERENCES are reads, writes and type annotations; only the target is judged, not the access."]),
          "Line precision judges each engine only on lines where the oracle has a call it can map, and counts "
          "edges that sit on no oracle call (decorator lines) as wrong. Do not rank the engines on it alone.",
          f"v2 precision at exact call sites (published): {(r['check'].get('v2_site_precision') or {}).get('value')}.",
          f"Flags: {json.dumps(r['flags'])} (def_line_* = the line defines a function of the target's own name, usually the oracle's mistake; "
          "dev_multi_* = dev was right but had several targets on the line).",
          f"Scorer notes: {json.dumps(r['scorer_notes'])}.",
          f"Check against the published scores: {'OK' if r['check'].get('ok') else 'MISMATCH ' + json.dumps(r['check'].get('mismatches'))} ({r['check']['mode']}).", ""]
    if carried:
        L += [f"{carried[0]} verdicts copied from `{carried[1]}` (rows identical to that run).", ""]
    L += ["## How each v2 miss happened", "",
          "| group | v2 miss | reason | calls |", "|---|---|---|---|"]
    L += [f"| {g} | {m} | {rs} | {n} |" for g, m, rs, n in r["v2_misses"]] or ["| - | - | - | 0 |"]
    L += ["",
          "`no_node`: v2 has no node for the target. `wrong_target`: v2 resolved this call to another target. "
          "`external`: v2 called it external. `reported`: only unresolved edges, with v2's reason. "
          "`silent`: no v2 edge at this call at all.", "",
          "Verdict: `confirmed` (the row is what its group says), `oracle wrong`, `dev wrong`, `v2 right after all`, or `?`.",
          "Cause: one short phrase for the code shape (for example `method on a constructor-injected field`). Reuse phrases.",
          "Reason true: for a `reported` miss, `yes` or `no`.", ""]
    for kind in ORDER:
        title, help_ = GROUPS[kind]
        rows = r["samples"].get(kind, [])
        n_rows = r["rows"].get(kind, 0)
        size = f"{len(rows)} of {n_rows}" + (f" rows, {c.get(kind, 0)} edges" if n_rows != c.get(kind, 0) else "")
        L += [f"## {title} ({size})", f"<!-- kind: {kind} -->", "", help_, "", COLS,
              "|---|---|---|---|---|---|---|---|---|---|"]
        for i, row in enumerate(rows, 1):
            fixed = [f"`{row['file']}:{row['line']}`", f"`{row['source']}`", row["oracle"], row["dev"], row["v2"]]
            fixed = [esc(x) for x in fixed]
            v = carried[2].get((kind, *[fixed[0]] + fixed[2:]), ("", "", "")) if carried else ("", "", "")
            L.append("| " + " | ".join([str(i)] + fixed + [esc(row["miss"]), *v]) + " |")
        L.append("")
    path.write_text("\n".join(L) + "\n")


def previous_sheet(history, out, name, suffix="differences.md"):
    if not history or not history.is_dir():
        return None
    here = out.resolve()
    cands = [p for p in history.glob(f"*/out/{name}-{suffix}") if p.parent.resolve() != here]
    return max(cands, key=lambda p: p.stat().st_mtime) if cands else None


def write_rows_tsv(path, all_rows):
    cols = ["group", "file", "line", "notes", "oracle", "dev", "v2", "source"]
    with open(path, "w") as fh:
        fh.write("\t".join(cols) + "\n")
        for k, r in all_rows:
            vals = [k, r["file"], str(r["line"]), r["miss"], r["oracle"], r["dev"], r["v2"], r["source"]]
            fh.write("\t".join(v.replace("\t", " ") for v in vals) + "\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--engine-repo", required=True)
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--work", required=True, type=pathlib.Path)
    ap.add_argument("--out", required=True, type=pathlib.Path)
    ap.add_argument("--history", type=pathlib.Path)
    ap.add_argument("--per-kind", type=int, default=25)
    a = ap.parse_args()
    E, W = load_scip_eval(a.engine_repo)
    cfg = tomllib.loads(pathlib.Path(a.manifest).read_text())
    a.out.mkdir(parents=True, exist_ok=True)
    bad = 0
    # CALLS keeps its file names (<repo>-differences.md, ...); each other relation
    # gets its own sheet, <repo>-<relation>-differences.md, so verdicts carry per relation.
    jobs = [(repo, rel) for repo in cfg["repos"] for rel in RELATIONS]
    for repo, relation in jobs:
        name = repo["name"]
        prefix = name if relation == "calls" else f"{name}-{relation}"
        suffix = "differences.md" if relation == "calls" else f"{relation}-differences.md"
        sheet = a.out / f"{prefix}-differences.md"
        # Never lose a person's verdicts: read today's sheet if it exists, else the newest earlier one.
        src_sheet = sheet if sheet.exists() else previous_sheet(a.history, a.out, name, suffix)
        cells, status = parse_sheet(src_sheet) if src_sheet else ({}, [])
        try:
            all_rows, r = diff_repo(E, W, repo, cfg, a.work.resolve(), a.out, a.per_kind, set(cells), relation)
        except (SystemExit, Exception) as e:  # one bad repo must not stop the others
            print(f"{name} {relation}: skipped: {type(e).__name__}: {e}", file=sys.stderr)
            bad |= relation == "calls"  # an older scorer without REFERENCES is no failure
            continue
        keys = {row_key(k, row) for k, rs in r["samples"].items() for row in rs}
        if src_sheet and src_sheet != sheet:
            # New engines or a new day: a "done" repository has new unjudged rows if anything changed.
            open_rows = sum(len(rs) for rs in r["samples"].values()) - len(keys & set(cells))
            status = [re.sub(r"^- stage:\s*done\b.*", "- stage: verifying   (new rows to judge after the engines changed)", l)
                      if open_rows else l for l in status]
        carried = (len(keys & set(cells)), str(src_sheet), cells) if cells else None
        r["verdicts_carried"] = carried[0] if carried else 0
        (a.out / f"{prefix}-diff.json").write_text(json.dumps(r, indent=2, sort_keys=True) + "\n")
        write_rows_tsv(a.out / f"{prefix}-rows.tsv", all_rows)
        write_sheet(sheet, r, carried, status)
        c = r["counts"]
        ok = r["check"].get("ok")
        bad |= ok is False
        print(f"{name}: {RELATIONS[relation][3]} {r['obligations']}: both right {c['both_right']}, gap {c['gap']}, v2 gain {c['v2_gain']}, "
              f"both miss {c['both_miss']}; wrong edges v2 {c['v2_wrong']}, dev {c['dev_wrong']}; "
              f"check {'OK' if ok else 'MISMATCH'}" + (f"; {carried[0]} verdicts carried" if carried else "") + f" -> {sheet}")
        if ok is False:
            print(f"{name}: counts do not match the published scores: {r['check']['mismatches']}", file=sys.stderr)
    # All thirteen v2 relations against dev, with no oracle (a person judges the rows).
    for repo in cfg["repos"]:
        name = repo["name"]
        wd = a.work.resolve() / name
        try:
            v2sha, devsha = cfg["engines"]["v2"][:12], cfg["engines"]["legacy"][:12]
            summary, _ = diff_pairs(repo, cfg, latest_run(wd, f"v2-{v2sha}-run", "out/graph.jsonl"),
                                    latest_run(wd, f"legacy-{devsha}-run", "export.jsonl"),
                                    E.Source(wd / "src"), a.out, a.history, a.per_kind)
        except (SystemExit, Exception) as e:
            print(f"{name} relations: skipped: {type(e).__name__}: {e}", file=sys.stderr)
            continue
        print(f"{name}: relations v2/dev/both: " + ", ".join(f"{r} {v}/{d}/{b}" for r, v, d, b, *_ in summary if v or d)
              + f" -> {a.out / (name + '-relations.md')}")
    sys.exit(bad)


if __name__ == "__main__":
    main()
