# taiga-back (python): INVOKES, graph v2 against dev

Engines: v2 `5a6074642e06`, dev `25ae40bf8662`. No oracle: you judge each row.

## Counts

v2 1 pairs, dev 16 pairs (dev types: FETCHES_API 16).
Both 0, only v2 1, only dev 16; agreement 0.0% of the union.
Pairs are matched on (file, name with only letters and digits) of both ends, so the engines' different spellings of one test or scope meet; an edge to a route, data or package node (v2) has no dev counterpart. v2 unresolved and external edges are left out.

Verdict: `confirmed` (the group is right), `v2 wrong`, `dev wrong`, `both wrong`, or `?`. Cause: one short phrase.

## Only v2 has it (1 of 1)
<!-- group: only_v2 -->

v2 has this edge, dev does not. Check: is the edge real in the code (v2 gain) or wrong (v2 wrong)?

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|
| 1 | `taiga/importers/github/importer.py::GithubImporter.get_access_token` | `data::external_service::github.com` | yes | no | taiga/importers/github/importer.py:694 |  |  |

## Only dev has it (16 of 16)
<!-- group: only_dev -->

dev has this edge, v2 does not. Check: is it real (a v2 gap) or wrong (dev wrong)?

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|
| 1 | `taiga/importers/asana/importer.py::AsanaImporter._import_attachments` | `route:GET:/attachment['download_url']` | no | FETCHES_API | - |  |  |
| 2 | `taiga/importers/github/importer.py::GithubImporter._import_project_data` | `route:GET:/repo['organization']['avatar_url']` | no | FETCHES_API | - |  |  |
| 3 | `taiga/importers/github/importer.py::GithubImporter.get_access_token` | `route:POST:/login/oauth/access_token` | no | FETCHES_API | - |  |  |
| 4 | `taiga/importers/jira/common.py::JiraImporterCommon.get_access_token` | `route:POST:/server + '/plugins/servlet/oauth/access-token` | no | FETCHES_API | - |  |  |
| 5 | `taiga/importers/jira/common.py::JiraImporterCommon.get_auth_url` | `route:POST:/server + '/plugins/servlet/oauth/request-token` | no | FETCHES_API | - |  |  |
| 6 | `tests/integration/test_epics.py::test_get_invalid_csv` | `route:GET:/{}` | no | FETCHES_API | - |  |  |
| 7 | `tests/integration/test_epics.py::test_get_valid_csv` | `route:GET:/{}` | no | FETCHES_API | - |  |  |
| 8 | `tests/integration/test_exporter_api.py::test_valid_project_export_with_celery_disabled_and_gzip` | `route:GET:/url + '` | no | FETCHES_API | - |  |  |
| 9 | `tests/integration/test_exporter_api.py::test_valid_project_export_with_celery_enabled_and_gzip` | `route:GET:/url + '` | no | FETCHES_API | - |  |  |
| 10 | `tests/integration/test_issues.py::test_get_invalid_csv` | `route:GET:/{}` | no | FETCHES_API | - |  |  |
| 11 | `tests/integration/test_issues.py::test_get_valid_csv` | `route:GET:/{}` | no | FETCHES_API | - |  |  |
| 12 | `tests/integration/test_tasks.py::test_get_invalid_csv` | `route:GET:/{}` | no | FETCHES_API | - |  |  |
| 13 | `tests/integration/test_tasks.py::test_get_valid_csv` | `route:GET:/{}` | no | FETCHES_API | - |  |  |
| 14 | `tests/integration/test_users.py::test_list_contacts_filter_exclude_project` | `route:GET:/url + '` | no | FETCHES_API | - |  |  |
| 15 | `tests/integration/test_userstories.py::test_get_invalid_csv` | `route:GET:/{}` | no | FETCHES_API | - |  |  |
| 16 | `tests/integration/test_userstories.py::test_get_valid_csv` | `route:GET:/{}` | no | FETCHES_API | - |  |  |

## Both have it (spot check) (0 of 0)
<!-- group: both -->

Both engines agree. Check a few: an agreement can still be wrong.

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|

