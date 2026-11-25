# taiga-back (python): CONTAINS, graph v2 against dev

Engines: v2 `4e50b002a213`, dev `25ae40bf8662`. No oracle: you judge each row.

## Counts

v2 20 pairs, dev 6800 pairs (dev types: CONTAINS 6800).
Both 20, only v2 0, only dev 6780; agreement 0.3% of the union.
Pairs are matched on (file, name with only letters and digits) of both ends, so the engines' different spellings of one test or scope meet; an edge to a route, data or package node (v2) has no dev counterpart. v2 unresolved and external edges are left out.

Verdict: `confirmed` (the group is right), `v2 wrong`, `dev wrong`, `both wrong`, or `?`. Cause: one short phrase.

## Only v2 has it (0 of 0)
<!-- group: only_v2 -->

v2 has this edge, dev does not. Check: is the edge real in the code (v2 gain) or wrong (v2 wrong)?

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|

## Only dev has it (25 of 6780)
<!-- group: only_dev -->

dev has this edge, v2 does not. Check: is it real (a v2 gap) or wrong (dev wrong)?

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|
| 1 | `taiga/base/apps.py::BaseAppConfig` | `taiga/base/apps.py::BaseAppConfig.ready` | no | CONTAINS | - |  |  |
| 2 | `taiga/export_import/serializers/serializers.py::EpicRelatedUserStoryExportSerializer` | `taiga/export_import/serializers/serializers.py::EpicRelatedUserStoryExportSerializer.order` | no | CONTAINS | - |  |  |
| 3 | `taiga/export_import/serializers/serializers.py::IssueExportSerializer` | `taiga/export_import/serializers/serializers.py::IssueExportSerializer.external_reference` | no | CONTAINS | - |  |  |
| 4 | `taiga/external_apps/serializers.py::ApplicationSerializer` | `taiga/external_apps/serializers.py::ApplicationSerializer.icon_url` | no | CONTAINS | - |  |  |
| 5 | `taiga/importers/github/importer.py::AssignedEventHandler` | `taiga/importers/github/importer.py::AssignedEventHandler.handle` | no | CONTAINS | - |  |  |
| 6 | `taiga/projects/admin.py::IssueTypeAdmin` | `taiga/projects/admin.py::IssueTypeAdmin.list_display` | no | CONTAINS | - |  |  |
| 7 | `taiga/projects/admin.py::SeverityAdmin` | `taiga/projects/admin.py::SeverityAdmin.raw_id_fields` | no | CONTAINS | - |  |  |
| 8 | `taiga/projects/api.py::PriorityViewSet` | `taiga/projects/api.py::PriorityViewSet.bulk_update_perm` | no | CONTAINS | - |  |  |
| 9 | `taiga/projects/epics/api.py::EpicRelatedUserStoryViewSet` | `taiga/projects/epics/api.py::EpicRelatedUserStoryViewSet.validator_class` | no | CONTAINS | - |  |  |
| 10 | `taiga/projects/history/migrations/0012_auto_20160629_1036.py::Migration` | `taiga/projects/history/migrations/0012_auto_20160629_1036.py::Migration.dependencies` | no | CONTAINS | - |  |  |
| 11 | `taiga/projects/likes/models.py::Like.Meta` | `taiga/projects/likes/models.py::Like.Meta.unique_together` | no | CONTAINS | - |  |  |
| 12 | `taiga/projects/models.py::Project.Meta` | `taiga/projects/models.py::Project.Meta.verbose_name_plural` | no | CONTAINS | - |  |  |
| 13 | `taiga/projects/models.py::SwimlaneUserStoryStatus` | `taiga/projects/models.py::SwimlaneUserStoryStatus.status` | no | CONTAINS | - |  |  |
| 14 | `taiga/projects/serializers.py::ProjectSerializer` | `taiga/projects/serializers.py::ProjectSerializer.tags` | no | CONTAINS | - |  |  |
| 15 | `taiga/projects/serializers.py::ProjectTemplateSerializer` | `taiga/projects/serializers.py::ProjectTemplateSerializer.issue_types` | no | CONTAINS | - |  |  |
| 16 | `taiga/projects/serializers.py::UserStoryStatusSerializer` | `taiga/projects/serializers.py::UserStoryStatusSerializer.id` | no | CONTAINS | - |  |  |
| 17 | `taiga/projects/userstories/serializers.py::UserStoryListSerializer` | `taiga/projects/userstories/serializers.py::UserStoryListSerializer.external_reference` | no | CONTAINS | - |  |  |
| 18 | `taiga/projects/validators.py::UpdateProjectOrderBulkValidator` | `taiga/projects/validators.py::UpdateProjectOrderBulkValidator.project_id` | no | CONTAINS | - |  |  |
| 19 | `taiga/projects/votes/mixins/viewsets.py::VotedResourceMixin` | `taiga/projects/votes/mixins/viewsets.py::VotedResourceMixin.downvote` | no | CONTAINS | - |  |  |
| 20 | `taiga/timeline/models.py::Timeline.Meta` | `taiga/timeline/models.py::Timeline.Meta.indexes` | no | CONTAINS | - |  |  |
| 21 | `taiga/timeline/serializers.py::TimelineSerializer` | `taiga/timeline/serializers.py::TimelineSerializer.data` | no | CONTAINS | - |  |  |
| 22 | `taiga/users/serializers.py::UserBasicInfoSerializer` | `taiga/users/serializers.py::UserBasicInfoSerializer.photo` | no | CONTAINS | - |  |  |
| 23 | `taiga/webhooks/serializers.py::MilestoneSerializer` | `taiga/webhooks/serializers.py::MilestoneSerializer.id` | no | CONTAINS | - |  |  |
| 24 | `tests/factories.py::AttachmentFactory.Meta` | `tests/factories.py::AttachmentFactory.Meta.model` | no | CONTAINS | - |  |  |
| 25 | `tests/fixtures.py::PartialMethodCaller` | `tests/fixtures.py::PartialMethodCaller.__getattr__` | no | CONTAINS | - |  |  |

## Both have it (spot check) (20 of 20)
<!-- group: both -->

Both engines agree. Check a few: an agreement can still be wrong.

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|
| 1 | `tests/integration/test_neighbors.py::TestIssues` | `tests/integration/test_neighbors.py::TestIssues.test_empty_related_queryset` | yes | CONTAINS | tests/integration/test_neighbors.py:110 |  |  |
| 2 | `tests/integration/test_neighbors.py::TestIssues` | `tests/integration/test_neighbors.py::TestIssues.test_no_filters` | yes | CONTAINS | tests/integration/test_neighbors.py:98 |  |  |
| 3 | `tests/integration/test_neighbors.py::TestIssues` | `tests/integration/test_neighbors.py::TestIssues.test_ordering_by_assigned_to` | yes | CONTAINS | tests/integration/test_neighbors.py:274 |  |  |
| 4 | `tests/integration/test_neighbors.py::TestIssues` | `tests/integration/test_neighbors.py::TestIssues.test_ordering_by_assigned_to_desc` | yes | CONTAINS | tests/integration/test_neighbors.py:293 |  |  |
| 5 | `tests/integration/test_neighbors.py::TestIssues` | `tests/integration/test_neighbors.py::TestIssues.test_ordering_by_assigned_to_desc_with_none_and_normal_values` | yes | CONTAINS | tests/integration/test_neighbors.py:328 |  |  |
| 6 | `tests/integration/test_neighbors.py::TestIssues` | `tests/integration/test_neighbors.py::TestIssues.test_ordering_by_assigned_to_desc_with_none_values` | yes | CONTAINS | tests/integration/test_neighbors.py:312 |  |  |
| 7 | `tests/integration/test_neighbors.py::TestIssues` | `tests/integration/test_neighbors.py::TestIssues.test_ordering_by_owner` | yes | CONTAINS | tests/integration/test_neighbors.py:236 |  |  |
| 8 | `tests/integration/test_neighbors.py::TestIssues` | `tests/integration/test_neighbors.py::TestIssues.test_ordering_by_owner_desc` | yes | CONTAINS | tests/integration/test_neighbors.py:255 |  |  |
| 9 | `tests/integration/test_neighbors.py::TestIssues` | `tests/integration/test_neighbors.py::TestIssues.test_ordering_by_priority` | yes | CONTAINS | tests/integration/test_neighbors.py:198 |  |  |
| 10 | `tests/integration/test_neighbors.py::TestIssues` | `tests/integration/test_neighbors.py::TestIssues.test_ordering_by_priority_desc` | yes | CONTAINS | tests/integration/test_neighbors.py:217 |  |  |
| 11 | `tests/integration/test_neighbors.py::TestIssues` | `tests/integration/test_neighbors.py::TestIssues.test_ordering_by_severity` | yes | CONTAINS | tests/integration/test_neighbors.py:122 |  |  |
| 12 | `tests/integration/test_neighbors.py::TestIssues` | `tests/integration/test_neighbors.py::TestIssues.test_ordering_by_severity_desc` | yes | CONTAINS | tests/integration/test_neighbors.py:141 |  |  |
| 13 | `tests/integration/test_neighbors.py::TestIssues` | `tests/integration/test_neighbors.py::TestIssues.test_ordering_by_status` | yes | CONTAINS | tests/integration/test_neighbors.py:160 |  |  |
| 14 | `tests/integration/test_neighbors.py::TestIssues` | `tests/integration/test_neighbors.py::TestIssues.test_ordering_by_status_desc` | yes | CONTAINS | tests/integration/test_neighbors.py:179 |  |  |
| 15 | `tests/integration/test_neighbors.py::TestUserStories` | `tests/integration/test_neighbors.py::TestUserStories.test_filtered_by_milestone` | yes | CONTAINS | tests/integration/test_neighbors.py:80 |  |  |
| 16 | `tests/integration/test_neighbors.py::TestUserStories` | `tests/integration/test_neighbors.py::TestUserStories.test_filtered_by_tags` | yes | CONTAINS | tests/integration/test_neighbors.py:65 |  |  |
| 17 | `tests/integration/test_neighbors.py::TestUserStories` | `tests/integration/test_neighbors.py::TestUserStories.test_no_filters` | yes | CONTAINS | tests/integration/test_neighbors.py:28 |  |  |
| 18 | `tests/integration/test_neighbors.py::TestUserStories` | `tests/integration/test_neighbors.py::TestUserStories.test_results_set_left_repeat_id` | yes | CONTAINS | tests/integration/test_neighbors.py:51 |  |  |
| 19 | `tests/integration/test_neighbors.py::TestUserStories` | `tests/integration/test_neighbors.py::TestUserStories.test_results_set_repeat_id` | yes | CONTAINS | tests/integration/test_neighbors.py:40 |  |  |
| 20 | `tests/integration/test_webhook_serializers.py::TestCustomAttributesValuesWebhookSerializerMixin` | `tests/integration/test_webhook_serializers.py::TestCustomAttributesValuesWebhookSerializerMixin.test_get_custom_attributes_values` | yes | CONTAINS | tests/integration/test_webhook_serializers.py:9 |  |  |

