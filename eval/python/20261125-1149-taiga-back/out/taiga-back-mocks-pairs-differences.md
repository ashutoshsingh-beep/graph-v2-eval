# taiga-back (python): MOCKS, graph v2 against dev

Engines: v2 `8e6c33b35a2d`, dev `43d92add3d58`. No oracle: you judge each row.

## Counts

v2 56 pairs, dev 0 pairs (dev types: none).
Both 0, only v2 56, only dev 0; agreement 0.0% of the union.
Pairs are matched on (file, name with only letters and digits) of both ends, so the engines' different spellings of one test or scope meet; an edge to a route, data or package node (v2) has no dev counterpart. v2 unresolved and external edges are left out.

Verdict: `confirmed` (the group is right), `v2 wrong`, `dev wrong`, `both wrong`, or `?`. Cause: one short phrase.

## Only v2 has it (25 of 56)
<!-- group: only_v2 -->

v2 has this edge, dev does not. Check: is the edge real in the code (v2 gain) or wrong (v2 wrong)?

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|
| 1 | `tests/integration/resources_permissions/test_webhooks_resources.py::test_webhook_action_test` | `taiga/webhooks/tasks.py::_send_request` | yes | no | tests/integration/resources_permissions/test_webhooks_resources.py:232 |  |  |
| 2 | `tests/integration/test_importers_asana_api.py::test_import_asana_list_projects_with_problem_on_request` | `taiga/importers/asana/importer.py::AsanaClient` | yes | no | tests/integration/test_importers_asana_api.py:178 |  |  |
| 3 | `tests/integration/test_importers_github_api.py::test_import_github_list_users_with_problem_on_request` | `taiga/importers/github/importer.py::GithubClient` | yes | no | tests/integration/test_importers_github_api.py:134 |  |  |
| 4 | `tests/integration/test_importers_jira_api.py::test_import_jira_list_projects_with_problem_on_request` | `taiga/importers/jira/common.py::JiraClient` | yes | no | tests/integration/test_importers_jira_api.py:174 |  |  |
| 5 | `tests/integration/test_importers_trello_api.py::test_import_trello_list_projects_with_problem_on_request` | `taiga/importers/trello/importer.py::TrelloClient` | yes | no | tests/integration/test_importers_trello_api.py:177 |  |  |
| 6 | `tests/integration/test_importers_trello_api.py::test_import_trello_transform_action_data_wrong_id_old` | `taiga/importers/trello/importer.py::TrelloClient` | yes | no | tests/integration/test_importers_trello_api.py:214 |  |  |
| 7 | `tests/integration/test_userstories_update_kanban_order.py::test_userstories_are_closed_after_moving_in_bulk_to_a_closed_status` | `taiga/webhooks/tasks.py::_send_request` | yes | no | tests/integration/test_userstories_update_kanban_order.py:934 |  |  |
| 8 | `tests/integration/test_userstories_update_kanban_order.py::test_userstories_are_opened_after_moving_in_bulk_to_a_opened_status` | `taiga/webhooks/tasks.py::_send_request` | yes | no | tests/integration/test_userstories_update_kanban_order.py:983 |  |  |
| 9 | `tests/integration/test_webhooks_epics.py::test_webhooks_when_create_epic` | `taiga/webhooks/tasks.py::_send_request` | yes | no | tests/integration/test_webhooks_epics.py:27 |  |  |
| 10 | `tests/integration/test_webhooks_epics.py::test_webhooks_when_delete_epic` | `taiga/webhooks/tasks.py::_send_request` | yes | no | tests/integration/test_webhooks_epics.py:78 |  |  |
| 11 | `tests/integration/test_webhooks_epics.py::test_webhooks_when_delete_epic_related_userstory` | `taiga/webhooks/tasks.py::_send_request` | yes | no | tests/integration/test_webhooks_epics.py:298 |  |  |
| 12 | `tests/integration/test_webhooks_epics.py::test_webhooks_when_update_epic_attachments` | `taiga/webhooks/tasks.py::_send_request` | yes | no | tests/integration/test_webhooks_epics.py:98 |  |  |
| 13 | `tests/integration/test_webhooks_issues.py::test_webhooks_when_delete_issue` | `taiga/webhooks/tasks.py::_send_request` | yes | no | tests/integration/test_webhooks_issues.py:78 |  |  |
| 14 | `tests/integration/test_webhooks_issues.py::test_webhooks_when_update_issue_attachments` | `taiga/webhooks/tasks.py::_send_request` | yes | no | tests/integration/test_webhooks_issues.py:98 |  |  |
| 15 | `tests/integration/test_webhooks_milestones.py::test_webhooks_when_update_milestone` | `taiga/webhooks/tasks.py::_send_request` | yes | no | tests/integration/test_webhooks_milestones.py:50 |  |  |
| 16 | `tests/integration/test_webhooks_signals.py::test_new_object_with_one_webhook_signal` | `taiga/base/utils/urls.py::validate_private_url` | yes | no | tests/integration/test_webhooks_signals.py:36 |  |  |
| 17 | `tests/integration/test_webhooks_tasks.py::test_webhooks_when_create_task` | `taiga/webhooks/tasks.py::_send_request` | yes | no | tests/integration/test_webhooks_tasks.py:30 |  |  |
| 18 | `tests/integration/test_webhooks_tasks.py::test_webhooks_when_update_task` | `taiga/webhooks/tasks.py::_send_request` | yes | no | tests/integration/test_webhooks_tasks.py:50 |  |  |
| 19 | `tests/integration/test_webhooks_tasks.py::test_webhooks_when_update_task_custom_attributes` | `taiga/webhooks/tasks.py::_send_request` | yes | no | tests/integration/test_webhooks_tasks.py:175 |  |  |
| 20 | `tests/integration/test_webhooks_userstories.py::test_webhooks_when_create_user_story` | `taiga/webhooks/tasks.py::_send_request` | yes | no | tests/integration/test_webhooks_userstories.py:30 |  |  |
| 21 | `tests/integration/test_webhooks_userstories.py::test_webhooks_when_delete_user_story` | `taiga/webhooks/tasks.py::_send_request` | yes | no | tests/integration/test_webhooks_userstories.py:113 |  |  |
| 22 | `tests/integration/test_webhooks_userstories.py::test_webhooks_when_update_assigned_users_user_story` | `taiga/webhooks/tasks.py::_send_request` | yes | no | tests/integration/test_webhooks_userstories.py:81 |  |  |
| 23 | `tests/integration/test_webhooks_userstories.py::test_webhooks_when_update_user_story_points` | `taiga/webhooks/tasks.py::_send_request` | yes | no | tests/integration/test_webhooks_userstories.py:288 |  |  |
| 24 | `tests/integration/test_webhooks_wikipages.py::test_webhooks_when_update_wiki_page_attachments` | `taiga/webhooks/tasks.py::_send_request` | yes | no | tests/integration/test_webhooks_wikipages.py:101 |  |  |
| 25 | `tests/unit/test_timeline.py::test_push_to_timeline_many_objects` | `taiga/timeline/service.py::_add_to_object_timeline` | yes | no | tests/unit/test_timeline.py:21 |  |  |

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

