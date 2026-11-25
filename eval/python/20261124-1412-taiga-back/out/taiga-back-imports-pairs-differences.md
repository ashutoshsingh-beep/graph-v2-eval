# taiga-back (python): IMPORTS, graph v2 against dev

Engines: v2 `4e50b002a213`, dev `25ae40bf8662`. No oracle: you judge each row.

## Counts

v2 2931 pairs, dev 1962 pairs (dev types: IMPORTS 1962).
Both 1894, only v2 1037, only dev 68; agreement 63.2% of the union.
Pairs are matched on (file, name with only letters and digits) of both ends, so the engines' different spellings of one test or scope meet; an edge to a route, data or package node (v2) has no dev counterpart. v2 unresolved and external edges are left out.

Verdict: `confirmed` (the group is right), `v2 wrong`, `dev wrong`, `both wrong`, or `?`. Cause: one short phrase.

## Only v2 has it (25 of 1037)
<!-- group: only_v2 -->

v2 has this edge, dev does not. Check: is the edge real in the code (v2 gain) or wrong (v2 wrong)?

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|
| 1 | `taiga/auth/api.py` | `taiga/base/response.py` | yes | no | taiga/auth/api.py:14 |  |  |
| 2 | `taiga/base/api/authentication.py` | `taiga/base/api/__init__.py::taiga.base.api.HTTP_HEADER_ENCODING` | yes | no | taiga/base/api/authentication.py:44 |  |  |
| 3 | `taiga/base/api/mixins.py` | `taiga/base/response.py` | yes | no | taiga/base/api/mixins.py:40 |  |  |
| 4 | `taiga/base/api/viewsets.py` | `taiga/base/api/generics.py` | yes | no | taiga/base/api/viewsets.py:40 |  |  |
| 5 | `taiga/export_import/serializers/cache.py` | `taiga/users/models.py` | yes | no | taiga/export_import/serializers/cache.py:8 |  |  |
| 6 | `taiga/external_apps/admin.py` | `taiga/external_apps/models.py` | yes | no | taiga/external_apps/admin.py:10 |  |  |
| 7 | `taiga/external_apps/api.py` | `taiga/base/response.py` | yes | no | taiga/external_apps/api.py:14 |  |  |
| 8 | `taiga/importers/asana/api.py` | `taiga/base/response.py` | yes | no | taiga/importers/asana/api.py:12 |  |  |
| 9 | `taiga/importers/github/api.py` | `taiga/importers/exceptions.py` | yes | no | taiga/importers/github/api.py:19 |  |  |
| 10 | `taiga/projects/api.py` | `taiga/projects/filters.py` | yes | no | taiga/projects/api.py:50 |  |  |
| 11 | `taiga/projects/api.py` | `taiga/projects/throttling.py` | yes | no | taiga/projects/api.py:58 |  |  |
| 12 | `taiga/projects/epics/api.py` | `taiga/base/api/viewsets.py::ModelCrudViewSet` | yes | no | taiga/projects/epics/api.py:15 |  |  |
| 13 | `taiga/projects/epics/api.py` | `taiga/projects/epics/serializers.py` | yes | no | taiga/projects/epics/api.py:32 |  |  |
| 14 | `taiga/projects/issues/migrations/0003_auto_20141210_1108.py` | `taiga/projects/userstories/models.py` | yes | no | taiga/projects/issues/migrations/0003_auto_20141210_1108.py:12 |  |  |
| 15 | `taiga/projects/milestones/services.py` | `taiga/projects/services/bulk_update_order.py::apply_order_updates` | yes | no | taiga/projects/milestones/services.py:11 |  |  |
| 16 | `taiga/projects/notifications/services.py` | `taiga/events/events.py` | yes | no | taiga/projects/notifications/services.py:33 |  |  |
| 17 | `taiga/projects/settings/api.py` | `taiga/projects/settings/services.py` | yes | no | taiga/projects/settings/api.py:19 |  |  |
| 18 | `taiga/projects/tagging/api.py` | `taiga/base/response.py` | yes | no | taiga/projects/tagging/api.py:8 |  |  |
| 19 | `taiga/timeline/apps.py` | `taiga/timeline/signals.py` | yes | no | taiga/timeline/apps.py:19 |  |  |
| 20 | `tests/integration/resources_permissions/test_milestones_resources.py` | `taiga/projects/choices.py` | yes | no | tests/integration/resources_permissions/test_milestones_resources.py:12 |  |  |
| 21 | `tests/integration/test_hooks_bitbucket.py` | `taiga/projects/services/__init__.py` | yes | no | tests/integration/test_hooks_bitbucket.py:30 |  |  |
| 22 | `tests/integration/test_userstories_update_backlog_order.py` | `tests/factories.py` | yes | no | tests/integration/test_userstories_update_backlog_order.py:24 |  |  |
| 23 | `tests/integration/test_vote_tasks.py` | `tests/factories.py` | yes | no | tests/integration/test_vote_tasks.py:11 |  |  |
| 24 | `tests/integration/test_votes.py` | `taiga/projects/votes/services.py` | yes | no | tests/integration/test_votes.py:12 |  |  |
| 25 | `tests/integration/test_webhooks_wikipages.py` | `taiga/base/utils/json.py` | yes | no | tests/integration/test_webhooks_wikipages.py:20 |  |  |

## Only dev has it (25 of 68)
<!-- group: only_dev -->

dev has this edge, v2 does not. Check: is it real (a v2 gap) or wrong (dev wrong)?

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|
| 1 | `taiga/auth/api.py` | `taiga/auth/authentication.py::AUTH_HEADER_TYPES` | no | IMPORTS | - |  |  |
| 2 | `taiga/auth/tokens.py` | `taiga/auth/utils.py::format_lazy` | no | IMPORTS | - |  |  |
| 3 | `taiga/base/api/fields.py` | `taiga/base/api/__init__.py::ISO_8601` | no | IMPORTS | - |  |  |
| 4 | `taiga/base/api/generics.py` | `taiga/base/api/utils/__init__.py::get_object_or_error` | no | IMPORTS | - |  |  |
| 5 | `taiga/base/fields.py` | `taiga/base/api/__init__.py::ISO_8601` | no | IMPORTS | - |  |  |
| 6 | `taiga/base/filters.py` | `taiga/base/api/utils/__init__.py::get_object_or_error` | no | IMPORTS | - |  |  |
| 7 | `taiga/external_apps/api.py` | `taiga/base/api/utils/__init__.py::get_object_or_404` | no | IMPORTS | - |  |  |
| 8 | `taiga/external_apps/migrations/0001_initial.py` | `Module:taiga.external_apps.models` | no | IMPORTS | - |  |  |
| 9 | `taiga/projects/attachments/api.py` | `taiga/base/api/utils/__init__.py::get_object_or_404` | no | IMPORTS | - |  |  |
| 10 | `taiga/projects/attachments/api.py` | `taiga/base/api/utils/__init__.py::get_object_or_error` | no | IMPORTS | - |  |  |
| 11 | `taiga/projects/epics/migrations/0002_epic_color.py` | `Module:taiga.base.utils.colors` | no | IMPORTS | - |  |  |
| 12 | `taiga/projects/issues/api.py` | `taiga/base/api/utils/__init__.py::get_object_or_error` | no | IMPORTS | - |  |  |
| 13 | `taiga/projects/likes/mixins/viewsets.py` | `taiga/base/api/utils/__init__.py::get_object_or_error` | no | IMPORTS | - |  |  |
| 14 | `taiga/projects/migrations/0031_project_logo.py` | `Module:taiga.projects.models` | no | IMPORTS | - |  |  |
| 15 | `taiga/projects/migrations/0054_auto_20160928_0540.py` | `Module:taiga.base.utils.time` | no | IMPORTS | - |  |  |
| 16 | `taiga/projects/migrations/0058_auto_20161215_1347.py` | `Module:taiga.base.db.models.fields.json` | no | IMPORTS | - |  |  |
| 17 | `taiga/projects/migrations/0060_auto_20180614_1338.py` | `Module:taiga.base.db.models.fields.json` | no | IMPORTS | - |  |  |
| 18 | `taiga/projects/mixins/ordering.py` | `taiga/base/api/utils/__init__.py::get_object_or_404` | no | IMPORTS | - |  |  |
| 19 | `taiga/projects/notifications/api.py` | `taiga/base/api/utils/__init__.py::get_object_or_error` | no | IMPORTS | - |  |  |
| 20 | `taiga/projects/notifications/migrations/0007_notifypolicy_live_notify_level.py` | `Module:taiga.projects.notifications.choices` | no | IMPORTS | - |  |  |
| 21 | `taiga/projects/settings/migrations/0001_initial.py` | `Module:taiga.projects.settings.choices` | no | IMPORTS | - |  |  |
| 22 | `taiga/projects/userstories/migrations/0014_auto_20160928_0540.py` | `Module:taiga.base.utils.time` | no | IMPORTS | - |  |  |
| 23 | `taiga/projects/userstories/migrations/0021_auto_20201202_0850.py` | `Module:taiga.base.utils.time` | no | IMPORTS | - |  |  |
| 24 | `taiga/projects/wiki/api.py` | `taiga/base/api/utils/__init__.py::get_object_or_404` | no | IMPORTS | - |  |  |
| 25 | `tests/integration/test_webhook_serializers.py` | `Module:taiga.webhooks.serializers` | no | IMPORTS | - |  |  |

## Both have it (spot check) (25 of 1894)
<!-- group: both -->

Both engines agree. Check a few: an agreement can still be wrong.

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|
| 1 | `taiga/auth/serializers.py` | `taiga/auth/services.py::refresh_token` | yes | IMPORTS | taiga/auth/serializers.py:42 |  |  |
| 2 | `taiga/export_import/serializers/serializers.py` | `taiga/export_import/serializers/cache.py::_issues_statuses_cache` | yes | IMPORTS | taiga/export_import/serializers/serializers.py:19 |  |  |
| 3 | `taiga/external_apps/api.py` | `taiga/base/decorators.py::detail_route` | yes | IMPORTS | taiga/external_apps/api.py:18 |  |  |
| 4 | `taiga/front/sitemaps/wiki.py` | `taiga/front/templatetags/functions.py::resolve` | yes | IMPORTS | taiga/front/sitemaps/wiki.py:13 |  |  |
| 5 | `taiga/importers/pivotal/importer.py` | `taiga/projects/history/services.py::make_diff_values` | yes | IMPORTS | taiga/importers/pivotal/importer.py:21 |  |  |
| 6 | `taiga/projects/admin.py` | `taiga/projects/userstories/apps.py::disconnect_all_userstories_signals` | yes | IMPORTS | taiga/projects/admin.py:214 |  |  |
| 7 | `taiga/projects/custom_attributes/permissions.py` | `taiga/base/api/permissions.py::AllowAny` | yes | IMPORTS | taiga/projects/custom_attributes/permissions.py:11 |  |  |
| 8 | `taiga/projects/notifications/serializers.py` | `taiga/users/gravatar.py::get_user_gravatar_id` | yes | IMPORTS | taiga/projects/notifications/serializers.py:12 |  |  |
| 9 | `taiga/projects/notifications/services.py` | `taiga/projects/notifications/choices.py::NotifyLevel` | yes | IMPORTS | taiga/projects/notifications/services.py:26 |  |  |
| 10 | `taiga/projects/services/__init__.py` | `taiga/projects/services/bulk_update_order.py::bulk_update_issue_type_order` | yes | IMPORTS | taiga/projects/services/__init__.py:17 |  |  |
| 11 | `taiga/projects/services/__init__.py` | `taiga/projects/services/members.py::create_members_in_bulk` | yes | IMPORTS | taiga/projects/services/__init__.py:34 |  |  |
| 12 | `taiga/projects/services/__init__.py` | `taiga/projects/services/members.py::get_max_memberships_for_project` | yes | IMPORTS | taiga/projects/services/__init__.py:37 |  |  |
| 13 | `taiga/projects/userstories/api.py` | `taiga/projects/votes/mixins/viewsets.py::VotersViewSetMixin` | yes | IMPORTS | taiga/projects/userstories/api.py:38 |  |  |
| 14 | `taiga/projects/userstories/services.py` | `taiga/projects/tasks/models.py::Task` | yes | IMPORTS | taiga/projects/userstories/services.py:32 |  |  |
| 15 | `taiga/projects/wiki/api.py` | `taiga/projects/models.py::Project` | yes | IMPORTS | taiga/projects/wiki/api.py:23 |  |  |
| 16 | `taiga/projects/wiki/serializers.py` | `taiga/projects/notifications/mixins.py::WatchedResourceSerializer` | yes | IMPORTS | taiga/projects/wiki/serializers.py:12 |  |  |
| 17 | `taiga/users/admin.py` | `taiga/users/forms.py::UserCreationForm` | yes | IMPORTS | taiga/users/admin.py:18 |  |  |
| 18 | `taiga/users/models.py` | `taiga/base/utils/slug.py::slugify_uniquely` | yes | IMPORTS | taiga/users/models.py:31 |  |  |
| 19 | `tests/integration/resources_permissions/test_history_resources.py` | `tests/utils.py::helper_test_http_method` | yes | IMPORTS | tests/integration/resources_permissions/test_history_resources.py:18 |  |  |
| 20 | `tests/integration/resources_permissions/test_storage_resources.py` | `taiga/userstorage/serializers.py::StorageEntrySerializer` | yes | IMPORTS | tests/integration/resources_permissions/test_storage_resources.py:11 |  |  |
| 21 | `tests/integration/resources_permissions/test_tasks_custom_attributes_resource.py` | `taiga/permissions/choices.py::MEMBERS_PERMISSIONS` | yes | IMPORTS | tests/integration/resources_permissions/test_tasks_custom_attributes_resource.py:13 |  |  |
| 22 | `tests/integration/test_hooks_gitlab.py` | `taiga/projects/history/services.py::get_history_queryset_by_model_instance` | yes | IMPORTS | tests/integration/test_hooks_gitlab.py:26 |  |  |
| 23 | `tests/integration/test_importer_api.py` | `taiga/projects/issues/models.py::Issue` | yes | IMPORTS | tests/integration/test_importer_api.py:20 |  |  |
| 24 | `tests/integration/test_users.py` | `taiga/users/services.py::get_liked_list` | yes | IMPORTS | tests/integration/test_users.py:32 |  |  |
| 25 | `tests/unit/test_utils.py` | `taiga/base/utils/db.py::to_tsquery` | yes | IMPORTS | tests/unit/test_utils.py:24 |  |  |

