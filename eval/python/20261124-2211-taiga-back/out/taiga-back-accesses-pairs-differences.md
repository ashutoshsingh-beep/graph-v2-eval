# taiga-back (python): ACCESSES, graph v2 against dev

Engines: v2 `8e6c33b35a2d`, dev `43d92add3d58`. No oracle: you judge each row.

## Counts

v2 1083 pairs, dev 1069 pairs (dev types: ACCESSES_MODEL 1069).
Both 0, only v2 1083, only dev 1069; agreement 0.0% of the union.
Pairs are matched on (file, name with only letters and digits) of both ends, so the engines' different spellings of one test or scope meet; an edge to a route, data or package node (v2) has no dev counterpart. v2 unresolved and external edges are left out.

Verdict: `confirmed` (the group is right), `v2 wrong`, `dev wrong`, `both wrong`, or `?`. Cause: one short phrase.

## Only v2 has it (25 of 1083)
<!-- group: only_v2 -->

v2 has this edge, dev does not. Check: is the edge real in the code (v2 gain) or wrong (v2 wrong)?

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|
| 1 | `docker/config.py` | `data::env_var::TAIGA_SITES_SCHEME` | yes | no | docker/config.py:32 |  |  |
| 2 | `taiga/base/api/fields.py::DateTimeField.from_native` | `data::config_key::USE_TZ` | yes | no | taiga/base/api/fields.py:761 |  |  |
| 3 | `taiga/base/api/request.py::Request.__init__` | `data::config_key::DEFAULT_CHARSET` | yes | no | taiga/base/api/request.py:170 |  |  |
| 4 | `taiga/base/management/commands/test_emails.py::Command.handle` | `data::model::taiga.projects.models.Membership` | yes | no | taiga/base/management/commands/test_emails.py:51 |  |  |
| 5 | `taiga/importers/jira/normal.py::JiraNormalImporter._import_subtasks` | `data::model::taiga.projects.tasks.models.Task` | yes | no | taiga/importers/jira/normal.py:273 |  |  |
| 6 | `taiga/importers/management/commands/import_from_pivotal.py::Command.handle` | `data::model::taiga.users.models.User` | yes | no | taiga/importers/management/commands/import_from_pivotal.py:34 |  |  |
| 7 | `taiga/projects/custom_attributes/migrations/0013_auto_20181022_1624.py::Migration` | `data::model::taiga.projects.custom_attributes.models.EpicCustomAttribute` | yes | no | taiga/projects/custom_attributes/migrations/0013_auto_20181022_1624.py:23 |  |  |
| 8 | `taiga/projects/epics/models.py::Epic.save` | `data::model::taiga.projects.epics.models.Epic` | yes | no | taiga/projects/epics/models.py:97 |  |  |
| 9 | `taiga/projects/history/migrations/0012_auto_20160629_1036.py::Migration` | `data::model::taiga.projects.history.models.HistoryEntry` | yes | no | taiga/projects/history/migrations/0012_auto_20160629_1036.py:21 |  |  |
| 10 | `taiga/projects/migrations/0060_auto_20180614_1338.py::Migration` | `data::model::taiga.projects.models.UserStoryDueDate` | yes | no | taiga/projects/migrations/0060_auto_20180614_1338.py:58 |  |  |
| 11 | `taiga/projects/milestones/migrations/0001_initial.py::Migration` | `data::config_key::AUTH_USER_MODEL` | yes | no | taiga/projects/milestones/migrations/0001_initial.py:19 |  |  |
| 12 | `taiga/projects/models.py::ProjectTemplate.apply_to_project` | `data::model::taiga.projects.models.Points` | yes | no | taiga/projects/models.py:1299 |  |  |
| 13 | `taiga/projects/tasks/models.py::Task` | `data::config_key::AUTH_USER_MODEL` | yes | no | taiga/projects/tasks/models.py:35 |  |  |
| 14 | `taiga/projects/userstories/migrations/0014_auto_20160928_0540.py::Migration` | `data::model::taiga.projects.userstories.models.UserStory` | yes | no | taiga/projects/userstories/migrations/0014_auto_20160928_0540.py:22 |  |  |
| 15 | `taiga/projects/userstories/models.py::UserStory.save` | `data::model::taiga.projects.userstories.models.RolePoints` | yes | no | taiga/projects/userstories/models.py:165 |  |  |
| 16 | `taiga/users/services.py::get_big_photo_url` | `data::config_key::THN_AVATAR_BIG` | yes | no | taiga/users/services.py:91 |  |  |
| 17 | `taiga/webhooks/validators.py::WebhookValidator.validate_url` | `data::config_key::WEBHOOKS_ALLOW_PRIVATE_ADDRESS` | yes | no | taiga/webhooks/validators.py:25 |  |  |
| 18 | `tests/integration/resources_permissions/test_projects_resource.py::data` | `data::model::taiga.projects.models.Project` | yes | no | tests/integration/resources_permissions/test_projects_resource.py:38 |  |  |
| 19 | `tests/integration/test_hooks_github.py::test_push_event_user_story_processing` | `data::model::taiga.projects.userstories.models.UserStory` | yes | no | tests/integration/test_hooks_github.py:192 |  |  |
| 20 | `tests/integration/test_hooks_gitlab.py::test_issues_event_closed_issue_conected_with_external_one_with_close_status_defined` | `data::model::taiga.projects.models.Membership` | yes | no | tests/integration/test_hooks_gitlab.py:1175 |  |  |
| 21 | `tests/integration/test_importer_api.py::test_valid_dump_import_error_without_enough_membership_private_project_slots_one_project` | `data::model::taiga.projects.models.Project` | yes | no | tests/integration/test_importer_api.py:1311 |  |  |
| 22 | `tests/integration/test_neighbors.py::TestIssues.test_ordering_by_assigned_to_desc_with_none_and_normal_values` | `data::model::taiga.projects.issues.models.Issue` | yes | no | tests/integration/test_neighbors.py:335 |  |  |
| 23 | `tests/integration/test_notifications.py::test_send_notifications_using_services_method_for_user_stories` | `data::model::taiga.projects.notifications.models.HistoryChangeNotification` | yes | no | tests/integration/test_notifications.py:404 |  |  |
| 24 | `tests/integration/test_projects.py::test_edit_tag_only_name` | `data::model::taiga.projects.tasks.models.Task` | yes | no | tests/integration/test_projects.py:1982 |  |  |
| 25 | `tests/integration/test_us_autoclosing.py::test_auto_open_us_when_add_open_task` | `data::model::taiga.projects.userstories.models.UserStory` | yes | no | tests/integration/test_us_autoclosing.py:236 |  |  |

## Only dev has it (25 of 1069)
<!-- group: only_dev -->

dev has this edge, v2 does not. Check: is it real (a v2 gap) or wrong (dev wrong)?

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|
| 1 | `taiga/export_import/management/commands/dump_project.py::Command.handle` | `taiga/projects/models.py::Project` | no | ACCESSES_MODEL | - |  |  |
| 2 | `taiga/hooks/github/migrations/0001_initial.py::create_github_system_user` | `taiga/users/models.py::User` | no | ACCESSES_MODEL | - |  |  |
| 3 | `taiga/importers/github/tasks.py::import_project` | `taiga/users/models.py::User` | no | ACCESSES_MODEL | - |  |  |
| 4 | `taiga/importers/jira/common.py::JiraImporterCommon._cleanup` | `taiga/projects/models.py::Project` | no | ACCESSES_MODEL | - |  |  |
| 5 | `taiga/projects/milestones/services.py::update_userstories_milestone_in_bulk` | `taiga/projects/milestones/models.py::Milestone` | no | ACCESSES_MODEL | - |  |  |
| 6 | `taiga/projects/milestones/utils.py::attach_extra_info` | `taiga/projects/userstories/models.py::UserStory` | no | ACCESSES_MODEL | - |  |  |
| 7 | `taiga/projects/notifications/services.py::get_projects_watched` | `taiga/users/models.py::User` | no | ACCESSES_MODEL | - |  |  |
| 8 | `taiga/projects/tasks/migrations/0008_remove_task_watchers.py::create_notifications` | `taiga/projects/notifications/models.py::Watched` | no | ACCESSES_MODEL | - |  |  |
| 9 | `taiga/projects/userstories/utils.py::attach_total_points` | `taiga/projects/models.py::Points` | no | ACCESSES_MODEL | - |  |  |
| 10 | `taiga/projects/utils.py::attach_milestones` | `taiga/projects/milestones/models.py::Milestone` | no | ACCESSES_MODEL | - |  |  |
| 11 | `taiga/users/services.py::_build_watched_sql_for_projects` | `taiga/projects/notifications/models.py::NotifyPolicy` | no | ACCESSES_MODEL | - |  |  |
| 12 | `tests/integration/resources_permissions/test_epics_resources.py::test_epic_put_update_with_project_change` | `taiga/projects/epics/models.py::Epic` | no | ACCESSES_MODEL | - |  |  |
| 13 | `tests/integration/resources_permissions/test_issues_resources.py::test_issue_put_update_with_project_change` | `taiga/projects/models.py::Project` | no | ACCESSES_MODEL | - |  |  |
| 14 | `tests/integration/resources_permissions/test_tasks_resources.py::data` | `taiga/projects/tasks/models.py::Task` | no | ACCESSES_MODEL | - |  |  |
| 15 | `tests/integration/test_custom_attributes_epics.py::test_epic_custom_attributes_values_update` | `taiga/projects/epics/models.py::Epic` | no | ACCESSES_MODEL | - |  |  |
| 16 | `tests/integration/test_hooks_github.py::test_issues_event_opened_issue` | `taiga/projects/models.py::Membership` | no | ACCESSES_MODEL | - |  |  |
| 17 | `tests/integration/test_hooks_gitlab.py::test_push_event_issue_processing` | `taiga/projects/issues/models.py::Issue` | no | ACCESSES_MODEL | - |  |  |
| 18 | `tests/integration/test_importer_api.py::test_valid_dump_import_with_the_limit_of_membership_whit_you_for_private_project` | `taiga/projects/models.py::Project` | no | ACCESSES_MODEL | - |  |  |
| 19 | `tests/integration/test_issues.py::test_promote_issue_to_us` | `taiga/projects/userstories/models.py::UserStory` | no | ACCESSES_MODEL | - |  |  |
| 20 | `tests/integration/test_milestones.py::test_api_move_tasks_to_another_sprint` | `taiga/projects/models.py::Project` | no | ACCESSES_MODEL | - |  |  |
| 21 | `tests/integration/test_notifications.py::test_watching_users_to_notify_on_issue_modification_3` | `taiga/projects/issues/models.py::Issue` | no | ACCESSES_MODEL | - |  |  |
| 22 | `tests/integration/test_projects.py::test_project_transfer_accept_from_admin_member_with_valid_token_with_enough_slots` | `taiga/projects/models.py::Project` | no | ACCESSES_MODEL | - |  |  |
| 23 | `tests/integration/test_users.py::test_validate_requested_email_change_invalidates_password_recovery_token` | `taiga/users/models.py::User` | no | ACCESSES_MODEL | - |  |  |
| 24 | `tests/integration/test_userstories_update_backlog_order.py::test_api_update_orders_in_bulk_succeeds_moved_to_a_milestone_to_the_middle` | `taiga/projects/models.py::Project` | no | ACCESSES_MODEL | - |  |  |
| 25 | `tests/integration/test_userstories_update_kanban_order.py::test_api_update_orders_in_bulk_succeeds_moved_to_a_swimlane_and_before_a_us` | `taiga/projects/models.py::Project` | no | ACCESSES_MODEL | - |  |  |

## Both have it (spot check) (0 of 0)
<!-- group: both -->

Both engines agree. Check a few: an agreement can still be wrong.

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|

