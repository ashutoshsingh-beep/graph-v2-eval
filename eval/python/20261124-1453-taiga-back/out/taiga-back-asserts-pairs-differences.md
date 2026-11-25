# taiga-back (python): ASSERTS, graph v2 against dev

Engines: v2 `5a6074642e06`, dev `25ae40bf8662`. No oracle: you judge each row.

## Counts

v2 1570 pairs, dev 0 pairs (dev types: none).
Both 0, only v2 1570, only dev 0; agreement 0.0% of the union.
Pairs are matched on (file, name with only letters and digits) of both ends, so the engines' different spellings of one test or scope meet; an edge to a route, data or package node (v2) has no dev counterpart. v2 unresolved and external edges are left out.

Verdict: `confirmed` (the group is right), `v2 wrong`, `dev wrong`, `both wrong`, or `?`. Cause: one short phrase.

## Only v2 has it (25 of 1570)
<!-- group: only_v2 -->

v2 has this edge, dev does not. Check: is the edge real in the code (v2 gain) or wrong (v2 wrong)?

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|
| 1 | `tests/integration/resources_permissions/test_epics_resources.py::test_epic_action_bulk_create` | `tests/utils.py::helper_test_http_method` | yes | no | tests/integration/resources_permissions/test_epics_resources.py:642 |  |  |
| 2 | `tests/integration/resources_permissions/test_projects_choices_resources.py::test_mix_tags` | `tests/utils.py::helper_test_http_method` | yes | no | tests/integration/resources_permissions/test_projects_choices_resources.py:2689 |  |  |
| 3 | `tests/integration/resources_permissions/test_projects_choices_resources.py::test_severity_update` | `tests/utils.py::helper_test_http_method` | yes | no | tests/integration/resources_permissions/test_projects_choices_resources.py:2066 |  |  |
| 4 | `tests/integration/test_epics_tags.py::test_api_epic_add_new_tags_without_colors` | `taiga/base/utils/json.py::dumps` | yes | no | tests/integration/test_epics_tags.py:72 |  |  |
| 5 | `tests/integration/test_history.py::test_take_snapshot_crete` | `taiga/projects/history/services.py::take_snapshot` | yes | no | tests/integration/test_history.py:37 |  |  |
| 6 | `tests/integration/test_history.py::test_take_two_snapshots_without_changes` | `taiga/projects/history/services.py::take_snapshot` | yes | no | tests/integration/test_history.py:75 |  |  |
| 7 | `tests/integration/test_hooks_github.py::test_blocked_project` | `taiga/base/utils/json.py::dumps` | yes | no | tests/integration/test_hooks_github.py:93 |  |  |
| 8 | `tests/integration/test_importer_api.py::test_invalid_us_import_with_bad_choices` | `taiga/base/utils/json.py::dumps` | yes | no | tests/integration/test_importer_api.py:529 |  |  |
| 9 | `tests/integration/test_issues.py::test_api_create_in_bulk_with_status_milestone` | `taiga/base/utils/json.py::dumps` | yes | no | tests/integration/test_issues.py:818 |  |  |
| 10 | `tests/integration/test_issues.py::test_api_filter_by_subject` | `tests/factories.py::create_issue` | yes | no | tests/integration/test_issues.py:197 |  |  |
| 11 | `tests/integration/test_issues.py::test_mulitple_exclude_filter_tags` | `tests/integration/test_issues.py::create_filter_issues_context` | yes | no | tests/integration/test_issues.py:477 |  |  |
| 12 | `tests/integration/test_issues_tags.py::test_api_issue_add_new_tags_without_colors` | `taiga/base/utils/json.py::dumps` | yes | no | tests/integration/test_issues_tags.py:72 |  |  |
| 13 | `tests/integration/test_memberships.py::test_api_create_bulk_members_without_enough_memberships_private_project_slots_multiple_projects` | `taiga/base/utils/json.py::dumps` | yes | no | tests/integration/test_memberships.py:355 |  |  |
| 14 | `tests/integration/test_memberships.py::test_api_create_invalid_membership_role_doesnt_exist_in_the_project` | `taiga/base/utils/json.py::dumps` | yes | no | tests/integration/test_memberships.py:664 |  |  |
| 15 | `tests/integration/test_projects.py::test_duplicate_project` | `taiga/timeline/service.py::get_project_timeline` | yes | no | tests/integration/test_projects.py:2257 |  |  |
| 16 | `tests/integration/test_projects.py::test_edit_tag_only_color` | `taiga/base/utils/json.py::dumps` | yes | no | tests/integration/test_projects.py:2009 |  |  |
| 17 | `tests/integration/test_projects.py::test_partially_update_project` | `taiga/base/utils/json.py::dumps` | yes | no | tests/integration/test_projects.py:261 |  |  |
| 18 | `tests/integration/test_projects.py::test_project_list_with_search_query_order_by_ranking` | `tests/factories.py::create_project` | yes | no | tests/integration/test_projects.py:783 |  |  |
| 19 | `tests/integration/test_projects.py::test_transfer_request_from_not_anonimous` | `tests/factories.py::create_project` | yes | no | tests/integration/test_projects.py:804 |  |  |
| 20 | `tests/integration/test_timeline.py::test_delete_project_timeline` | `taiga/timeline/service.py::get_profile_timeline` | yes | no | tests/integration/test_timeline.py:354 |  |  |
| 21 | `tests/integration/test_userstories_update_backlog_order.py::test_api_update_orders_in_bulk_invalid_after_us_because_no_milestone.ff92409d~1` | `taiga/base/utils/json.py::dumps` | yes | no | tests/integration/test_userstories_update_backlog_order.py:690 |  |  |
| 22 | `tests/integration/test_vote_tasks.py::test_get_task_is_voted` | `tests/factories.py::create_task` | yes | no | tests/integration/test_vote_tasks.py:95 |  |  |
| 23 | `tests/unit/test_common_throttle.py::test_user_multi_read_first_small_throttling` | `taiga/base/throttling.py::CommonThrottle.allow_request` | yes | no | tests/unit/test_common_throttle.py:89 |  |  |
| 24 | `tests/unit/test_mdrender.py::test_render_url_autolinks_with_https` | `taiga/mdrender/service.py::render` | yes | no | tests/unit/test_mdrender.py:217 |  |  |
| 25 | `tests/unit/test_mdrender.py::test_render_url_autolinks_without_http` | `taiga/mdrender/service.py::render` | yes | no | tests/unit/test_mdrender.py:205 |  |  |

## Only dev has it (0 of 0)
<!-- group: only_dev -->

dev has this edge, v2 does not. Check: is it real (a v2 gap) or wrong (dev wrong)?

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|

## Both have it (spot check) (0 of 0)
<!-- group: both -->

Both engines agree. Check a few: an agreement can still be wrong.

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|

