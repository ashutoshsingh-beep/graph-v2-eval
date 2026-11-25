# taiga-back (python): TESTS, graph v2 against dev

Engines: v2 `4e50b002a213`, dev `25ae40bf8662`. No oracle: you judge each row.

## Counts

v2 7929 pairs, dev 0 pairs (dev types: none).
Both 0, only v2 7929, only dev 0; agreement 0.0% of the union.
Pairs are matched on (file, name with only letters and digits) of both ends, so the engines' different spellings of one test or scope meet; an edge to a route, data or package node (v2) has no dev counterpart. v2 unresolved and external edges are left out.

Verdict: `confirmed` (the group is right), `v2 wrong`, `dev wrong`, `both wrong`, or `?`. Cause: one short phrase.

## Only v2 has it (25 of 7929)
<!-- group: only_v2 -->

v2 has this edge, dev does not. Check: is the edge real in the code (v2 gain) or wrong (v2 wrong)?

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|
| 1 | `tests/integration/resources_permissions/test_attachment_resources.py::test_task_attachment_update` | `tests/utils.py::reconnect_signals` | yes | no | tests/integration/resources_permissions/test_attachment_resources.py:33 |  |  |
| 2 | `tests/integration/resources_permissions/test_epics_related_userstories_resources.py::test_epic_related_userstories_delete` | `taiga/projects/notifications/utils.py::attach_watchers_to_queryset` | yes | no | tests/integration/resources_permissions/test_epics_related_userstories_resources.py:130 |  |  |
| 3 | `tests/integration/resources_permissions/test_epics_resources.py::test_epic_watchers_list` | `tests/factories.py::RelatedUserStory` | yes | no | tests/integration/resources_permissions/test_epics_resources.py:150 |  |  |
| 4 | `tests/integration/resources_permissions/test_issues_resources.py::test_issue_voters_retrieve` | `taiga/projects/attachments/utils.py::attach_basic_attachments` | yes | no | tests/integration/resources_permissions/test_issues_resources.py:131 |  |  |
| 5 | `tests/integration/resources_permissions/test_milestones_resources.py::test_milestone_list` | `taiga/base/utils/json.py::loads` | yes | no | tests/integration/resources_permissions/test_milestones_resources.py:221 |  |  |
| 6 | `tests/integration/resources_permissions/test_projects_choices_resources.py::test_issue_status_patch` | `tests/factories.py::EpicStatusFactory` | yes | no | tests/integration/resources_permissions/test_projects_choices_resources.py:106 |  |  |
| 7 | `tests/integration/resources_permissions/test_projects_choices_resources.py::test_membership_list` | `tests/factories.py::TaskStatusFactory` | yes | no | tests/integration/resources_permissions/test_projects_choices_resources.py:143 |  |  |
| 8 | `tests/integration/resources_permissions/test_projects_choices_resources.py::test_points_list` | `tests/factories.py::MembershipFactory` | yes | no | tests/integration/resources_permissions/test_projects_choices_resources.py:55 |  |  |
| 9 | `tests/integration/resources_permissions/test_projects_choices_resources.py::test_priority_update` | `tests/factories.py::EpicStatusFactory` | yes | no | tests/integration/resources_permissions/test_projects_choices_resources.py:106 |  |  |
| 10 | `tests/integration/resources_permissions/test_projects_choices_resources.py::test_severity_action_bulk_update_order` | `tests/factories.py::PointsFactory` | yes | no | tests/integration/resources_permissions/test_projects_choices_resources.py:115 |  |  |
| 11 | `tests/integration/resources_permissions/test_projects_choices_resources.py::test_swimlane_user_story_status_patch` | `tests/factories.py::IssueStatusFactory` | yes | no | tests/integration/resources_permissions/test_projects_choices_resources.py:152 |  |  |
| 12 | `tests/integration/resources_permissions/test_projects_resource.py::test_delete_tasks_csv_uuid` | `tests/factories.py::RoleFactory` | yes | no | tests/integration/resources_permissions/test_projects_resource.py:59 |  |  |
| 13 | `tests/integration/resources_permissions/test_tasks_resources.py::test_task_put_update_with_project_change` | `taiga/projects/notifications/utils.py::attach_total_watchers_to_queryset` | yes | no | tests/integration/resources_permissions/test_tasks_resources.py:437 |  |  |
| 14 | `tests/integration/test_hooks_bitbucket.py::test_push_event_task_mention` | `tests/factories.py::MembershipFactory` | yes | no | tests/integration/test_hooks_bitbucket.py:396 |  |  |
| 15 | `tests/integration/test_importer_api.py::test_invalid_us_import` | `tests/factories.py::MembershipFactory` | yes | no | tests/integration/test_importer_api.py:432 |  |  |
| 16 | `tests/integration/test_memberships.py::test_create_members_in_bulk` | `taiga/projects/models.py::Membership` | yes | no | tests/integration/test_memberships.py:125 |  |  |
| 17 | `tests/integration/test_occ.py::test_valid_concurrent_save_for_us_different_fields` | `taiga/base/utils/json.py::dumps` | yes | no | tests/integration/test_occ.py:237 |  |  |
| 18 | `tests/integration/test_projects.py::test_private_project_can_be_public_because_project_has_unlimited_members` | `tests/factories.py::create_project` | yes | no | tests/integration/test_projects.py:1573 |  |  |
| 19 | `tests/integration/test_projects.py::test_project_transfer_reject_from_member_with_other_user_token` | `tests/factories.py::create_project` | yes | no | tests/integration/test_projects.py:970 |  |  |
| 20 | `tests/integration/test_timeline.py::test_create_issue_timeline` | `taiga/mdrender/service.py::render` | yes | no | tests/integration/test_timeline.py:188 |  |  |
| 21 | `tests/integration/test_users.py::test_get_voted_list_permissions` | `tests/factories.py::MembershipFactory` | yes | no | tests/integration/test_users.py:1367 |  |  |
| 22 | `tests/integration/test_userstories_update_backlog_order.py::test_api_update_orders_in_bulk_invalid_after_us_because_milestone.ff92409d~1` | `taiga/base/utils/json.py::dumps` | yes | no | tests/integration/test_userstories_update_backlog_order.py:661 |  |  |
| 23 | `tests/integration/test_userstories_update_kanban_order.py::test_api_update_orders_in_bulk_invalid_swimlane` | `tests/factories.py::create_userstory` | yes | no | tests/integration/test_userstories_update_kanban_order.py:588 |  |  |
| 24 | `tests/integration/test_webhooks_issues.py::test_webhooks_when_update_issue_custom_attributes` | `taiga/mdrender/service.py::render` | yes | no | tests/integration/test_webhooks_issues.py:173 |  |  |
| 25 | `tests/unit/test_import.py::test_import_epic_with_user_stories` | `taiga/base/utils/json.py::loads` | yes | no | tests/unit/test_import.py:34 |  |  |

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

