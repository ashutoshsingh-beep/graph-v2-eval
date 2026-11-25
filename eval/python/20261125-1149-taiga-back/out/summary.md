# SCIP accuracy evaluation

Method: `docs/graph-v2/accuracy-method.md`. Intervals are 95% Wilson. Precision first.

## taiga-back (python) @ `8ab6a4e3b5f6`

Oracle scip-python 0.6.6: 22014 call sites. v2 `8e6c33b35a2d`, old engine `43d92add3d58`. Scoring: all.

### CALLS, v2 by site (callee span end)

| tier | precision | edges judged of population |
|---|---|---|
| exact | 100.0% [87.1, 100.0] (n=26) | 26 of 26 |
| import | 99.0% [98.8, 99.2] (n=10108) | 10108 of 10108 |
| name | 99.5% [99.0, 99.8] (n=1434) | 1434 of 1434 |
| external | 99.6% [99.2, 99.7] (n=3134) | 3134 of 3134 |
| external_module | 94.3% [93.5, 95.1] (n=3134) | 3134 of 3134 |
| overall | 99.2% [99.0, 99.3] (n=14702) | 14702 of 14702 |

| recall | value |
|---|---|
| repo | 91.0% [90.5, 91.5] (n=12595) |
| external | 71.8% [70.4, 73.1] (n=4347) |
| overall | 86.1% [85.5, 86.6] (n=16942) |

| recall by tier (share of all oracle sites a right edge of that tier finds) | value |
|---|---|
| exact | 0.1% [0.1, 0.2] (n=16942) |
| import | 59.1% [58.3, 59.8] (n=16942) |
| name | 8.4% [8.0, 8.8] (n=16942) |
| external | 18.4% [17.8, 19.0] (n=16942) |

Unjudged v2 edges: `{"no_oracle_site": 4856, "oracle_target_local_or_unknown": 4007}`. Oracle sites whose in-repo target has no v2 node (misses in recall): 2; in-repo recall without them, a diagnostic: 91.0% [90.5, 91.5] (n=12593).

### CALLS, both engines by line, in-repo targets

| engine | precision | recall | oracle targets on lines with no edge | judged edges at no oracle site (right/wrong) |
|---|---|---|---|---|
| v2 | 94.2% [93.8, 94.6] (n=12343) | 91.0% [90.5, 91.5] (n=12573) | 0.0684 | 168/614 |
| old engine | 92.9% [92.2, 93.6] (n=5485) | 38.9% [38.1, 39.8] (n=12573) | 0.6031 | no spans |

### CALLS, both engines by line, all targets (in-repo and external)

| engine | precision | recall | external recall | external edges |
|---|---|---|---|---|
| v2 | 92.2% [91.7, 92.6] (n=16065) | 86.4% [85.9, 86.9] (n=16241) | 70.6% [69.1, 72.1] (n=3668) | 11073 |
| old engine | 88.5% [87.7, 89.3] (n=5756) | 30.1% [29.4, 30.9] (n=16241) | 0.0% [0.0, 0.1] (n=3668) | 0 |

### IMPORTS (file pairs)

| engine | scope | precision | recall |
|---|---|---|---|
| v2 | in_repo | 77.4% [75.6, 79.1] (n=2213) | 99.5% [99.1, 99.8] (n=1720) |
| v2 | external | 40.3% [37.9, 42.8] (n=1523) | 71.9% [68.8, 74.8] (n=854) |
| old engine | in_repo | 97.0% [95.9, 97.8] (n=1311) | 73.9% [71.8, 75.9] (n=1720) |
| old engine | external | 40.2% [37.8, 42.7] (n=1534) | 72.2% [69.2, 75.1] (n=854) |

### REFERENCES, v2 by site (name used, not called; 109054 oracle sites)

| scope | precision | recall |
|---|---|---|
| repo | 99.0% [98.2, 99.5] (n=1000) | 28.9% [26.2, 31.8] (n=1000) |
| external | 98.0% [95.7, 99.1] (n=302) | 24.6% [22.0, 27.4] (n=1000) |
| overall | 98.8% [97.9, 99.3] (n=1000) | 25.2% [22.6, 28.0] (n=1000) |

| precision by access (information only) | value |
|---|---|
| read | 99.2% [98.4, 99.6] (n=1000) |
| type | 100.0% [87.5, 100.0] (n=27) |
| write | 99.3% [96.4, 99.9] (n=152) |

Unjudged v2 edges: `{"fixture_or_data_rule": 506, "no_oracle_site": 1061, "oracle_target_local_or_unknown": 534, "unresolved": 12620}`. Oracle sites whose in-repo target has no v2 node: 1040; found only as a CALLS edge: 5.

Old engine REFERENCES by line (READS / WRITES of module-level variables only, 811 edges): in-repo precision 91.3% [89.0, 93.2] (n=669), recall 7.3% [5.9, 9.1] (n=1000).

### v2 unresolved, accounting, determinism, cost

- Unresolved CALLS share: 0.446 (18968 of 42533).
- Top unresolved reasons: dynamic_dispatch 11111, no_candidate 7443, reflection 373, many_candidates 26, external_not_indexed 9, depth_cap 6.
- Top ledger kinds: fact_unplaced 103763, unresolved_edge 32629, fact_unused 32435, unhandled_node 30160, layer_abstain 3059, unresolved_graphql_registration 42, assert_fatality_unproven 32, prefix_not_read 30, unknown_test_marker 24, handler_outside_repo 16.
- U12 accounting (emitted = placed + ledgered, lost 0), both builds: pass over 12 kinds, totals {'emitted': 247091, 'ledgered': 129681, 'lost': 0, 'placed': 117410}.
- Old engine U12: not applicable: no raw-fact ledger.
- Determinism: v2 graph hash identical True; old engine export hash identical True.
- v2 build wall [30.74, 31.73] s, peak RSS [1194, 1114] MiB, store 104918033 bytes.
- Old engine wall [6.56, 6.05] s, peak RSS [304, 302] MiB, export 11713167 bytes.
- Disagreement sample: `taiga-back-disagreements.md` (30 rows).
