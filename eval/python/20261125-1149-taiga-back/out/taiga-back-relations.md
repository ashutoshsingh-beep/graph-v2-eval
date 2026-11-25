# taiga-back: all relations, graph v2 against dev

| relation | v2 pairs | dev pairs | both | only v2 | only dev | agreement |
|---|---|---|---|---|---|---|
| CALLS | 7438 | 7480 | 4486 | 2952 | 2994 | 43.0% |
| IMPORTS | 2931 | 1962 | 1894 | 1037 | 68 | 63.2% |
| REFERENCES | 2826 | 5711 | 422 | 2404 | 5289 | 5.2% |
| EXTENDS | 1288 | 997 | 938 | 350 | 59 | 69.6% |
| CONTAINS | 20 | 6800 | 20 | 0 | 6780 | 0.3% |
| TESTS | 7929 | 0 | 0 | 7929 | 0 | 0.0% |
| ASSERTS | 1570 | 0 | 0 | 1570 | 0 | 0.0% |
| MOCKS | 56 | 0 | 0 | 56 | 0 | 0.0% |
| HANDLES | 3 | 449 | 0 | 3 | 449 | 0.0% |
| ACCESSES | 1083 | 1069 | 0 | 1083 | 1069 | 0.0% |
| INVOKES | 1 | 16 | 0 | 1 | 16 | 0.0% |
| NAVIGATES | 0 | 0 | 0 | 0 | 0 | - |
| COVERS | 0 | 0 | 0 | 0 | 0 | - |

dev edges not compared (no v2 counterpart, or structure v2 does not keep as edges): {'CONTAINS from or to a folder or file (dev only)': 6812, 'READS_ENV': 58, 'EXPORTS': 14}.
v2 edges not compared (unresolved, external, or structure dev never makes): {'CALLS unresolved': 18968, 'REFERENCES unresolved': 12620, 'CALLS external': 11073, 'CONTAINS to a condition (v2 only)': 3013, 'IMPORTS external': 2534, 'REFERENCES external': 1539, 'CONTAINS from or to a folder or file (dev only)': 1404, 'ACCESSES unresolved': 836, 'EXTENDS external': 496, 'MOCKS unresolved': 146, 'MOCKS external': 31, 'EXTENDS unresolved': 24, 'IMPORTS unresolved': 20, 'INVOKES unresolved': 15, 'HANDLES unresolved': 12}.
Sheets: `<repo>-<relation>-pairs-differences.md` for every relation with edges.
