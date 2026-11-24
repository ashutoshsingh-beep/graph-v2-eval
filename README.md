# SCIP scorer changes (my notes)

Repo: `~/CodeParser/codeparser-scip-ts` (worktree of codeparser)
Branch: `feat/scip-eval-references`, based on `fleet/graph-v2` @ `b3cd5e698`
File: `scripts/accuracy/scip_eval.py` unless noted. Not pushed.

---

## Commit 1: `5b18ef534`, TS oracle covers the whole repo
Also on branch `fix/scip-ts-include-all`.

**Why**
- scip-typescript followed the repo's `tsconfig.json` `include`.
- commander.js includes only root `*.js` and `lib/**`, so `tests/` and `examples/` had no oracle calls.
- Both engines read every file, so their edges there went unscored.
- Python already avoided this with a temp `pyrightconfig.json`.

**What changed**: `scip_index()`
- Before indexing a TS repo: rename `tsconfig.json` → `tsconfig.scip-eval-orig.json`.
- Write a temp `tsconfig.json`: `extends` the original + `include: ["**/*"]` + `allowJs`.
- Restore the original in `finally`, so the checkout stays pristine.
- Record the temp config as `"tsconfig"` in the index metadata.
- Delete old TS `.scip` files in `~/Library/Caches/covlant-eval/scip/`; the cache name doesn't include the config.

---

## Commit 2: `7e5451d85`, REFERENCES scoring
REFERENCES = a name **used but not called** (read, write, type annotation).

**Why**
- The scorer only did CALLS + IMPORTS; the lead asked for more relations.
- SCIP has no "reference" role, so a reference = a SCIP reference that isn't a call.
- scip-python / scip-typescript give imported names **no Import bit**, so import lines must be skipped by hand.

**Oracle side (SCIP)**
- `is_reference_site(start, end, excluded)` (~line 412): true if the span is in no excluded range.
- `reference_excluded_ranges(src, path, lang)` (~line 428): ranges to skip.
  - Python (`ast`): import statements + class base lists (`class A(Base)` = EXTENDS).
  - TS (`TS_IMPORT_RE`, lexical): `import … from`, `export … from`, `import x = require()`.
- `Oracle.__init__`
  - new `self.ref_sites` (~line 481), same shape as `self.sites`.
  - in the occurrence loop: a call → `self.sites` (unchanged); not a call and not excluded → `self.ref_sites`.
  - targets via the same `target()`; its counters for refs are renamed `reference_*`, so call counters don't change.
  - new count: `reference_in_import_or_base_list`.

**v2 side**
- `class V2` (~line 750): reads `REFERENCES` edges into `self.refs` (keeps `access`, `rule`).
- Skips rules `fixture.*` / `data.*` (pytest fixtures, Django FK) → counted in `refs_skipped`.

**dev side**
- `_legacy_export_sites/main.go`: emits dev `READS` / `WRITES` (`st.NativeRelationships`) as `kind: "reference"` rows with `label` (reads/writes) + `site_line`.
- `class Legacy` (~line 805): loads them into `self.refs`.

**Scoring**
- `score_v2_references()` (~line 1012): join at `(file, end byte)`, like CALLS exact site.
  - Precision: overall, repo, external, by tier, by access (read/write/type, info only).
  - Recall: repo, external, overall; diagnostic `found_only_as_a_calls_edge`.
  - Unjudged: `no_oracle_site`, `at_oracle_call_site`, `unresolved`, `oracle_target_not_a_v2_node`, `fixture_or_data_rule`.
- `_RefOracle` (~line 1228): 3-line adapter, `.sites = oracle.ref_sites`, so `line_score()` can be reused unchanged.
- `score_legacy_references()` (~line 1236): dev by `(file, line)` via `line_score()`, like dev CALLS.
  - Python only. TS → "not scored" (dev TS writes the **function's first line**, not the access line).
- `evaluate()`: own seed `"<seed>:<repo>:references"`, so CALLS/IMPORTS samples don't change.
  - report keys: `v2.references`, `legacy.references`, `oracle.reference_sites`.
- `write_summary()`: REFERENCES table + one dev line in `summary.md`.

**Tests**: `test_scip_eval.py` → `class ReferencesTest` (6 tests)
- reference vs call vs import vs base list, Python + TS
- v2 right / wrong / unresolved / fixture edge
- dev by line

**Kit** (`~/Downloads/kit/graph-eval.sh`, not in git)
- `scores` prints 4 rows: REFERENCES in-repo / external × precision / recall (v2; dev `-`).

---

---

## Later commits on `feat/scip-eval-references`
- `27f084563`: dev TS REFERENCES scored by line too (needs dev branch `fix/dev-ts-reads-writes-line`, `3589a9313`: TS READS/WRITES carry the access line).
- `66de33f4c`: `V2.refs` rows keep `reason` (graph_diff needs it).
- `5b0a3f7fc`: `main.go` writes **every** dev graph edge as `kind: "edge"` + type in `label`.

## Kit `graph_diff.py` (not in git)
**REFERENCES worksheet (SCIP oracle)**
- `diff_repo(..., relation)`: `calls` or `references` (`RELATIONS` table).
- References use `oracle.ref_sites`, `v2.refs`, `leg.refs`; `SitesView` feeds `line_obligations`.
- Files: `<repo>-references-differences.md`, `-references-rows.tsv`, `-references-diff.json`. CALLS files unchanged.

**All 13 relations, v2 vs dev (no oracle, you judge)**
- `diff_pairs()`: per v2 type, set compare of `(from, to)` pairs → `both` / `only_v2` / `only_dev`.
- `DEV_TO_V2`: dev type → v2 type (READS/WRITES/HAS_TYPE/ACCEPTS/RETURNS/USES/USES_FIXTURE → REFERENCES, HAS_METHOD/BELONGS_TO → CONTAINS, IMPLEMENTS/OVERRIDES → EXTENDS, …).
- IDs matched as `(file, dotted name)`: `v2_key()`, `dev_key()`.
- `structure_only()`: CONTAINS to v2 conditions / dev folder+file containment → counted, not compared.
- v2 unresolved + external edges left out (counted).
- Files: `<repo>-relations.md` (13-row table), `<repo>-<relation>-pairs-differences.md`, `<repo>-relations-rows.tsv`.

**First results (saved builds)**
- click: IMPORTS 80%, EXTENDS 67%, CALLS 29%, REFERENCES 24% agreement.
- commander.js CALLS 2%: v2 resolves to `typings/index.d.ts`, dev to `lib/command.js` (real difference).
- CONTAINS: dev class→method, v2 none; v2 describe→test and function→condition.

## Known limits
- Read vs write is **not** checked; SCIP doesn't mark them. Only the target is scored.
- Dev REFERENCES = module-level variables only, so dev recall is low by design.
- Dev TypeScript REFERENCES are not scored (line = function start; design in dev's `analyze.ts`, impact-analysis only).
- Type annotations aren't separated; they're counted as normal references.
- TS imports are found by regex, not a parser.

## Tried and reverted
- Scoring dev TS REFERENCES by file + target (line ignored): reverted, kept "not scored".

## Status
- Tests: all new pass; 2 old failures in `test_directory_input.py` (also fail without these changes).
- Kit rerun **not done yet**: last try stopped at `disk floor reached` (3.5 GB free, needs 8 GB).
- Run: `export PATH="$PATH:$HOME/go/bin" KIT_HOME=~/CodeParser DEV_REF=origin/development V2_REF=feat/scip-eval-references SKIP_PARSER_BUILD=1; ./graph-eval.sh run ~/CodeParser/repos-day1.tsv <tag>`
