# SCIP accuracy evaluation

Method: `docs/graph-v2/accuracy-method.md`. Intervals are 95% Wilson. Precision first.

## click (python) @ `934813e4d421`

Oracle scip-python 0.6.6: 3794 call sites. v2 `b3cd5e698314`, old engine `25ae40bf8662`. Scoring: all.

### CALLS, v2 by site (callee span end)

| tier | precision | edges judged of population |
|---|---|---|
| exact | 0.0% [0.0, 56.1] (n=3) | 3 of 3 |
| import | 100.0% [99.7, 100.0] (n=1460) | 1460 of 1460 |
| name | 99.8% [98.7, 100.0] (n=424) | 424 of 424 |
| external | 100.0% [99.4, 100.0] (n=666) | 666 of 666 |
| external_module | 86.5% [83.7, 88.9] (n=666) | 666 of 666 |
| overall | 99.8% [99.6, 99.9] (n=2553) | 2553 of 2553 |

| recall | value |
|---|---|
| repo | 82.1% [80.5, 83.6] (n=2293) |
| external | 59.2% [56.4, 62.1] (n=1124) |
| overall | 74.6% [73.1, 76.0] (n=3417) |

| recall by tier (share of all oracle sites a right edge of that tier finds) | value |
|---|---|
| exact | 0.0% [0.0, 0.1] (n=3417) |
| import | 42.7% [41.1, 44.4] (n=3417) |
| name | 12.4% [11.3, 13.5] (n=3417) |
| external | 19.5% [18.2, 20.8] (n=3417) |

Unjudged v2 edges: `{"no_oracle_site": 1641, "oracle_target_local_or_unknown": 266}`. Oracle sites whose in-repo target has no v2 node (misses in recall): 8; in-repo recall without them, a diagnostic: 82.4% [80.8, 83.9] (n=2285).

### CALLS, both engines by line, in-repo targets

| engine | precision | recall | oracle targets on lines with no edge | judged edges at no oracle site (right/wrong) |
|---|---|---|---|---|
| v2 | 79.6% [78.1, 81.1] (n=2787) | 82.0% [80.4, 83.6] (n=2283) | 0.1572 | 336/565 |
| old engine | 94.3% [93.1, 95.3] (n=1678) | 49.8% [47.8, 51.8] (n=2283) | 0.4735 | no spans |

### CALLS, both engines by line, all targets (in-repo and external)

| engine | precision | recall | external recall | external edges |
|---|---|---|---|---|
| v2 | 83.0% [81.8, 84.2] (n=3498) | 76.0% [74.5, 77.4] (n=3332) | 62.9% [60.0, 65.8] (n=1049) | 1029 |
| old engine | 89.6% [88.1, 91.0] (n=1765) | 34.1% [32.5, 35.8] (n=3332) | 0.0% [0.0, 0.4] (n=1049) | 0 |

### IMPORTS (file pairs)

| engine | scope | precision | recall |
|---|---|---|---|
| v2 | in_repo | 95.6% [90.1, 98.1] (n=114) | 100.0% [96.6, 100.0] (n=109) |
| v2 | external | 97.3% [93.3, 99.0] (n=149) | 90.6% [85.1, 94.2] (n=160) |
| old engine | in_repo | 98.6% [92.3, 99.8] (n=70) | 63.3% [53.9, 71.8] (n=109) |
| old engine | external | 76.4% [69.9, 81.9] (n=191) | 91.2% [85.9, 94.7] (n=160) |

### v2 unresolved, accounting, determinism, cost

- Unresolved CALLS share: 0.2564 (1538 of 5998).
- Top unresolved reasons: no_candidate 729, dynamic_dispatch 675, external_not_indexed 94, reflection 29, many_candidates 9, depth_cap 2.
- Top ledger kinds: fact_unplaced 8379, unhandled_node 4633, fact_unused 2802, unresolved_edge 2561, assert_fatality_unproven 67, layer_abstain 35, unresolved_graphql_registration 15, unknown_route_call 4, framework_unmatched 1, handler_outside_repo 1.
- U12 accounting (emitted = placed + ledgered, lost 0), both builds: pass over 11 kinds, totals {'emitted': 29308, 'ledgered': 11656, 'lost': 0, 'placed': 17652}.
- Old engine U12: not applicable: no raw-fact ledger.
- Determinism: v2 graph hash identical True; old engine export hash identical True.
- v2 build wall [3.05, 2.55] s, peak RSS [214, 213] MiB, store 11929528 bytes.
- Old engine wall [2.03, 1.53] s, peak RSS [92, 92] MiB, export 702020 bytes.
- Disagreement sample: `click-disagreements.md` (30 rows).

## cobra (go) @ `88b30ab89da2`

Oracle scip-go 0.1.24: 4052 call sites. v2 `b3cd5e698314`, old engine `25ae40bf8662`. Scoring: all.

### CALLS, v2 by site (callee span end)

| tier | precision | edges judged of population |
|---|---|---|
| exact | 100.0% [99.8, 100.0] (n=2202) | 2202 of 2202 |
| import | n/a | 0 of 0 |
| name | n/a | 0 of 0 |
| external | 100.0% [99.8, 100.0] (n=1788) | 1788 of 1788 |
| external_module | 100.0% [99.8, 100.0] (n=1788) | 1788 of 1788 |
| overall | 100.0% [99.9, 100.0] (n=3990) | 3990 of 3990 |

| recall | value |
|---|---|
| repo | 99.8% [99.5, 99.9] (n=2206) |
| external | 99.1% [98.6, 99.5] (n=1804) |
| overall | 99.5% [99.2, 99.7] (n=4010) |

| recall by tier (share of all oracle sites a right edge of that tier finds) | value |
|---|---|
| exact | 54.9% [53.4, 56.5] (n=4010) |
| import | 0.0% [0.0, 0.1] (n=4010) |
| name | 0.0% [0.0, 0.1] (n=4010) |
| external | 44.6% [43.1, 46.1] (n=4010) |

Unjudged v2 edges: `{"no_oracle_site": 8, "oracle_target_local_or_unknown": 22}`. Oracle sites whose in-repo target has no v2 node (misses in recall): 0; in-repo recall without them, a diagnostic: 99.8% [99.5, 99.9] (n=2206).

### CALLS, both engines by line, in-repo targets

| engine | precision | recall | oracle targets on lines with no edge | judged edges at no oracle site (right/wrong) |
|---|---|---|---|---|
| v2 | 100.0% [99.8, 100.0] (n=2202) | 99.9% [99.7, 100.0] (n=2192) | 0.0009 | 0/0 |
| old engine | 100.0% [99.7, 100.0] (n=1502) | 68.5% [66.5, 70.4] (n=2192) | 0.2901 | no spans |

### CALLS, both engines by line, all targets (in-repo and external)

| engine | precision | recall | external recall | external edges |
|---|---|---|---|---|
| v2 | 100.0% [99.9, 100.0] (n=3991) | 99.5% [99.3, 99.7] (n=3953) | 99.1% [98.5, 99.4] (n=1761) | 1793 |
| old engine | 100.0% [99.7, 100.0] (n=1502) | 38.0% [36.5, 39.5] (n=3953) | 0.0% [0.0, 0.2] (n=1761) | 0 |

### IMPORTS (file pairs)

| engine | scope | precision | recall |
|---|---|---|---|
| v2 | in_repo | 8.3% [1.5, 35.4] (n=12) | 8.3% [1.5, 35.4] (n=12) |
| v2 | external | 100.0% [97.8, 100.0] (n=174) | 100.0% [97.8, 100.0] (n=174) |
| old engine | in_repo | undefined: no pairs | 0.0% [0.0, 24.2] (n=12) |
| old engine | external | 100.0% [97.8, 100.0] (n=174) | 100.0% [97.8, 100.0] (n=174) |

### v2 unresolved, accounting, determinism, cost

- Unresolved CALLS share: 0.0186 (76 of 4096).
- Top unresolved reasons: dynamic_dispatch 42, no_candidate 31, depth_cap 3.
- Top ledger kinds: fact_unused 393, unresolved_edge 192, assert_fatality_unproven 24, fact_unplaced 14, rules_unsupported_language 1.
- U12 accounting (emitted = placed + ledgered, lost 0), both builds: pass over 8 kinds, totals {'emitted': 9512, 'ledgered': 599, 'lost': 0, 'placed': 8913}.
- Old engine U12: not applicable: no raw-fact ledger.
- Determinism: v2 graph hash identical True; old engine export hash identical True.
- v2 build wall [2.54, 1.54] s, peak RSS [164, 165] MiB, store 30720980 bytes.
- Old engine wall [1.53, 0.51] s, peak RSS [321, 321] MiB, export 375233 bytes.
- Disagreement sample: `cobra-disagreements.md` (20 rows).
