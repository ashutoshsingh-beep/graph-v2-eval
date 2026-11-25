# taiga-back (python): CALLS, graph v2 against dev

Engines: v2 `4e50b002a213`, dev `25ae40bf8662`. No oracle: you judge each row.

## Counts

v2 7438 pairs, dev 7480 pairs (dev types: CALLS 7480).
Both 4486, only v2 2952, only dev 2994; agreement 43.0% of the union.
Pairs are matched on (file, name with only letters and digits) of both ends, so the engines' different spellings of one test or scope meet; an edge to a route, data or package node (v2) has no dev counterpart. v2 unresolved and external edges are left out.

Verdict: `confirmed` (the group is right), `v2 wrong`, `dev wrong`, `both wrong`, or `?`. Cause: one short phrase.

## Only v2 has it (25 of 2952)
<!-- group: only_v2 -->

v2 has this edge, dev does not. Check: is the edge real in the code (v2 gain) or wrong (v2 wrong)?

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|
| 1 | `framework::python::_pytest.fixtures.FixtureDef.execute` | `tests/integration/resources_permissions/test_epics_custom_attributes_resource.py::data` | yes | no | tests/integration/resources_permissions/test_epics_custom_attributes_resource.py:23 |  |  |
| 2 | `framework::python::_pytest.fixtures.FixtureDef.execute` | `tests/integration/resources_permissions/test_storage_resources.py::data` | yes | no | tests/integration/resources_permissions/test_storage_resources.py:31 |  |  |
| 3 | `taiga/base/api/generics.py::RetrieveUpdateDestroyAPIView.put` | `taiga/base/api/mixins.py::UpdateModelMixin.update` | yes | no | taiga/base/api/generics.py:405 |  |  |
| 4 | `taiga/base/filters.py::MembersFilterBackend.filter_queryset` | `taiga/base/exceptions.py::BaseException.__init__` | yes | no | taiga/base/filters.py:274 |  |  |
| 5 | `taiga/export_import/services/store.py::_validate_if_owner_have_enough_space_to_this_project` | `taiga/export_import/exceptions.py::TaigaImportError.__init__` | yes | no | taiga/export_import/services/store.py:796 |  |  |
| 6 | `taiga/export_import/validators/fields.py::HistoryValuesField.from_native` | `taiga/base/api/relations.py::RelatedField.__init__` | yes | no | taiga/export_import/validators/fields.py:175 |  |  |
| 7 | `taiga/importers/jira/agile.py::JiraAgileImporter._import_user_stories_data` | `taiga/importers/jira/common.py::JiraImporterCommon._import_attachments` | yes | no | taiga/importers/jira/agile.py:249 |  |  |
| 8 | `taiga/projects/epics/validators.py::EpicValidator` | `taiga/base/api/fields.py::WritableField.__init__` | yes | no | taiga/projects/epics/validators.py:34 |  |  |
| 9 | `taiga/projects/history/api.py::HistoryViewSet.list` | `taiga/base/response.py::NotFound` | yes | no | taiga/projects/history/api.py:180 |  |  |
| 10 | `taiga/projects/milestones/api.py::MilestoneViewSet.move_tasks_to_sprint` | `taiga/base/api/utils/__init__.py::taiga.base.api.utils.get_object_or_error` | yes | no | taiga/projects/milestones/api.py:164 |  |  |
| 11 | `taiga/projects/notifications/api.py::WebNotificationsViewSet.list` | `taiga/base/response.py::Ok` | yes | no | taiga/projects/notifications/api.py:58 |  |  |
| 12 | `taiga/projects/notifications/services.py::create_notify_policy_if_not_exists` | `taiga/base/exceptions.py::BaseException.__init__` | yes | no | taiga/projects/notifications/services.py:93 |  |  |
| 13 | `taiga/projects/tagging/validators.py::DeleteTagValidator.validate_tag` | `taiga/base/exceptions.py::ValidationError` | yes | no | taiga/projects/tagging/validators.py:91 |  |  |
| 14 | `taiga/projects/validators.py::DuplicateProjectValidator` | `taiga/base/api/fields.py::CharField` | yes | no | taiga/projects/validators.py:342 |  |  |
| 15 | `taiga/users/api.py::UsersViewSet.create` | `taiga/base/exceptions.py::BaseException.__init__` | yes | no | taiga/users/api.py:79 |  |  |
| 16 | `taiga/users/api.py::UsersViewSet.watched` | `taiga/base/response.py::Ok` | yes | no | taiga/users/api.py:428 |  |  |
| 17 | `tests/integration/resources_permissions/test_auth_resources.py::teardown_module` | `tests/utils.py::reconnect_signals` | yes | no | tests/integration/resources_permissions/test_auth_resources.py:24 |  |  |
| 18 | `tests/integration/test_hooks_bitbucket.py::test_push_event_task_processing` | `tests/factories.py::MembershipFactory` | yes | no | tests/integration/test_hooks_bitbucket.py:299 |  |  |
| 19 | `tests/integration/test_memberships.py::test_api_create_member_max_pending_memberships` | `tests/factories.py::ProjectFactory` | yes | no | tests/integration/test_memberships.py:883 |  |  |
| 20 | `tests/integration/test_memberships.py::test_api_create_membership_without_enough_memberships_private_project_slots_multiple_projects` | `tests/factories.py::RoleFactory` | yes | no | tests/integration/test_memberships.py:731 |  |  |
| 21 | `tests/integration/test_neighbors.py::teardown_module` | `tests/utils.py::reconnect_signals` | yes | no | tests/integration/test_neighbors.py:23 |  |  |
| 22 | `tests/integration/test_projects.py::test_private_project_can_be_public_because_owner_has_unlimited_slot` | `tests/factories.py::create_project` | yes | no | tests/integration/test_projects.py:1560 |  |  |
| 23 | `tests/integration/test_projects.py::test_public_project_can_be_private_because_project_has_unlimited_members` | `tests/factories.py::MembershipFactory` | yes | no | tests/integration/test_projects.py:1674 |  |  |
| 24 | `tests/integration/test_users.py::test_get_watched_list` | `tests/factories.py::RoleFactory` | yes | no | tests/integration/test_users.py:920 |  |  |
| 25 | `tests/integration/test_userstorage_api.py::test_list_userstorage` | `tests/factories.py::UserFactory` | yes | no | tests/integration/test_userstorage_api.py:19 |  |  |

## Only dev has it (25 of 2994)
<!-- group: only_dev -->

dev has this edge, v2 does not. Check: is it real (a v2 gap) or wrong (dev wrong)?

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|
| 1 | `taiga/base/api/fields.py::ChoiceField.metadata` | `taiga/base/api/fields.py::ChoiceField` | no | CALLS | - |  |  |
| 2 | `taiga/base/api/fields.py::WritableField.field_from_native` | `taiga/base/api/serializers.py::BaseSerializer.from_native` | no | CALLS | - |  |  |
| 3 | `taiga/base/api/generics.py::GenericAPIView.filter_queryset` | `taiga/base/api/generics.py::GenericAPIView.get_filter_backends` | no | CALLS | - |  |  |
| 4 | `taiga/base/api/generics.py::ListCreateAPIView` | `taiga/base/api/generics.py::GenericAPIView.get_serializer_class.<locals>.DefaultSerializer` | no | CALLS | - |  |  |
| 5 | `taiga/base/api/mixins.py::UpdateModelMixin.update` | `taiga/projects/userstories/api.py::UserStoryViewSet.pre_validate` | no | CALLS | - |  |  |
| 6 | `taiga/export_import/services/validations.py::has_available_slot_for_new_project` | `taiga/projects/models.py::Membership` | no | CALLS | - |  |  |
| 7 | `taiga/export_import/validators/validators.py::MilestoneExportValidator.__init__` | `taiga/export_import/validators/mixins.py::WatcheableObjectModelValidatorMixin.__init__` | no | CALLS | - |  |  |
| 8 | `taiga/hooks/event_hooks.py::BaseIssueEventHook.process_event` | `taiga/hooks/event_hooks.py::BaseIssueEventHook.action_type` | no | CALLS | - |  |  |
| 9 | `taiga/importers/jira/normal.py::JiraNormalImporter._link_epics_with_user_stories` | `taiga/projects/epics/models.py::RelatedUserStory` | no | CALLS | - |  |  |
| 10 | `taiga/importers/trello/importer.py::TrelloImporter.list_projects` | `taiga/importers/trello/importer.py::TrelloClient.get` | no | CALLS | - |  |  |
| 11 | `taiga/projects/api.py::PointsViewSet` | `taiga/projects/serializers.py::PointsSerializer` | no | CALLS | - |  |  |
| 12 | `taiga/projects/attachments/admin.py` | `taiga/projects/attachments/admin.py::AttachmentAdmin` | no | CALLS | - |  |  |
| 13 | `taiga/projects/epics/api.py::EpicViewSet` | `taiga/projects/epics/permissions.py::EpicPermission` | no | CALLS | - |  |  |
| 14 | `taiga/projects/history/freeze_impl.py::userstory_values` | `taiga/base/utils/collections.py::OrderedSet.add` | no | CALLS | - |  |  |
| 15 | `taiga/projects/wiki/api.py::WikiViewSet.pre_save` | `taiga/projects/occ/mixins.py::OCCResourceMixin.pre_save` | no | CALLS | - |  |  |
| 16 | `taiga/users/services.py::get_visible_project_ids` | `taiga/projects/models.py::Membership` | no | CALLS | - |  |  |
| 17 | `tests/integration/resources_permissions/test_epics_related_userstories_resources.py::test_epic_related_userstories_list` | `taiga/auth/backends.py::TokenBackend.decode` | no | CALLS | - |  |  |
| 18 | `tests/integration/resources_permissions/test_epics_resources.py::test_epic_put_update_with_project_change` | `taiga/projects/models.py::Project` | no | CALLS | - |  |  |
| 19 | `tests/integration/resources_permissions/test_projects_resource.py::test_project_list` | `taiga/auth/backends.py::TokenBackend.decode` | no | CALLS | - |  |  |
| 20 | `tests/integration/resources_permissions/test_userstories_resources.py::test_user_story_put_update_and_comment` | `taiga/base/api/serializers.py::LightSerializer.__init__` | no | CALLS | - |  |  |
| 21 | `tests/integration/resources_permissions/test_wiki_resources.py::test_wiki_link_create` | `taiga/projects/wiki/models.py::WikiLink` | no | CALLS | - |  |  |
| 22 | `tests/integration/test_auth.py::test_auth_uppercase_ignore` | `taiga/auth/models.py::TokenUser.set_password` | no | CALLS | - |  |  |
| 23 | `tests/integration/test_hooks_gitlab.py::test_signal_handlers_move_on_destroy_with_not_assigned_status` | `tests/integration/test_userstories.py::test_api_filters_data_respects_archived_status_and_other_filters.<locals>.count` | no | CALLS | - |  |  |
| 24 | `tests/integration/test_importers_asana_api.py::test_authorize_without_code` | `taiga/base/utils/json.py::dumps` | no | CALLS | - |  |  |
| 25 | `tests/integration/test_projects.py::test_mix_tags` | `taiga/projects/tasks/models.py::Task` | no | CALLS | - |  |  |

## Both have it (spot check) (25 of 4486)
<!-- group: both -->

Both engines agree. Check a few: an agreement can still be wrong.

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|
| 1 | `taiga/base/api/renderers.py::StaticHTMLRenderer.render` | `taiga/base/api/renderers.py::TemplateHTMLRenderer.resolve_context` | yes | CALLS | taiga/base/api/renderers.py:287 |  |  |
| 2 | `taiga/export_import/serializers/serializers.py::RolePointsExportSerializer` | `taiga/export_import/serializers/fields.py::SlugRelatedField` | yes | CALLS | taiga/export_import/serializers/serializers.py:201 |  |  |
| 3 | `taiga/export_import/services/store.py::store_issue` | `taiga/export_import/services/store.py::_store_history` | yes | CALLS | taiga/export_import/services/store.py:652 |  |  |
| 4 | `taiga/export_import/validators/validators.py::ProjectExportValidator` | `taiga/export_import/validators/validators.py::PriorityExportValidator` | yes | CALLS | taiga/export_import/validators/validators.py:420 |  |  |
| 5 | `taiga/hooks/bitbucket/event_hooks.py::IssuesEventHook.get_data` | `taiga/hooks/bitbucket/event_hooks.py::BaseBitBucketEventHook.replace_bitbucket_references` | yes | CALLS | taiga/hooks/bitbucket/event_hooks.py:42 |  |  |
| 6 | `taiga/hooks/gitlab/api.py::GitLabViewSet._get_event_name` | `taiga/base/utils/json.py::loads` | yes | CALLS | taiga/hooks/gitlab/api.py:64 |  |  |
| 7 | `taiga/importers/github/api.py::GithubImporterViewSet.list_projects` | `taiga/importers/github/importer.py::GithubImporter` | yes | CALLS | taiga/importers/github/api.py:55 |  |  |
| 8 | `taiga/importers/jira/api.py::JiraImporterViewSet.list_users` | `taiga/users/gravatar.py::get_user_gravatar_id` | yes | CALLS | taiga/importers/jira/api.py:79 |  |  |
| 9 | `taiga/importers/trello/importer.py::TrelloImporter._import_action` | `taiga/mdrender/service.py::render` | yes | CALLS | taiga/importers/trello/importer.py:422 |  |  |
| 10 | `taiga/projects/api.py::ProjectViewSet.pre_save` | `taiga/projects/services/projects.py::check_if_project_can_be_created_or_updated` | yes | CALLS | taiga/projects/api.py:528 |  |  |
| 11 | `taiga/projects/history/permissions.py::WikiHistoryPermission` | `taiga/base/api/permissions.py::HasProjectPerm` | yes | CALLS | taiga/projects/history/permissions.py:67 |  |  |
| 12 | `taiga/projects/references/models.py::make_unique_reference_id` | `taiga/projects/references/models.py::make_sequence_name` | yes | CALLS | taiga/projects/references/models.py:49 |  |  |
| 13 | `taiga/projects/serializers.py::SeveritySerializer` | `taiga/base/fields.py::Field` | yes | CALLS | taiga/projects/serializers.py:123 |  |  |
| 14 | `taiga/projects/tasks/signals.py::_try_to_close_or_open_milestone_when_create_or_edit_task` | `taiga/projects/milestones/services.py::calculate_milestone_is_closed` | yes | CALLS | taiga/projects/tasks/signals.py:70 |  |  |
| 15 | `taiga/projects/userstories/signals.py::try_to_close_milestone_when_delete_us` | `taiga/projects/userstories/signals.py::_try_to_close_milestone_when_delete_us` | yes | CALLS | taiga/projects/userstories/signals.py:71 |  |  |
| 16 | `taiga/projects/utils.py::attach_extra_info` | `taiga/projects/utils.py::attach_notify_policies` | yes | CALLS | taiga/projects/utils.py:583 |  |  |
| 17 | `taiga/searches/services.py::_search_by_query` | `taiga/projects/userstories/utils.py::attach_total_points` | yes | CALLS | taiga/searches/services.py:84 |  |  |
| 18 | `taiga/timeline/timeline_implementations.py::epic_related_userstory_timeline` | `taiga/timeline/service.py::extract_userstory_info` | yes | CALLS | taiga/timeline/timeline_implementations.py:54 |  |  |
| 19 | `tests/integration/resources_permissions/test_auth_resources.py::test_auth_action_register_with_short_password` | `taiga/base/utils/json.py::dumps` | yes | CALLS | tests/integration/resources_permissions/test_auth_resources.py:70 |  |  |
| 20 | `tests/integration/resources_permissions/test_history_resources.py::test_wiki_action_edit_comment` | `tests/utils.py::helper_test_http_method` | yes | CALLS | tests/integration/resources_permissions/test_history_resources.py:1124 |  |  |
| 21 | `tests/integration/resources_permissions/test_projects_choices_resources.py::test_issue_type_action_bulk_update_order` | `tests/utils.py::helper_test_http_method` | yes | CALLS | tests/integration/resources_permissions/test_projects_choices_resources.py:1803 |  |  |
| 22 | `tests/integration/resources_permissions/test_userstories_custom_attributes_resource.py::test_userstory_custom_attribute_patch` | `tests/utils.py::helper_test_http_method` | yes | CALLS | tests/integration/resources_permissions/test_userstories_custom_attributes_resource.py:297 |  |  |
| 23 | `tests/integration/test_projects.py::test_project_transfer_reject_from_no_admin_member_with_valid_token` | `taiga/base/utils/json.py::dumps` | yes | CALLS | tests/integration/test_projects.py:1064 |  |  |
| 24 | `tests/integration/test_projects.py::test_project_transfer_validate_token_from_member_with_invalid_token` | `taiga/base/utils/json.py::dumps` | yes | CALLS | tests/integration/test_projects.py:1375 |  |  |
| 25 | `tests/unit/auth/test_token_denylist.py::test_tokens_can_be_manually_denylisted` | `taiga/auth/tokens.py::DenylistMixin.denylist` | yes | CALLS | tests/unit/auth/test_token_denylist.py:137 |  |  |

