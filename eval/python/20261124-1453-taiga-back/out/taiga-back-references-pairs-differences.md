# taiga-back (python): REFERENCES, graph v2 against dev

Engines: v2 `5a6074642e06`, dev `25ae40bf8662`. No oracle: you judge each row.

## Counts

v2 2826 pairs, dev 5711 pairs (dev types: HAS_TYPE 1945, USES_FIXTURE 1798, ACCEPTS 1305, READS 398, RETURNS 215, USES 47, WRITES 3).
Both 422, only v2 2404, only dev 5289; agreement 5.2% of the union.
Pairs are matched on (file, name with only letters and digits) of both ends, so the engines' different spellings of one test or scope meet; an edge to a route, data or package node (v2) has no dev counterpart. v2 unresolved and external edges are left out.

Verdict: `confirmed` (the group is right), `v2 wrong`, `dev wrong`, `both wrong`, or `?`. Cause: one short phrase.

## Only v2 has it (25 of 2404)
<!-- group: only_v2 -->

v2 has this edge, dev does not. Check: is the edge real in the code (v2 gain) or wrong (v2 wrong)?

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|
| 1 | `settings/common.py` | `settings/common.py::THN_ATTACHMENT_CARD` | yes | no | settings/common.py:560 |  |  |
| 2 | `taiga/export_import/api.py::ProjectImporterViewSet.issue` | `taiga/projects/issues/models.py::Issue` | yes | no | taiga/export_import/api.py:272 |  |  |
| 3 | `taiga/export_import/services/store.py::store_issue` | `taiga/export_import/validators/validators.py::IssueCustomAttributesValuesExportValidator` | yes | no | taiga/export_import/services/store.py:665 |  |  |
| 4 | `taiga/front/sitemaps/__init__.py` | `taiga/front/sitemaps/issues.py::IssuesSitemap` | yes | no | taiga/front/sitemaps/__init__.py:46 |  |  |
| 5 | `taiga/hooks/gitlab/api.py::GitLabViewSet` | `taiga/hooks/gitlab/event_hooks.py::PushEventHook` | yes | no | taiga/hooks/gitlab/api.py:24 |  |  |
| 6 | `taiga/importers/jira/common.py::JiraImporterCommon._create_custom_fields` | `taiga/projects/custom_attributes/models.py::UserStoryCustomAttribute` | yes | no | taiga/importers/jira/common.py:222 |  |  |
| 7 | `taiga/projects/admin.py` | `taiga/projects/models.py::Membership` | yes | no | taiga/projects/admin.py:313 |  |  |
| 8 | `taiga/projects/api.py::ProjectViewSet` | `taiga/projects/validators.py::ProjectValidator` | yes | no | taiga/projects/api.py:69 |  |  |
| 9 | `taiga/projects/attachments/api.py::EpicAttachmentViewSet` | `taiga/base/filters.py::CanViewEpicAttachmentFilterBackend` | yes | no | taiga/projects/attachments/api.py:109 |  |  |
| 10 | `taiga/projects/custom_attributes/api.py::TaskCustomAttributesValuesViewSet` | `taiga/projects/custom_attributes/models.py::TaskCustomAttributesValues` | yes | no | taiga/projects/custom_attributes/api.py:116 |  |  |
| 11 | `taiga/projects/notifications/signals.py::on_mentions` | `taiga/projects/notifications/choices.py::WebNotificationType.mentioned` | yes | no | taiga/projects/notifications/signals.py:102 |  |  |
| 12 | `taiga/projects/settings/api.py::UserProjectSettingsViewSet` | `taiga/projects/settings/validators.py::UserProjectSettingsValidator` | yes | no | taiga/projects/settings/api.py:26 |  |  |
| 13 | `taiga/projects/userstories/api.py::UserStoryViewSet` | `taiga/base/filters.py::MilestoneEstimatedStartFilter` | yes | no | taiga/projects/userstories/api.py:71 |  |  |
| 14 | `taiga/routers.py` | `taiga/projects/issues/api.py::IssueWatchersViewSet` | yes | no | taiga/routers.py:212 |  |  |
| 15 | `taiga/users/admin.py::UserAdmin` | `taiga/users/forms.py::UserChangeForm` | yes | no | taiga/users/admin.py:165 |  |  |
| 16 | `tests/integration/resources_permissions/test_attachment_resources.py::test_epic_attachment_patch` | `tests/integration/resources_permissions/test_attachment_resources.py::data_epic` | yes | no | tests/integration/resources_permissions/test_attachment_resources.py:484 |  |  |
| 17 | `tests/integration/resources_permissions/test_attachment_resources.py::test_user_story_attachment_retrieve` | `tests/integration/resources_permissions/test_attachment_resources.py::data` | yes | no | tests/integration/resources_permissions/test_attachment_resources.py:209 |  |  |
| 18 | `tests/integration/resources_permissions/test_users_resources.py::test_user_action_change_email` | `tests/integration/resources_permissions/test_users_resources.py::data` | yes | no | tests/integration/resources_permissions/test_users_resources.py:285 |  |  |
| 19 | `tests/integration/resources_permissions/test_users_resources.py::test_user_retrieve` | `tests/integration/resources_permissions/test_users_resources.py::data` | yes | no | tests/integration/resources_permissions/test_users_resources.py:45 |  |  |
| 20 | `tests/integration/test_hooks_gitlab.py::test_issues_event_opened_issue` | `taiga/projects/notifications/choices.py::NotifyLevel.all` | yes | no | tests/integration/test_hooks_gitlab.py:946 |  |  |
| 21 | `tests/integration/test_projects.py::test_edit_tag_only_color` | `tests/integration/test_feedback.py::user` | yes | no | tests/integration/test_projects.py:2001 |  |  |
| 22 | `tests/integration/test_tasks.py::test_api_create_in_bulk_with_status_milestone_userstory` | `tests/integration/test_feedback.py::user` | yes | no | tests/integration/test_tasks.py:160 |  |  |
| 23 | `tests/integration/test_users.py::test_get_voted_list_valid_info` | `tests/factories.py::UserStoryFactory` | yes | no | tests/integration/test_users.py:1162 |  |  |
| 24 | `tests/unit/auth/test_tokens.py::test_init_no_token_given` | `tests/unit/auth/test_tokens.py::MyToken.token_type` | yes | no | tests/unit/auth/test_tokens.py:104 |  |  |
| 25 | `tests/unit/test_attachments_services.py` | `tests/factories.py::WikiAttachmentFactory` | yes | no | tests/unit/test_attachments_services.py:47 |  |  |

## Only dev has it (25 of 5289)
<!-- group: only_dev -->

dev has this edge, v2 does not. Check: is it real (a v2 gap) or wrong (dev wrong)?

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|
| 1 | `taiga/export_import/api.py::ProjectImporterViewSet.load_dump` | `taiga/export_import/api.py::logger` | no | READS | - |  |  |
| 2 | `taiga/export_import/serializers/mixins.py::AttachmentExportSerializer.name` | `taiga/base/fields.py::Field` | no | HAS_TYPE | - |  |  |
| 3 | `taiga/export_import/serializers/serializers.py::EpicExportSerializer.related_user_stories` | `taiga/base/fields.py::MethodField` | no | HAS_TYPE | - |  |  |
| 4 | `taiga/export_import/serializers/serializers.py::ProjectExportSerializer.total_activity_last_year` | `taiga/base/fields.py::Field` | no | HAS_TYPE | - |  |  |
| 5 | `taiga/projects/models.py::TaskDueDate.order` | `taiga/base/api/fields.py::IntegerField` | no | HAS_TYPE | - |  |  |
| 6 | `taiga/projects/notifications/permissions.py::NotifyPolicyPermission.retrieve_perms` | `taiga/base/api/permissions.py::IsAuthenticated` | no | HAS_TYPE | - |  |  |
| 7 | `taiga/projects/permissions.py::EpicStatusPermission.update_perms` | `taiga/permissions/permissions.py::IsProjectAdmin` | no | HAS_TYPE | - |  |  |
| 8 | `taiga/projects/permissions.py::IssueStatusPermission.update_perms` | `taiga/permissions/permissions.py::IsProjectAdmin` | no | HAS_TYPE | - |  |  |
| 9 | `taiga/projects/permissions.py::SwimlanePermission.destroy_perms` | `taiga/permissions/permissions.py::IsProjectAdmin` | no | HAS_TYPE | - |  |  |
| 10 | `taiga/projects/serializers.py::MembershipAdminSerializer.user_email` | `taiga/base/fields.py::MethodField` | no | HAS_TYPE | - |  |  |
| 11 | `taiga/projects/userstories/api.py::UserStoryViewSet.filters_data` | `taiga/base/response.py::Ok` | no | RETURNS | - |  |  |
| 12 | `taiga/webhooks/serializers.py::TaskSerializer.milestone` | `taiga/webhooks/serializers.py::MilestoneSerializer` | no | HAS_TYPE | - |  |  |
| 13 | `taiga/webhooks/serializers.py::WebhookSerializer.id` | `taiga/base/fields.py::Field` | no | HAS_TYPE | - |  |  |
| 14 | `tests/integration/resources_permissions/test_attachment_resources.py::test_wiki_attachment_update` | `tests/fixtures.py::client` | no | USES_FIXTURE | - |  |  |
| 15 | `tests/integration/resources_permissions/test_issues_custom_attributes_resource.py::test_issue_custom_attributes_values_retrieve` | `tests/fixtures.py::client` | no | USES_FIXTURE | - |  |  |
| 16 | `tests/integration/resources_permissions/test_projects_choices_resources.py::test_user_story_status_retrieve` | `tests/integration/test_webhooks.py::data` | no | USES_FIXTURE | - |  |  |
| 17 | `tests/integration/resources_permissions/test_userstories_custom_attributes_resource.py::test_userstory_custom_attribute_delete` | `tests/fixtures.py::client` | no | USES_FIXTURE | - |  |  |
| 18 | `tests/integration/resources_permissions/test_userstories_custom_attributes_resource.py::test_userstory_custom_attribute_retrieve` | `tests/integration/test_webhooks.py::data` | no | USES_FIXTURE | - |  |  |
| 19 | `tests/integration/test_importer_api.py::test_invalid_project_import_with_extra_data` | `tests/fixtures.py::client` | no | USES_FIXTURE | - |  |  |
| 20 | `tests/integration/test_projects.py::test_private_project_can_be_public_because_owner_has_unlimited_slot_and_project_has_unlimited_members` | `tests/fixtures.py::client` | no | USES_FIXTURE | - |  |  |
| 21 | `tests/integration/test_projects.py::test_project_transfer_start_to_not_a_membership` | `tests/fixtures.py::client` | no | USES_FIXTURE | - |  |  |
| 22 | `tests/integration/test_users.py::test_users_by_username_throttling_api` | `tests/fixtures.py::client` | no | USES_FIXTURE | - |  |  |
| 23 | `tests/integration/test_userstories_update_kanban_order.py::test_api_update_orders_in_bulk_invalid_after_us_because_status` | `tests/fixtures.py::client` | no | USES_FIXTURE | - |  |  |
| 24 | `tests/integration/test_userstories_update_kanban_order.py::test_api_update_orders_in_bulk_invalid_before_us_because_project` | `tests/fixtures.py::client` | no | USES_FIXTURE | - |  |  |
| 25 | `tests/integration/test_watch_issues.py::test_list_issue_watchers` | `tests/fixtures.py::client` | no | USES_FIXTURE | - |  |  |

## Both have it (spot check) (25 of 422)
<!-- group: both -->

Both engines agree. Check a few: an agreement can still be wrong.

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|
| 1 | `taiga/base/middleware/cors.py::CorsMiddleware._populate_response` | `taiga/base/middleware/cors.py::CORS_ALLOWED_ORIGINS` | yes | READS | taiga/base/middleware/cors.py:38 |  |  |
| 2 | `taiga/hooks/gitlab/event_hooks.py::IssuesEventHook.ignore` | `taiga/hooks/event_hooks.py::ISSUE_ACTION_CLOSE` | yes | READS | taiga/hooks/gitlab/event_hooks.py:45 |  |  |
| 3 | `taiga/projects/history/services.py` | `taiga/projects/history/freeze_impl.py::task_freezer` | yes | USES | taiga/projects/history/services.py:476 |  |  |
| 4 | `taiga/projects/history/templatetags/functions.py::verbose_name` | `taiga/projects/history/templatetags/functions.py::EXTRA_FIELD_VERBOSE_NAMES` | yes | READS | taiga/projects/history/templatetags/functions.py:23 |  |  |
| 5 | `taiga/projects/management/commands/sample_data.py::Command.create_user` | `taiga/projects/management/commands/sample_data.py::COLOR_CHOICES` | yes | READS | taiga/projects/management/commands/sample_data.py:621 |  |  |
| 6 | `taiga/projects/notifications/squashing.py::is_squashable` | `taiga/projects/notifications/squashing.py::EXCLUDED_FIELDS` | yes | READS | taiga/projects/notifications/squashing.py:48 |  |  |
| 7 | `taiga/users/api.py::UsersViewSet.change_password` | `taiga/auth/settings.py::PASSWORD_MAX_LENGTH` | yes | READS | taiga/users/api.py:234 |  |  |
| 8 | `tests/integration/resources_permissions/test_history_resources.py::test_user_story_action_edit_comment` | `tests/integration/resources_permissions/test_history_resources.py::data_us` | yes | USES_FIXTURE | tests/integration/resources_permissions/test_history_resources.py:383 |  |  |
| 9 | `tests/integration/resources_permissions/test_history_resources.py::test_wiki_action_edit_comment` | `tests/integration/resources_permissions/test_history_resources.py::data_wiki` | yes | USES_FIXTURE | tests/integration/resources_permissions/test_history_resources.py:1100 |  |  |
| 10 | `tests/integration/resources_permissions/test_history_resources.py::test_wiki_history_retrieve` | `tests/integration/resources_permissions/test_history_resources.py::data_wiki` | yes | USES_FIXTURE | tests/integration/resources_permissions/test_history_resources.py:1079 |  |  |
| 11 | `tests/integration/test_hooks_gitlab.py::test_issues_event_closed_issue_conected_with_external_one_with_close_status_defined` | `tests/integration/test_hooks_gitlab.py::close_issue_base_payload` | yes | READS | tests/integration/test_hooks_gitlab.py:1187 |  |  |
| 12 | `tests/integration/test_hooks_gitlab.py::test_issues_event_updated_issue_connected_with_external_one` | `tests/integration/test_hooks_gitlab.py::edit_issue_base_payload` | yes | READS | tests/integration/test_hooks_gitlab.py:1008 |  |  |
| 13 | `tests/integration/test_hooks_gitlab.py::test_issues_event_updated_issue_without_connection` | `tests/integration/test_hooks_gitlab.py::edit_issue_base_payload` | yes | READS | tests/integration/test_hooks_gitlab.py:1044 |  |  |
| 14 | `tests/integration/test_issues.py::test_api_validator_assigned_to_when_update_issues` | `taiga/permissions/choices.py::MEMBERS_PERMISSIONS` | yes | READS | tests/integration/test_issues.py:669 |  |  |
| 15 | `tests/integration/test_searches.py::test_search_text_query_with_an_invalid_project_id` | `tests/integration/test_searches.py::searches_initial_data` | yes | USES_FIXTURE | tests/integration/test_searches.py:136 |  |  |
| 16 | `tests/integration/test_tasks.py::test_api_validator_assigned_to_when_update_tasks` | `taiga/permissions/choices.py::MEMBERS_PERMISSIONS` | yes | READS | tests/integration/test_tasks.py:998 |  |  |
| 17 | `tests/integration/test_watch_projects.py::test_get_project_is_watcher` | `taiga/permissions/choices.py::ANON_PERMISSIONS` | yes | READS | tests/integration/test_watch_projects.py:120 |  |  |
| 18 | `tests/unit/auth/test_backends.py::test_decode_hmac_with_expiry` | `tests/unit/auth/test_backends.py::SECRET` | yes | READS | tests/unit/auth/test_backends.py:186 |  |  |
| 19 | `tests/unit/auth/test_backends.py::test_decode_rsa_with_expiry` | `tests/unit/auth/test_backends.py::payload` | yes | READS | tests/unit/auth/test_backends.py:245 |  |  |
| 20 | `tests/unit/auth/test_tokens.py::test_delitem` | `tests/unit/auth/test_tokens.py::token` | yes | USES_FIXTURE | tests/unit/auth/test_tokens.py:239 |  |  |
| 21 | `tests/unit/test_mdrender.py::test_cache_by_sha` | `tests/unit/test_mdrender.py::dummy_project` | yes | READS | tests/unit/test_mdrender.py:266 |  |  |
| 22 | `tests/unit/test_mdrender.py::test_render_attachment_image` | `tests/unit/test_mdrender.py::dummy_project` | yes | READS | tests/unit/test_mdrender.py:313 |  |  |
| 23 | `tests/unit/test_mdrender.py::test_render_reference_links` | `tests/unit/test_mdrender.py::dummy_project` | yes | READS | tests/unit/test_mdrender.py:193 |  |  |
| 24 | `tests/unit/test_mdrender.py::test_render_relative_image` | `tests/unit/test_mdrender.py::dummy_project` | yes | READS | tests/unit/test_mdrender.py:243 |  |  |
| 25 | `tests/unit/test_mdrender.py::test_render_url_autolinks_with_https` | `tests/unit/test_mdrender.py::dummy_project` | yes | READS | tests/unit/test_mdrender.py:217 |  |  |

