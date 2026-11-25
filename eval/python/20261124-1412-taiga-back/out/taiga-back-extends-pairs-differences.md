# taiga-back (python): EXTENDS, graph v2 against dev

Engines: v2 `4e50b002a213`, dev `25ae40bf8662`. No oracle: you judge each row.

## Counts

v2 1288 pairs, dev 997 pairs (dev types: EXTENDS 873, OVERRIDES 124).
Both 938, only v2 350, only dev 59; agreement 69.6% of the union.
Pairs are matched on (file, name with only letters and digits) of both ends, so the engines' different spellings of one test or scope meet; an edge to a route, data or package node (v2) has no dev counterpart. v2 unresolved and external edges are left out.

Verdict: `confirmed` (the group is right), `v2 wrong`, `dev wrong`, `both wrong`, or `?`. Cause: one short phrase.

## Only v2 has it (25 of 350)
<!-- group: only_v2 -->

v2 has this edge, dev does not. Check: is the edge real in the code (v2 gain) or wrong (v2 wrong)?

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|
| 1 | `taiga/base/api/fields.py::IntegerField.__init__` | `taiga/base/api/fields.py::WritableField.__init__` | yes | no | taiga/base/api/fields.py:874 |  |  |
| 2 | `taiga/base/api/fields.py::SlugField.__init__` | `taiga/base/api/fields.py::CharField.__init__` | yes | no | taiga/base/api/fields.py:543 |  |  |
| 3 | `taiga/base/api/generics.py::GenericAPIView` | `taiga/base/api/views.py::APIView` | yes | no | taiga/base/api/generics.py:45 |  |  |
| 4 | `taiga/base/api/generics.py::RetrieveAPIView` | `taiga/base/api/mixins.py::RetrieveModelMixin` | yes | no | taiga/base/api/generics.py:320 |  |  |
| 5 | `taiga/base/api/serializers.py::ModelSerializerOptions.__init__` | `taiga/base/api/serializers.py::SerializerOptions.__init__` | yes | no | taiga/base/api/serializers.py:696 |  |  |
| 6 | `taiga/base/api/validators.py::ModelValidator` | `taiga/base/api/serializers.py::ModelSerializer` | yes | no | taiga/base/api/validators.py:15 |  |  |
| 7 | `taiga/base/api/viewsets.py::ModelViewSet` | `taiga/base/api/mixins.py::DestroyModelMixin` | yes | no | taiga/base/api/viewsets.py:180 |  |  |
| 8 | `taiga/base/throttling.py::CommonThrottle` | `taiga/base/api/throttling.py::SimpleRateThrottle` | yes | no | taiga/base/throttling.py:55 |  |  |
| 9 | `taiga/base/throttling.py::SimpleRateThrottle` | `taiga/base/api/throttling.py::SimpleRateThrottle` | yes | no | taiga/base/throttling.py:188 |  |  |
| 10 | `taiga/export_import/validators/validators.py::EpicCustomAttributesValuesExportValidator.Meta` | `taiga/export_import/validators/validators.py::BaseCustomAttributesValuesExportValidator.Meta` | yes | no | taiga/export_import/validators/validators.py:198 |  |  |
| 11 | `taiga/importers/github/api.py::GithubImporterViewSet` | `taiga/base/api/viewsets.py::ViewSet` | yes | no | taiga/importers/github/api.py:25 |  |  |
| 12 | `taiga/projects/attachments/validators.py::AttachmentValidator` | `taiga/base/api/validators.py::ModelValidator` | yes | no | taiga/projects/attachments/validators.py:18 |  |  |
| 13 | `taiga/projects/contact/validators.py::ContactEntryValidator` | `taiga/base/api/validators.py::ModelValidator` | yes | no | taiga/projects/contact/validators.py:13 |  |  |
| 14 | `taiga/projects/custom_attributes/models.py::TaskCustomAttribute.Meta` | `taiga/projects/custom_attributes/models.py::AbstractCustomAttribute.Meta` | yes | no | taiga/projects/custom_attributes/models.py:74 |  |  |
| 15 | `taiga/projects/custom_attributes/validators.py::EpicCustomAttributesValuesValidator.Meta` | `taiga/projects/custom_attributes/validators.py::BaseCustomAttributesValuesValidator.Meta` | yes | no | taiga/projects/custom_attributes/validators.py:122 |  |  |
| 16 | `taiga/projects/issues/validators.py::_IssueMilestoneBulkValidator` | `taiga/base/api/validators.py::Validator` | yes | no | taiga/projects/issues/validators.py:44 |  |  |
| 17 | `taiga/projects/notifications/serializers.py::NotifyPolicySerializer` | `taiga/base/api/serializers.py::ModelSerializer` | yes | no | taiga/projects/notifications/serializers.py:19 |  |  |
| 18 | `taiga/projects/notifications/serializers.py::WebNotificationSerializer` | `taiga/base/api/serializers.py::ModelSerializer` | yes | no | taiga/projects/notifications/serializers.py:39 |  |  |
| 19 | `taiga/projects/tasks/validators.py::UpdateMilestoneBulkValidator` | `taiga/base/api/validators.py::Validator` | yes | no | taiga/projects/tasks/validators.py:154 |  |  |
| 20 | `taiga/projects/userstories/filters.py::AssignedUsersFilter` | `taiga/base/filters.py::BaseRelatedFieldsFilter` | yes | no | taiga/projects/userstories/filters.py:55 |  |  |
| 21 | `taiga/users/serializers.py::LikedObjectSerializer.__init__` | `taiga/users/serializers.py::HighLightedContentSerializer.__init__` | yes | no | taiga/users/serializers.py:231 |  |  |
| 22 | `taiga/users/throttling.py::UserUpdateRateThrottle` | `taiga/base/throttling.py::ThrottleByActionMixin` | yes | no | taiga/users/throttling.py:16 |  |  |
| 23 | `taiga/users/throttling.py::UserUpdateRateThrottle` | `taiga/base/throttling.py::UserRateThrottle` | yes | no | taiga/users/throttling.py:16 |  |  |
| 24 | `taiga/users/validators.py::CancelAccountValidator` | `taiga/base/api/validators.py::Validator` | yes | no | taiga/users/validators.py:91 |  |  |
| 25 | `taiga/users/validators.py::RoleValidator` | `taiga/base/api/validators.py::ModelValidator` | yes | no | taiga/users/validators.py:99 |  |  |

## Only dev has it (25 of 59)
<!-- group: only_dev -->

dev has this edge, v2 does not. Check: is it real (a v2 gap) or wrong (dev wrong)?

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|
| 1 | `taiga/base/api/relations.py::HyperlinkedIdentityField.field_to_native` | `taiga/base/api/fields.py::Field.field_to_native` | no | OVERRIDES | - |  |  |
| 2 | `taiga/base/api/relations.py::RelatedField.field_from_native` | `taiga/base/api/fields.py::WritableField.field_from_native` | no | OVERRIDES | - |  |  |
| 3 | `taiga/base/api/relations.py::RelatedField.field_to_native` | `taiga/base/api/fields.py::WritableField.field_to_native` | no | OVERRIDES | - |  |  |
| 4 | `taiga/base/api/relations.py::RelatedField.get_default_value` | `taiga/base/api/fields.py::WritableField.get_default_value` | no | OVERRIDES | - |  |  |
| 5 | `taiga/base/api/serializers.py::BaseSerializer.field_from_native` | `taiga/base/api/fields.py::WritableField.field_from_native` | no | OVERRIDES | - |  |  |
| 6 | `taiga/base/api/serializers.py::BaseSerializer.field_to_native` | `taiga/base/api/fields.py::WritableField.field_to_native` | no | OVERRIDES | - |  |  |
| 7 | `taiga/base/exceptions.py::PermissionDenied` | `taiga/base/exceptions.py::PermissionDenied` | no | EXTENDS | - |  |  |
| 8 | `taiga/export_import/validators/fields.py::HistorySnapshotField.from_native` | `taiga/base/fields.py::JSONField.from_native` | no | OVERRIDES | - |  |  |
| 9 | `taiga/export_import/validators/fields.py::HistoryValuesField.from_native` | `taiga/base/fields.py::JSONField.from_native` | no | OVERRIDES | - |  |  |
| 10 | `taiga/external_apps/auth_backends.py::Token.authenticate` | `taiga/base/api/authentication.py::BaseAuthentication.authenticate` | no | OVERRIDES | - |  |  |
| 11 | `taiga/external_apps/auth_backends.py::Token.authenticate_header` | `taiga/base/api/authentication.py::BaseAuthentication.authenticate_header` | no | OVERRIDES | - |  |  |
| 12 | `taiga/external_apps/permissions.py::CanUseToken.check_permissions` | `taiga/base/api/permissions.py::PermissionComponent.check_permissions` | no | OVERRIDES | - |  |  |
| 13 | `taiga/hooks/bitbucket/api.py::BitBucketViewSet._validate_signature` | `taiga/hooks/api.py::BaseWebhookApiViewSet._validate_signature` | no | OVERRIDES | - |  |  |
| 14 | `taiga/hooks/github/event_hooks.py::IssuesEventHook.get_data` | `taiga/hooks/event_hooks.py::BaseIssueEventHook.get_data` | no | OVERRIDES | - |  |  |
| 15 | `taiga/hooks/gitlab/api.py::GitLabViewSet._validate_signature` | `taiga/hooks/api.py::BaseWebhookApiViewSet._validate_signature` | no | OVERRIDES | - |  |  |
| 16 | `taiga/hooks/gitlab/event_hooks.py::IssuesEventHook.action_type` | `taiga/hooks/event_hooks.py::BaseIssueEventHook.action_type` | no | OVERRIDES | - |  |  |
| 17 | `taiga/hooks/gitlab/event_hooks.py::IssuesEventHook.get_data` | `taiga/hooks/event_hooks.py::BaseIssueEventHook.get_data` | no | OVERRIDES | - |  |  |
| 18 | `taiga/hooks/gogs/api.py::GogsViewSet._get_event_name` | `taiga/hooks/api.py::BaseWebhookApiViewSet._get_event_name` | no | OVERRIDES | - |  |  |
| 19 | `taiga/permissions/permissions.py::CommentAndOrUpdatePerm.check_permissions` | `taiga/base/api/permissions.py::PermissionComponent.check_permissions` | no | OVERRIDES | - |  |  |
| 20 | `taiga/permissions/permissions.py::HasProjectPerm.check_permissions` | `taiga/base/api/permissions.py::PermissionComponent.check_permissions` | no | OVERRIDES | - |  |  |
| 21 | `taiga/permissions/permissions.py::IsObjectOwner.check_permissions` | `taiga/base/api/permissions.py::PermissionComponent.check_permissions` | no | OVERRIDES | - |  |  |
| 22 | `taiga/projects/contact/permissions.py::IsContactActivated.check_permissions` | `taiga/base/api/permissions.py::PermissionComponent.check_permissions` | no | OVERRIDES | - |  |  |
| 23 | `taiga/users/permissions.py::IsTheSameUser.check_permissions` | `taiga/base/api/permissions.py::PermissionComponent.check_permissions` | no | OVERRIDES | - |  |  |
| 24 | `taiga/webhooks/permissions.py::IsWebhookProjectAdmin.check_permissions` | `taiga/base/api/permissions.py::PermissionComponent.check_permissions` | no | OVERRIDES | - |  |  |
| 25 | `tests/unit/auth/test_authentication.py::test_jwt_token_user_authentication_custom_tokenuser.<locals>.BobSaget.username` | `taiga/auth/models.py::TokenUser.username` | no | OVERRIDES | - |  |  |

## Both have it (spot check) (25 of 938)
<!-- group: both -->

Both engines agree. Check a few: an agreement can still be wrong.

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|
| 1 | `taiga/base/api/fields.py::DecimalField` | `taiga/base/api/fields.py::WritableField` | yes | EXTENDS | taiga/base/api/fields.py:915 |  |  |
| 2 | `taiga/base/api/fields.py::IntegerField` | `taiga/base/api/fields.py::WritableField` | yes | EXTENDS | taiga/base/api/fields.py:862 |  |  |
| 3 | `taiga/base/api/mixins.py::BlockeableSaveMixin` | `taiga/base/api/mixins.py::BlockeableModelMixin` | yes | EXTENDS | taiga/base/api/mixins.py:273 |  |  |
| 4 | `taiga/base/api/permissions.py::AllowAny` | `taiga/base/api/permissions.py::PermissionComponent` | yes | EXTENDS | taiga/base/api/permissions.py:143 |  |  |
| 5 | `taiga/base/api/relations.py::RelatedField` | `taiga/base/api/fields.py::WritableField` | yes | EXTENDS | taiga/base/api/relations.py:63 |  |  |
| 6 | `taiga/base/api/renderers.py::MultiPartRenderer.render` | `taiga/base/api/renderers.py::BaseRenderer.render` | yes | OVERRIDES | taiga/base/api/renderers.py:299 |  |  |
| 7 | `taiga/base/filters.py::CanViewUsFilterBackend` | `taiga/base/filters.py::PermissionBasedFilterBackend` | yes | EXTENDS | taiga/base/filters.py:199 |  |  |
| 8 | `taiga/export_import/api.py::ProjectImporterViewSet` | `taiga/base/api/viewsets.py::GenericViewSet` | yes | EXTENDS | taiga/export_import/api.py:84 |  |  |
| 9 | `taiga/export_import/serializers/serializers.py::EpicExportSerializer` | `taiga/export_import/serializers/mixins.py::WatcheableObjectLightSerializerMixin` | yes | EXTENDS | taiga/export_import/serializers/serializers.py:323 |  |  |
| 10 | `taiga/export_import/serializers/serializers.py::MilestoneExportSerializer` | `taiga/export_import/serializers/serializers.py::RelatedExportSerializer` | yes | EXTENDS | taiga/export_import/serializers/serializers.py:205 |  |  |
| 11 | `taiga/export_import/serializers/serializers.py::RolePointsExportSerializer` | `taiga/export_import/serializers/serializers.py::RelatedExportSerializer` | yes | EXTENDS | taiga/export_import/serializers/serializers.py:200 |  |  |
| 12 | `taiga/export_import/validators/validators.py::IssueCustomAttributesValuesExportValidator` | `taiga/export_import/validators/validators.py::BaseCustomAttributesValuesExportValidator` | yes | EXTENDS | taiga/export_import/validators/validators.py:219 |  |  |
| 13 | `taiga/external_apps/api.py::ApplicationToken` | `taiga/base/api/viewsets.py::ModelCrudViewSet` | yes | EXTENDS | taiga/external_apps/api.py:52 |  |  |
| 14 | `taiga/front/sitemaps/generics.py::GenericSitemap` | `taiga/front/sitemaps/base.py::Sitemap` | yes | EXTENDS | taiga/front/sitemaps/generics.py:16 |  |  |
| 15 | `taiga/projects/api.py::IssueTypeViewSet` | `taiga/projects/mixins/ordering.py::BulkUpdateOrderMixin` | yes | EXTENDS | taiga/projects/api.py:878 |  |  |
| 16 | `taiga/projects/contact/api.py::ContactViewSet` | `taiga/base/api/mixins.py::CreateModelMixin` | yes | EXTENDS | taiga/projects/contact/api.py:20 |  |  |
| 17 | `taiga/projects/custom_attributes/api.py::UserStoryCustomAttributeViewSet` | `taiga/base/api/mixins.py::ArchivedByProjectMixin` | yes | EXTENDS | taiga/projects/custom_attributes/api.py:41 |  |  |
| 18 | `taiga/projects/epics/validators.py::EpicValidator` | `taiga/projects/notifications/mixins.py::EditableWatchedResourceSerializer` | yes | EXTENDS | taiga/projects/epics/validators.py:31 |  |  |
| 19 | `taiga/projects/history/permissions.py::EpicHistoryPermission` | `taiga/base/api/permissions.py::TaigaResourcePermission` | yes | EXTENDS | taiga/projects/history/permissions.py:34 |  |  |
| 20 | `taiga/projects/issues/permissions.py::IssueVotersPermission` | `taiga/base/api/permissions.py::TaigaResourcePermission` | yes | EXTENDS | taiga/projects/issues/permissions.py:36 |  |  |
| 21 | `taiga/projects/permissions.py::IssueDueDatePermission` | `taiga/base/api/permissions.py::TaigaResourcePermission` | yes | EXTENDS | taiga/projects/permissions.py:235 |  |  |
| 22 | `taiga/projects/tasks/api.py::TaskViewSet` | `taiga/projects/notifications/mixins.py::AssignedToSignalMixin` | yes | EXTENDS | taiga/projects/tasks/api.py:40 |  |  |
| 23 | `taiga/projects/userstories/serializers.py::UserStoryNestedSerializer` | `taiga/projects/mixins/serializers.py::ProjectExtraInfoSerializerMixin` | yes | EXTENDS | taiga/projects/userstories/serializers.py:192 |  |  |
| 24 | `taiga/projects/wiki/validators.py::WikiPageValidator` | `taiga/projects/notifications/validators.py::WatchersValidator` | yes | EXTENDS | taiga/projects/wiki/validators.py:15 |  |  |
| 25 | `tests/factories.py::EpicFactory` | `tests/factories.py::Factory` | yes | EXTENDS | tests/factories.py:262 |  |  |

