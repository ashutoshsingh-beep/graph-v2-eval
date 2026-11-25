# taiga-back (python): graph differences to verify

Repo `https://github.com/taigaio/taiga-back` at `8ab6a4e3b5f6fbbfcbf108a6449011f07b7308aa`. Old engine `25ae40bf8662`, graph v2 `b3cd5e698314`.

## Status

Fill this in. `graph-eval.sh report` reads it, and the next run copies it forward.

- intern: 
- stage: not started   (not started | verifying | grouping patterns | done)
- language version: (auto)   write a value here to correct the detected one
- framework: (auto)   write a value here to correct the detected one
- next: 
- blocked by: 
- issues filed: 

## Counts

In-repo calls found by the oracle: 12573. Both right 4415, gap 480, v2 gain 7027, both miss 651.
Scored edges: v2 12343 (716 wrong), dev 5485 (388 wrong). Not scored: v2 149, dev 2079.
CALLS recall: dev 38.9% (4895/12573), v2 91.0% (11442/12573). CALLS precision: dev 92.9% (5097/5485), v2 94.2% (11627/12343).
Line precision judges each engine only on lines where the oracle has a call it can map, and counts edges that sit on no oracle call (decorator lines) as wrong. Do not rank the engines on it alone.
v2 precision at exact call sites (published): 0.9916.
Flags: {"def_line_both_miss": 9, "dev_multi_both_right": 523, "dev_multi_gap": 70} (def_line_* = the line defines a function of the target's own name, usually the oracle's mistake; dev_multi_* = dev was right but had several targets on the line).
Scorer notes: {"dev_edges_with_file_source_never_scored": 131, "dev_calls_without_site_line": 0}.
Check against the published scores: OK (full).

## How each v2 miss happened

| group | v2 miss | reason | calls |
|---|---|---|---|
| both_miss | reported | dynamic_dispatch | 510 |
| gap | reported | dynamic_dispatch | 313 |
| gap | silent | - | 145 |
| both_miss | wrong_target | - | 100 |
| both_miss | reported | many_candidates | 23 |
| gap | reported | no_candidate | 18 |
| both_miss | silent | - | 11 |
| both_miss | reported | no_candidate | 5 |
| gap | reported | many_candidates | 3 |
| both_miss | no_node | - | 2 |
| gap | wrong_target | - | 1 |

`no_node`: v2 has no node for the target. `wrong_target`: v2 resolved this call to another target. `external`: v2 called it external. `reported`: only unresolved edges, with v2's reason. `silent`: no v2 edge at this call at all.

Verdict: `confirmed` (the row is what its group says), `oracle wrong`, `dev wrong`, `v2 right after all`, or `?`.
Cause: one short phrase for the code shape (for example `method on a constructor-injected field`). Reuse phrases.
Reason true: for a `reported` miss, `yes` or `no`.

## Gaps: dev is right, v2 is not (25 of 480)
<!-- kind: gap -->

What v2 loses against the old engine. Check: is the oracle target right, does dev's edge really go there, and is v2 really wrong?

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `taiga/auth/backends.py:91` | `raise TokenBackendError(format_lazy(_("Unrecognized algorithm type '{}'"), algorithm))` | taiga/auth/utils.py:59 format_lazy(). | class::taiga/auth/exceptions.py::TokenBackendError; function::taiga/auth/utils.py::format_lazy | unresolved unresolved::python::format_lazy | reported (many_candidates); dev has 2 targets on this line |  |  |  |
| 2 | `taiga/auth/tokens.py:178` | `raise TokenError(format_lazy(_("Token has no '{}' claim"), claim))` | taiga/auth/utils.py:59 format_lazy(). | class::taiga/auth/exceptions.py::TokenError; function::taiga/auth/utils.py::format_lazy | unresolved unresolved::python::format_lazy | reported (many_candidates); dev has 2 targets on this line |  |  |  |
| 3 | `taiga/base/api/fields.py:876` | `super(IntegerField, self).__init__(*args, **kwargs)` | taiga/base/api/fields.py:289 WritableField#__init__(). | class::taiga/base/api/fields.py::IntegerField; method::taiga/base/api/fields.py::WritableField::__init__ | unresolved unresolved::python::super().__init__ | reported (dynamic_dispatch); dev has 2 targets on this line |  |  |  |
| 4 | `taiga/base/api/renderers.py:172` | `json = super(JSONPRenderer, self).render(data, accepted_media_type,` | taiga/base/api/renderers.py:102 JSONRenderer#render(). | class::taiga/base/api/renderers.py::JSONPRenderer; method::taiga/base/api/renderers.py::JSONRenderer::render | unresolved unresolved::python::super().render | reported (dynamic_dispatch); dev has 2 targets on this line |  |  |  |
| 5 | `taiga/base/api/utils/formatting.py:106` | `description = apply_markdown(description)` | taiga/base/api/utils/formatting.py:49 apply_markdown(). | function::taiga/base/api/utils/formatting.py::apply_markdown | unresolved unresolved::python::apply_markdown | reported (many_candidates) |  |  |  |
| 6 | `taiga/base/api/views.py:391` | `response.renderer_context = self.get_renderer_context()` | taiga/base/api/views.py:209 APIView#get_renderer_context(). | method::taiga/base/api/views.py::APIView::get_renderer_context | unresolved unresolved::python::self.get_renderer_context | reported (dynamic_dispatch) |  |  |  |
| 7 | `taiga/base/filters.py:646` | `return FilterBackend.filter_queryset(self, request, queryset, view)` | taiga/base/filters.py:102 OrderByFilterMixin#filter_queryset(). | method::taiga/base/filters.py::BaseCompareFilter::filter_queryset; method::taiga/base/filters.py::BaseRelatedFieldsFilter::filter_queryset; method::taiga/base/filters.py::IsProjectAdminFilterBackend::filter_queryset; method::taiga/base/filters.py::IsProjectAdminFromWebhookLogFilterBackend::filter_queryset; method::taiga/base/filters.py::MembersFilterBackend::filter_queryset; method::taiga/base/filters.py::OrderByFilterMixin::filter_queryset; method::taiga/base/filters.py::PermissionBasedAttachmentFilterBackend::filter_queryset; method::taiga/base/filters.py::PermissionBasedFilterBackend::filter_queryset; method::taiga/base/filters.py::QFilter::filter_queryset; method::taiga/base/filters.py::TagsFilter::filter_queryset; method::taiga/base/filters.py::WatchersFilter::filter_queryset; method::taiga/projects/filters.py::CanViewProjectObjFilterBackend::filter_queryset; method::taiga/projects/filters.py::DiscoverModeFilterBackend::filter_queryset; method::taiga/projects/filters.py::QFilterBackend::filter_queryset; method::taiga/projects/filters.py::UserOrderFilterBackend::filter_queryset; method::taiga/projects/userstories/filters.py::DashboardFilter::filter_queryset; method::taiga/projects/userstories/filters.py::UserStoriesRoleFilter::filter_queryset; method::taiga/projects/userstories/filters.py::UserStoryStatusesFilter::filter_queryset; method::taiga/users/filters.py::ContactsFilterBackend::filter_queryset; method::taiga/userstorage/filters.py::StorageEntriesFilterBackend::filter_queryset | unresolved unresolved::python::FilterBackend.filter_queryset | reported (no_candidate); dev has 20 targets on this line |  |  |  |
| 8 | `taiga/base/neighbors.py:97` | `left, right = get_neighbors(obj, results_set=queryset)` | taiga/base/neighbors.py:19 get_neighbors(). | function::taiga/base/neighbors.py::get_neighbors | name python::.::taiga/base/neighbors.py::taiga/base/neighbors/NeighborsSerializerMixin#get_nei… | wrong_target |  |  |  |
| 9 | `taiga/base/routers.py:288` | `return APIRoot.as_view()` | taiga/base/api/views.py:139 APIView#as_view(). | method::taiga/base/api/views.py::APIView::as_view | unresolved unresolved::python::APIRoot.as_view | reported (no_candidate) |  |  |  |
| 10 | `taiga/export_import/serializers/fields.py:86` | `return (UserRelatedField().to_value(user), obj['name'])` | taiga/export_import/serializers/fields.py:52 UserRelatedField#to_value(). | class::taiga/export_import/serializers/fields.py::UserRelatedField; method::taiga/export_import/serializers/fields.py::UserRelatedField::to_value | unresolved unresolved::python::UserRelatedField().to_value | reported (dynamic_dispatch); dev has 2 targets on this line |  |  |  |
| 11 | `taiga/hooks/event_hooks.py:82` | `if self.ignore():` | taiga/hooks/event_hooks.py:46 BaseEventHook#ignore(). | method::taiga/hooks/event_hooks.py::BaseEventHook::ignore | unresolved unresolved::python::self.ignore | reported (dynamic_dispatch) |  |  |  |
| 12 | `taiga/importers/management/commands/import_from_jira.py:51` | `(rtoken, rtoken_secret, url) = JiraNormalImporter.get_auth_url(` | taiga/importers/jira/common.py:727 JiraImporterCommon#get_auth_url(). | method::taiga/importers/jira/common.py::JiraImporterCommon::get_auth_url | unresolved unresolved::python::JiraNormalImporter.get_auth_url | reported (no_candidate) |  |  |  |
| 13 | `taiga/projects/api.py:200` | `serializer = self.get_serializer(self.object)` | taiga/base/api/generics.py:92 GenericAPIView#get_serializer(). | method::taiga/base/api/generics.py::GenericAPIView::get_serializer | unresolved unresolved::python::self.get_serializer | reported (dynamic_dispatch) |  |  |  |
| 14 | `taiga/projects/api.py:322` | `@detail_route(methods=["POST"])` | taiga/base/decorators.py:11 detail_route(). | function::taiga/base/decorators.py::detail_route | import python::.::taiga/base/decorators.py::taiga/base/decorators/detail_route().decorator().#ff… | silent |  |  |  |
| 15 | `taiga/projects/api.py:424` | `@detail_route(methods=["POST"])` | taiga/base/decorators.py:11 detail_route(). | function::taiga/base/decorators.py::detail_route | import python::.::taiga/base/decorators.py::taiga/base/decorators/detail_route().decorator().#ff… | silent |  |  |  |
| 16 | `taiga/projects/api.py:1047` | `@list_route(methods=["POST"])` | taiga/base/decorators.py:24 list_route(). | function::taiga/base/decorators.py::list_route | import python::.::taiga/base/decorators.py::taiga/base/decorators/list_route().decorator().#ff92… | silent |  |  |  |
| 17 | `taiga/projects/history/api.py:156` | `@detail_route(methods=['post'])` | taiga/base/decorators.py:11 detail_route(). | function::taiga/base/decorators.py::detail_route | import python::.::taiga/base/decorators.py::taiga/base/decorators/detail_route().decorator().#ff… | silent |  |  |  |
| 18 | `taiga/users/api.py:317` | `@list_route(methods=["GET"])` | taiga/base/decorators.py:24 list_route(). | function::taiga/base/decorators.py::list_route | import python::.::taiga/base/decorators.py::taiga/base/decorators/list_route().decorator().#ff92… | silent |  |  |  |
| 19 | `tests/integration/test_importers_trello_api.py:181` | `response = client.post(url, content_type="application/json", data=json.dumps({"token": "token"}))` | taiga/base/utils/json.py:15 dumps(). | function::taiga/base/utils/json.py::dumps | unresolved unresolved::python::json.dumps | reported (dynamic_dispatch) |  |  |  |
| 20 | `tests/integration/test_users.py:655` | `cancel_token = CancelToken.for_user(user)` | taiga/auth/tokens.py:185 Token#for_user(). | method::taiga/auth/tokens.py::Token::for_user | unresolved unresolved::python::CancelToken.for_user | reported (no_candidate) |  |  |  |
| 21 | `tests/unit/auth/test_token_denylist.py:75` | `AccessToken.for_user(user)` | taiga/auth/tokens.py:185 Token#for_user(). | method::taiga/auth/tokens.py::Token::for_user | unresolved unresolved::python::AccessToken.for_user | reported (no_candidate) |  |  |  |
| 22 | `tests/unit/auth/test_token_denylist.py:87` | `token = RefreshToken.for_user(user)` | taiga/auth/tokens.py:247 DenylistMixin#for_user(). | method::taiga/auth/tokens.py::DenylistMixin::for_user | unresolved unresolved::python::RefreshToken.for_user | reported (no_candidate) |  |  |  |
| 23 | `tests/unit/auth/test_token_denylist.py:150` | `not_expired_1 = RefreshToken.for_user(user)` | taiga/auth/tokens.py:247 DenylistMixin#for_user(). | method::taiga/auth/tokens.py::DenylistMixin::for_user | unresolved unresolved::python::RefreshToken.for_user | reported (no_candidate) |  |  |  |
| 24 | `tests/unit/test_notifications_squashing.py:36` | `assert_(history_entries, squashed)` | tests/unit/test_notifications_squashing.py:11 assert_(). | function::tests/unit/test_notifications_squashing.py::assert_ | no edge | silent |  |  |  |
| 25 | `tests/unit/test_notifications_squashing.py:106` | `assert_(expected, squashed, ordered=False)` | tests/unit/test_notifications_squashing.py:11 assert_(). | function::tests/unit/test_notifications_squashing.py::assert_ | no edge | silent |  |  |  |

## Wrong v2 edges (25 of 716)
<!-- kind: v2_wrong -->

A v2 edge on a line where the oracle has a call, whose target is none of that line's oracle targets. `at call site: no` means the edge sits on no call the oracle saw (for example a decorator line). Check: is v2's target wrong?

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `taiga/base/api/serializers.py:977` | `return ModelField(model_field=model_field, **kwargs)` | taiga/base/api/fields.py:495 CharField# | class::taiga/base/api/fields.py::ModelField; method::taiga/base/api/fields.py::ModelField::__init__ | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/ModelField#__init__().#5a0c25fb (at call site: no) |  |  |  |  |
| 2 | `taiga/export_import/validators/validators.py:127` | `modified_date = serializers.DateTimeField(required=False)` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/DateTimeField# (at call site: yes) |  |  |  |  |
| 3 | `taiga/export_import/validators/validators.py:251` | `modified_date = serializers.DateTimeField(required=False)` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/DateTimeField# (at call site: yes) |  |  |  |  |
| 4 | `taiga/export_import/validators/validators.py:321` | `modified_date = serializers.DateTimeField(required=False)` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/DateTimeField# (at call site: yes) |  |  |  |  |
| 5 | `taiga/export_import/validators/validators.py:370` | `due_date = serializers.DateTimeField(required=False)` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/DateTimeField#__init__().#9bbf… (at call site: no) |  |  |  |  |
| 6 | `taiga/export_import/validators/validators.py:385` | `modified_date = serializers.DateTimeField(required=False)` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/DateTimeField# (at call site: yes) |  |  |  |  |
| 7 | `taiga/export_import/validators/validators.py:431` | `default_issue_type = serializers.SlugRelatedField(slug_field="name", required=False)` | taiga/base/api/fields.py:276 WritableField# | no edge | import python::.::taiga/base/api/relations.py::taiga/base/api/relations/SlugRelatedField# (at call site: yes) |  |  |  |  |
| 8 | `taiga/projects/epics/api.py:180` | `@list_route(methods=["POST"])` | taiga/base/decorators.py:24 list_route(). | function::taiga/base/decorators.py::list_route | import python::.::taiga/base/decorators.py::taiga/base/decorators/list_route().decorator().#ff92… (at call site: no) |  |  |  |  |
| 9 | `taiga/projects/issues/api.py:224` | `@list_route(methods=["POST"])` | taiga/base/decorators.py:24 list_route(). | function::taiga/base/decorators.py::list_route | import python::.::taiga/base/decorators.py::taiga/base/decorators/list_route().decorator().#ff92… (at call site: no) |  |  |  |  |
| 10 | `taiga/projects/issues/validators.py:49` | `project_id = serializers.IntegerField()` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/IntegerField# (at call site: yes) |  |  |  |  |
| 11 | `taiga/projects/milestones/api.py:183` | `@detail_route(methods=["POST"])` | taiga/base/decorators.py:11 detail_route(). | function::taiga/base/decorators.py::detail_route | import python::.::taiga/base/decorators.py::taiga/base/decorators/detail_route().decorator().#ff… (at call site: no) |  |  |  |  |
| 12 | `taiga/projects/tagging/api.py:30` | `validator = validators.CreateTagValidator(data=request.DATA, project=project)` | taiga/projects/tagging/validators.py:29 CreateTagValidator# | no edge | name python::.::taiga/projects/tagging/validators.py::taiga/projects/tagging/validators/Projec… (at call site: no) |  |  |  |  |
| 13 | `taiga/projects/tasks/api.py:255` | `raise exc.Blocked(_("Blocked element"))` | taiga/base/exceptions.py:195 Blocked# | no edge | name python::.::taiga/base/exceptions.py::taiga/base/exceptions/APIException#__init__().#7c91f… (at call site: no) |  |  |  |  |
| 14 | `taiga/projects/tasks/api.py:297` | `raise exc.Blocked(_("Blocked element"))` | taiga/base/exceptions.py:195 Blocked# | no edge | name python::.::taiga/base/exceptions.py::taiga/base/exceptions/APIException#__init__().#7c91f… (at call site: no) |  |  |  |  |
| 15 | `taiga/projects/tasks/validators.py:37` | `project_id = serializers.IntegerField()` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/IntegerField# (at call site: yes) |  |  |  |  |
| 16 | `taiga/projects/tasks/validators.py:82` | `task_id = serializers.IntegerField()` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/IntegerField# (at call site: yes) |  |  |  |  |
| 17 | `taiga/projects/tasks/validators.py:90` | `milestone_id = serializers.IntegerField(required=False)` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/IntegerField# (at call site: yes) |  |  |  |  |
| 18 | `taiga/projects/tasks/validators.py:156` | `milestone_id = serializers.IntegerField()` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/IntegerField# (at call site: yes) |  |  |  |  |
| 19 | `taiga/projects/userstories/api.py:385` | `@list_route(methods=["POST"])` | taiga/base/decorators.py:24 list_route(). | function::taiga/base/decorators.py::list_route | import python::.::taiga/base/decorators.py::taiga/base/decorators/list_route().decorator().#ff92… (at call site: no) |  |  |  |  |
| 20 | `taiga/projects/userstories/validators.py:171` | `status_id = serializers.IntegerField()` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/IntegerField# (at call site: yes) |  |  |  |  |
| 21 | `taiga/projects/userstories/validators.py:259` | `us_id = serializers.IntegerField()` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/IntegerField# (at call site: yes) |  |  |  |  |
| 22 | `taiga/users/api.py:157` | `@list_route(methods=["POST"])` | taiga/base/decorators.py:24 list_route(). | function::taiga/base/decorators.py::list_route | import python::.::taiga/base/decorators.py::taiga/base/decorators/list_route().decorator().#ff92… (at call site: no) |  |  |  |  |
| 23 | `tests/integration/test_hooks_bitbucket.py:385` | `ev_hook = event_hooks.PushEventHook(issue.project, payload)` | taiga/hooks/bitbucket/event_hooks.py:64 PushEventHook# | no edge | name python::.::taiga/hooks/event_hooks.py::taiga/hooks/event_hooks/BaseEventHook#__init__().#… (at call site: no) |  |  |  |  |
| 24 | `tests/integration/test_hooks_bitbucket.py:814` | `ev_hook = event_hooks.IssueCommentEventHook(issue.project, payload)` | taiga/hooks/bitbucket/event_hooks.py:46 IssueCommentEventHook# | no edge | name python::.::taiga/hooks/event_hooks.py::taiga/hooks/event_hooks/BaseEventHook#__init__().#… (at call site: no) |  |  |  |  |
| 25 | `tests/integration/test_hooks_github.py:169` | `ev_hook = event_hooks.PushEventHook(task.project, payload)` | taiga/hooks/github/event_hooks.py:83 PushEventHook# | no edge | name python::.::taiga/hooks/event_hooks.py::taiga/hooks/event_hooks/BaseEventHook#__init__().#… (at call site: no) |  |  |  |  |

## v2 gains: v2 is right, dev is not (25 of 7027)
<!-- kind: v2_gain -->

What v2 adds. Verify a few so the gain is real.

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `taiga/export_import/services/store.py:144` | `validator.save()` | taiga/base/api/serializers.py:1097 ModelSerializer#save(). | no edge | import python::.::taiga/base/api/serializers.py::taiga/base/api/serializers/ModelSerializer#save… |  |  |  |  |
| 2 | `taiga/mdrender/service.py:172` | `text = _sanitize_text(data)` | taiga/mdrender/service.py:142 DiffMatchPatch#_sanitize_text(). | no edge | name python::.::taiga/mdrender/service.py::taiga/mdrender/service/DiffMatchPatch#diff_pretty_h… | dev has no node for the target |  |  |  |
| 3 | `taiga/mdrender/service.py:175` | `text = _split_long_text(_sanitize_text(data), idx, size)` | taiga/mdrender/service.py:146 DiffMatchPatch#_split_long_text(). | function::taiga/mdrender/service.py::DiffMatchPatch.diff_pretty_html.<locals>._split_long… | name python::.::taiga/mdrender/service.py::taiga/mdrender/service/DiffMatchPatch#diff_pretty_h… | dev has no node for the target |  |  |  |
| 4 | `taiga/projects/api.py:378` | `return response.Ok(services.get_member_stats_for_project(project))` | taiga/base/response.py:120 Ok# | function::taiga/projects/services/stats.py::get_member_stats_for_project | import python::.::taiga/base/response.py::taiga/base/response/Ok# |  |  |  |  |
| 5 | `taiga/projects/attachments/permissions.py:27` | `create_perms = HasProjectPerm('modify_epic') \| (CommentAttachmentPerm() & HasProjectPerm('comment_epic'))` | taiga/base/api/permissions.py:163 HasProjectPerm# | class::taiga/projects/attachments/permissions.py::CommentAttachmentPerm | import python::.::taiga/base/api/permissions.py::taiga/base/api/permissions/HasProjectPerm# |  |  |  |  |
| 6 | `taiga/projects/attachments/permissions.py:67` | `create_perms = HasProjectPerm('modify_wiki_page') \| (CommentAttachmentPerm() & HasProjectPerm('comment_wiki_page'))` | taiga/base/api/permissions.py:163 HasProjectPerm# | class::taiga/projects/attachments/permissions.py::CommentAttachmentPerm | import python::.::taiga/base/api/permissions.py::taiga/base/api/permissions/HasProjectPerm# |  |  |  |  |
| 7 | `taiga/projects/attachments/permissions.py:81` | `return UserStoryAttachmentPermission(request, view).check_permissions('retrieve', obj) or is_owner` | taiga/base/api/permissions.py:39 ResourcePermission#check_permissions(). | class::taiga/projects/attachments/permissions.py::UserStoryAttachmentPermission | name python::.::taiga/base/api/permissions.py::taiga/base/api/permissions/ResourcePermission#c… |  |  |  |  |
| 8 | `taiga/projects/epics/serializers.py:41` | `is_blocked = Field()` | taiga/base/fields.py:142 Field# | no edge | import python::.::taiga/base/fields.py::taiga/base/fields/Field# |  |  |  |  |
| 9 | `taiga/projects/epics/services.py:246` | `epic_data[custom_attr.name] = text.sanitize_csv_text_value(value)` | taiga/base/utils/text.py:22 sanitize_csv_text_value(). | no edge | import python::.::taiga/base/utils/text.py::taiga/base/utils/text/sanitize_csv_text_value().#ff9… |  |  |  |  |
| 10 | `taiga/projects/history/models.py:174` | `users_list = [resolve_value("users", x) for x in diff_in if x]` | taiga/projects/history/models.py:152 HistoryEntry#resolve_value(). | no edge | name python::.::taiga/projects/history/models.py::taiga/projects/history/models/HistoryEntry#v… | dev has no node for the target |  |  |  |
| 11 | `taiga/projects/history/models.py:196` | `points[role_name] = [resolve_value("points", oldpoint_id),` | taiga/projects/history/models.py:152 HistoryEntry#resolve_value(). | no edge | name python::.::taiga/projects/history/models.py::taiga/projects/history/models/HistoryEntry#v… | dev has no node for the target |  |  |  |
| 12 | `taiga/projects/issues/api.py:258` | `milestone = get_object_or_error(Milestone, request.user, pk=data["milestone_id"])` | taiga/base/api/utils/__init__.py:51 get_object_or_error(). | class::taiga/projects/milestones/models.py::Milestone | import python::.::taiga/base/api/utils/__init__.py::taiga/base/api/utils/get_object_or_error().#… |  |  |  |  |
| 13 | `taiga/projects/milestones/api.py:152` | `project = get_object_or_error(Project, request.user, pk=data["project_id"])` | taiga/base/api/utils/__init__.py:51 get_object_or_error(). | class::taiga/projects/models.py::Project | import python::.::taiga/base/api/utils/__init__.py::taiga/base/api/utils/get_object_or_error().#… |  |  |  |  |
| 14 | `taiga/projects/milestones/api.py:194` | `project = get_object_or_error(Project, request.user, pk=data["project_id"])` | taiga/base/api/utils/__init__.py:51 get_object_or_error(). | class::taiga/projects/models.py::Project | import python::.::taiga/base/api/utils/__init__.py::taiga/base/api/utils/get_object_or_error().#… |  |  |  |  |
| 15 | `taiga/projects/milestones/permissions.py:23` | `watch_perms = IsAuthenticated() & HasProjectPerm('view_milestones')` | taiga/base/api/permissions.py:163 HasProjectPerm# | class::taiga/base/api/permissions.py::IsAuthenticated | import python::.::taiga/base/api/permissions.py::taiga/base/api/permissions/HasProjectPerm# |  |  |  |  |
| 16 | `taiga/projects/userstories/api.py:393` | `raise exc.Blocked(_("Blocked element"))` | taiga/base/exceptions.py:195 Blocked# | no edge | import python::.::taiga/base/exceptions.py::taiga/base/exceptions/Blocked# |  |  |  |  |
| 17 | `tests/integration/resources_permissions/test_attachment_resources.py:181` | `m.blocked_wiki_attachment = f.WikiAttachmentFactory(project=data.blocked_project, content_object=m.blocked_wiki)` | tests/factories.py:179 WikiAttachmentFactory# | no edge | import python::.::tests/factories.py::tests/factories/WikiAttachmentFactory# |  |  |  |  |
| 18 | `tests/integration/resources_permissions/test_auth_resources.py:24` | `reconnect_signals()` | tests/utils.py:28 reconnect_signals. | no edge | import python::.::tests/utils.py::tests/utils/reconnect_signals. | dev has no node for the target |  |  |  |
| 19 | `tests/integration/resources_permissions/test_tasks_resources.py:696` | `results = helper_test_http_method(client, 'post', private_url1, "", users)` | tests/utils.py:54 helper_test_http_method(). | no edge | import python::.::tests/utils.py::tests/utils/helper_test_http_method().#19a11830 |  |  |  |  |
| 20 | `tests/integration/resources_permissions/test_users_resources.py:31` | `reconnect_signals()` | tests/utils.py:28 reconnect_signals. | no edge | import python::.::tests/utils.py::tests/utils/reconnect_signals. | dev has no node for the target |  |  |  |
| 21 | `tests/integration/resources_permissions/test_userstories_resources.py:370` | `results = helper_test_http_method(client, 'put', private_url2, user_story_data, users)` | tests/utils.py:54 helper_test_http_method(). | no edge | import python::.::tests/utils.py::tests/utils/helper_test_http_method().#19a11830 |  |  |  |  |
| 22 | `tests/integration/test_memberships.py:38` | `f.MembershipFactory(project=project, user=john, is_admin=True)` | tests/factories.py:203 MembershipFactory# | no edge | import python::.::tests/factories.py::tests/factories/MembershipFactory# |  |  |  |  |
| 23 | `tests/integration/test_sitemaps.py:24` | `reconnect_signals()` | tests/utils.py:28 reconnect_signals. | no edge | import python::.::tests/utils.py::tests/utils/reconnect_signals. | dev has no node for the target |  |  |  |
| 24 | `tests/integration/test_stats.py:20` | `disconnect_signals()` | tests/utils.py:28 disconnect_signals. | no edge | import python::.::tests/utils.py::tests/utils/disconnect_signals. | dev has no node for the target |  |  |  |
| 25 | `tests/integration/test_timeline.py:232` | `history_services.take_snapshot(project, user=project.owner)` | taiga/projects/history/services.py:368 take_snapshot(). | no edge | import python::.::taiga/projects/history/services.py::taiga/projects/history/services/take_snaps… |  |  |  |  |

## Both miss (25 of 651)
<!-- kind: both_miss -->

Neither engine has a right edge. Check the oracle target first; real rows are shared blind spots.

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `taiga/auth/backends.py:94` | `raise TokenBackendError(format_lazy(_("You must have cryptography installed to use {}."), algorithm))` | taiga/auth/utils.py:59 format_lazy(). | no edge | unresolved unresolved::python::format_lazy | reported (many_candidates) |  |  |  |
| 2 | `taiga/base/api/request.py:257` | `def user(self, value):` | taiga/base/api/request.py:247 Request#user(). | no edge | no edge | silent; oracle reads a definition as a call |  |  |  |
| 3 | `taiga/base/exceptions.py:187` | `class NotAuthenticated(NotAuthenticated):` | taiga/base/exceptions.py:76 NotAuthenticated# | no edge | no edge | silent |  |  |  |
| 4 | `taiga/base/middleware/cors.py:32` | `response = self.get_response(request)` | taiga/base/middleware/cors.py:28 CorsMiddleware#get_response. | no edge | unresolved unresolved::python::self.get_response | no_node; dev has no node for the target |  |  |  |
| 5 | `taiga/events/middleware.py:44` | `response = self.get_response(request)` | taiga/events/middleware.py:40 SessionIDMiddleware#get_response. | no edge | unresolved unresolved::python::self.get_response | no_node; dev has no node for the target |  |  |  |
| 6 | `taiga/export_import/validators/validators.py:426` | `default_us_status = serializers.SlugRelatedField(slug_field="name", required=False)` | taiga/base/api/fields.py:276 WritableField# | no edge | import python::.::taiga/base/api/relations.py::taiga/base/api/relations/SlugRelatedField# | wrong_target |  |  |  |
| 7 | `taiga/external_apps/api.py:32` | `raise exc.NotAuthenticated(_("Authentication required"))` | taiga/base/exceptions.py:76 NotAuthenticated# | no edge | unresolved unresolved::python::exc.NotAuthenticated | reported (many_candidates) |  |  |  |
| 8 | `taiga/importers/jira/normal.py:30` | `"importer_type": "normal"} for project in self._client.get('/project', {"expand": "description"})]` | taiga/importers/jira/common.py:104 JiraClient#get(). | no edge | unresolved unresolved::python::self._client.get | reported (dynamic_dispatch) |  |  |  |
| 9 | `taiga/projects/api.py:403` | `project = self.get_object()` | taiga/base/api/generics.py:199 GenericAPIView#get_object(). | no edge | unresolved unresolved::python::self.get_object | reported (dynamic_dispatch) |  |  |  |
| 10 | `taiga/projects/issues/api.py:169` | `raise exc.PermissionDenied(_("You don't have permissions to set this severity "` | taiga/base/exceptions.py:81 PermissionDenied# | no edge | unresolved unresolved::python::exc.PermissionDenied | reported (many_candidates) |  |  |  |
| 11 | `taiga/projects/references/validators.py:17` | `us = serializers.IntegerField(required=False)` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/IntegerField# | wrong_target |  |  |  |
| 12 | `taiga/projects/settings/serializers.py:16` | `project_name = serializers.SerializerMethodField("get_project_name")` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/SerializerMethodField# | wrong_target |  |  |  |
| 13 | `taiga/projects/tasks/validators.py:155` | `project_id = serializers.IntegerField()` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/IntegerField# | wrong_target |  |  |  |
| 14 | `taiga/projects/userstories/api.py:194` | `raise exc.PermissionDenied(_("You don't have permissions to set this status "` | taiga/base/exceptions.py:81 PermissionDenied# | no edge | unresolved unresolved::python::exc.PermissionDenied | reported (many_candidates) |  |  |  |
| 15 | `taiga/projects/userstories/api.py:482` | `raise exc.PermissionDenied(_("Archived project"))` | taiga/base/exceptions.py:81 PermissionDenied# | no edge | unresolved unresolved::python::exc.PermissionDenied | reported (many_candidates) |  |  |  |
| 16 | `taiga/projects/userstories/filters.py:108` | `return filters.FilterBackend.filter_queryset(self, request, queryset, view)` | taiga/base/filters.py:102 OrderByFilterMixin#filter_queryset(). | no edge | unresolved unresolved::python::filters.FilterBackend.filter_queryset | reported (no_candidate) |  |  |  |
| 17 | `taiga/routers.py:104` | `router.register(r"epic-custom-attributes", EpicCustomAttributeViewSet,` | taiga/base/routers.py:353 NestedRouterMixin#register(). | no edge | unresolved unresolved::python::router.register | reported (dynamic_dispatch) |  |  |  |
| 18 | `taiga/routers.py:113` | `router.register(r"epics/custom-attributes-values", EpicCustomAttributesValuesViewSet,` | taiga/base/routers.py:353 NestedRouterMixin#register(). | no edge | unresolved unresolved::python::router.register | reported (dynamic_dispatch) |  |  |  |
| 19 | `taiga/timeline/serializers.py:24` | `data = serializers.SerializerMethodField("get_data")` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/SerializerMethodField# | wrong_target |  |  |  |
| 20 | `tests/integration/test_hooks_gitlab.py:1098` | `def test_issues_event_updated_issue_without_connection(client):` | tests/integration/test_hooks_gitlab.py:1032 test_issues_event_updated_issue_without_connection(). | no edge | no edge | silent; oracle reads a definition as a call |  |  |  |
| 21 | `tests/integration/test_userstories_update_backlog_order.py:638` | `def test_api_update_orders_in_bulk_invalid_after_us_because_milestone(client):` | tests/integration/test_userstories_update_backlog_order.py:554 test_api_update_orders_in_bulk_invalid_after_us_because_milestone(). | no edge | no edge | silent; oracle reads a definition as a call |  |  |  |
| 22 | `tests/unit/auth/test_authentication.py:71` | `assert backend.get_header(request) == fake_header` | taiga/auth/authentication.py:80 JWTAuthentication#get_header(). | no edge | unresolved unresolved::python::backend.get_header | reported (dynamic_dispatch) |  |  |  |
| 23 | `tests/unit/auth/test_token_denylist.py:151` | `not_expired_2 = RefreshToken.for_user(user)` | taiga/auth/tokens.py:247 DenylistMixin#for_user(). | no edge | unresolved unresolved::python::RefreshToken.for_user | reported (no_candidate) |  |  |  |
| 24 | `tests/unit/auth/test_token_denylist.py:171` | `not_expired_4 = RefreshToken.for_user(user)` | taiga/auth/tokens.py:247 DenylistMixin#for_user(). | no edge | unresolved unresolved::python::RefreshToken.for_user | reported (no_candidate) |  |  |  |
| 25 | `tests/unit/auth/test_tokens.py:350` | `token = MyToken.for_user(user)` | taiga/auth/tokens.py:185 Token#for_user(). | no edge | unresolved unresolved::python::MyToken.for_user | reported (no_candidate) |  |  |  |

## Wrong dev edges (15 of 388)
<!-- kind: dev_wrong -->

A dev edge whose target is none of the line's oracle targets. Check a few: this is where dev's precision goes.

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `taiga/base/api/fields.py:223` | `return self.to_native(obj)` | taiga/base/api/fields.py:235 Field#to_native(). | method::taiga/base/api/relations.py::PrimaryKeyRelatedField::to_native | no edge |  |  |  |  |
| 2 | `taiga/base/api/fields.py:395` | `value = self.from_native(native)` | taiga/base/api/fields.py:404 WritableField#from_native(). | method::taiga/base/api/relations.py::SlugRelatedField::from_native | no edge |  |  |  |  |
| 3 | `taiga/base/api/fields.py:400` | `self.validate(value)` | taiga/base/api/fields.py:341 WritableField#validate(). | method::taiga/base/api/fields.py::ModelField::validate | no edge |  |  |  |  |
| 4 | `taiga/base/api/fields.py:400` | `self.validate(value)` | taiga/base/api/fields.py:341 WritableField#validate(). | method::taiga/base/api/fields.py::ChoiceField::validate | no edge |  |  |  |  |
| 5 | `taiga/base/api/serializers.py:751` | `field = self.get_pk_field(pk_field)` | taiga/base/api/serializers.py:881 ModelSerializer#get_pk_field(). | method::taiga/base/api/serializers.py::HyperlinkedModelSerializer::get_pk_field | no edge |  |  |  |  |
| 6 | `taiga/base/api/serializers.py:948` | `return ChoiceField(**kwargs)` | taiga/base/api/fields.py:495 CharField# | class::taiga/base/api/fields.py::ChoiceField | python::.::taiga/base/api/fields.py::taiga/base/api/fields/ChoiceField#; python::.::taiga/base/api/fields.py::taiga/base/api/fields/ChoiceField#__init__().#6f79be… |  |  |  |  |
| 7 | `taiga/base/filters.py:646` | `return FilterBackend.filter_queryset(self, request, queryset, view)` | taiga/base/filters.py:102 OrderByFilterMixin#filter_queryset(). | method::taiga/projects/filters.py::CanViewProjectObjFilterBackend::filter_queryset | no edge |  |  |  |  |
| 8 | `taiga/projects/migrations/0013_auto_20141210_1040.py:30` | `_fix_tags_model(Project)` | taiga/projects/migrations/0013_auto_20141210_1040.py:17 _fix_tags_model(). | class::taiga/projects/models.py::Project | python::.::taiga/projects/migrations/0013_auto_20141210_1040.py::taiga/projects/migration… |  |  |  |  |
| 9 | `taiga/projects/userstories/api.py:445` | `milestone = get_object_or_error(Milestone, request.user, pk=milestone_id, project=project)` | taiga/base/api/utils/__init__.py:51 get_object_or_error(). | class::taiga/projects/milestones/models.py::Milestone | python::.::taiga/base/api/utils/__init__.py::taiga/base/api/utils/get_object_or_error().#… |  |  |  |  |
| 10 | `tests/integration/resources_permissions/test_epics_resources.py:364` | `epic_data = EpicSerializer(data.public_epic).data` | taiga/projects/epics/serializers.py:54 EpicSerializer# | method::taiga/base/api/serializers.py::LightSerializer::__init__ | python::.::taiga/projects/epics/serializers.py::taiga/projects/epics/serializers/EpicSeri… |  |  |  |  |
| 11 | `tests/integration/resources_permissions/test_projects_choices_resources.py:1735` | `projects_data = json.loads(response.content.decode('utf-8'))` | taiga/base/utils/json.py:19 loads(). | method::taiga/auth/backends.py::TokenBackend::decode | python::.::taiga/base/utils/json.py::taiga/base/utils/json/loads().#ff92409d |  |  |  |  |
| 12 | `tests/integration/resources_permissions/test_storage_resources.py:113` | `results = helper_test_http_method(client, 'post', url, create_data, users, lambda: StorageEntry.objects.all().delete())` | tests/utils.py:54 helper_test_http_method(). | class::taiga/userstorage/models.py::StorageEntry | python::.::tests/utils.py::tests/utils/helper_test_http_method().#19a11830 |  |  |  |  |
| 13 | `tests/integration/test_hooks_bitbucket.py:810` | `assert get_history_queryset_by_model_instance(issue).count() == 0` | taiga/projects/history/services.py:441 get_history_queryset_by_model_instance(). | function::tests/integration/test_userstories.py::test_api_filters_data_respects_archived_… | python::.::taiga/projects/history/services.py::taiga/projects/history/services/get_histor… |  |  |  |  |
| 14 | `tests/integration/test_timeline.py:82` | `service.register_timeline_implementation("tasks.task", "test", lambda x, extra_data=None: id(x))` | taiga/timeline/service.py:252 register_timeline_implementation(). | method::taiga/auth/models.py::TokenUser::id | python::.::taiga/timeline/service.py::taiga/timeline/service/register_timeline_implementa… |  |  |  |  |
| 15 | `tests/unit/auth/test_tokens.py:414` | `access_token = AccessToken()` | taiga/auth/tokens.py:306 AccessToken# | method::taiga/auth/tokens.py::Token::__init__ | python::.::taiga/auth/tokens.py::taiga/auth/tokens/AccessToken#; python::.::taiga/auth/tokens.py::taiga/auth/tokens/Token#__init__().#7bc8abd7 |  |  |  |  |

## v2 edges the score cannot judge (10 of 147 rows, 149 edges)
<!-- kind: v2_unscored -->

v2 edges on lines where the oracle has no call with a target v2 has a node for. Not in any score. Look for calls the oracle misses (v2 right, oracle silent) and for v2 edges that are plainly wrong.

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `taiga/base/api/generics.py:317` | `return self.list(request, *args, **kwargs)` | no oracle call with a target | no edge | name python::.::taiga/base/api/mixins.py::taiga/base/api/mixins/ListModelMixin#list().#ef8b748c (at call site: yes) |  |  |  |  |
| 2 | `taiga/base/fields.py:133` | `raise ValidationError(self.error_messages['invalid_type'],` | no oracle call with a target | no edge | name python::.::taiga/base/exceptions.py::taiga/base/exceptions/ValidationError. (at call site: yes) |  |  |  |  |
| 3 | `taiga/base/routers.py:66` | `raise NotImplemented('get_urls must be overridden')` | no oracle call with a target | class::taiga/base/response.py::NotImplemented; method::taiga/base/response.py::Response::__init__ | name python::.::taiga/base/response.py::taiga/base/response/NotImplemented# (at call site: yes) |  |  |  |  |
| 4 | `taiga/importers/pivotal/tasks.py:21` | `@app.task(bind=True)` | no oracle call with a target | method::taiga/export_import/api.py::ProjectImporterViewSet::task | exact python::.::taiga/importers/pivotal/tasks.py::taiga/importers/pivotal/tasks/import_project… (at call site: no) |  |  |  |  |
| 5 | `taiga/importers/trello/tasks.py:21` | `@app.task(bind=True)` | no oracle call with a target | method::taiga/export_import/api.py::ProjectImporterViewSet::task | exact python::.::taiga/importers/trello/tasks.py::taiga/importers/trello/tasks/import_project()… (at call site: no) |  |  |  |  |
| 6 | `taiga/projects/api.py:550` | `services.delete_project(obj.id)` | no oracle call with a target | function::taiga/projects/services/projects.py::delete_project | import python::.::taiga/projects/services/projects.py::taiga/projects/services/projects/delete_p… (at call site: yes) |  |  |  |  |
| 7 | `taiga/projects/notifications/tasks.py:13` | `@app.task()` | no oracle call with a target | method::taiga/export_import/api.py::ProjectImporterViewSet::task | exact python::.::taiga/projects/notifications/tasks.py::taiga/projects/notifications/tasks/send… (at call site: no) |  |  |  |  |
| 8 | `taiga/projects/signals.py:92` | `SwimlaneUserStoryStatus(` | no oracle call with a target | class::taiga/projects/models.py::SwimlaneUserStoryStatus | name python::.::taiga/projects/models.py::taiga/projects/models/SwimlaneUserStoryStatus# (at call site: yes) |  |  |  |  |
| 9 | `taiga/users/api.py:292` | `"didn't use it before?"))` | no oracle call with a target | no edge | name python::.::taiga/base/exceptions.py::taiga/base/exceptions/BaseException#__init__().#7c91… (at call site: no) |  |  |  |  |
| 10 | `tests/integration/resources_permissions/test_projects_choices_resources.py:23` | `@pytest.fixture` | no oracle call with a target | no edge | exact python::.::tests/integration/resources_permissions/test_projects_choices_resources.py::te… (at call site: no) |  |  |  |  |

## dev edges the score cannot judge (10 of 2062 rows, 2079 edges)
<!-- kind: dev_unscored -->

The same for dev.

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `file::taiga/routers.py:85` | `(file not in the checkout)` | no oracle call with a target | class::taiga/projects/api.py::TaskDueDateViewSet | no edge |  |  |  |  |
| 2 | `taiga/base/api/request.py:379` | `stream = self.stream` | no oracle call with a target | method::taiga/base/api/request.py::Request::stream | no edge |  |  |  |  |
| 3 | `taiga/base/fields.py:161` | `super(I18NJSONField, self).__init__(*args, **kwargs)` | no oracle call with a target | class::taiga/base/fields.py::I18NJSONField | no edge |  |  |  |  |
| 4 | `taiga/importers/jira/common.py:169` | `if isinstance(user_id, User):` | no oracle call with a target | class::taiga/users/models.py::User ×2 | no edge |  |  |  |  |
| 5 | `taiga/importers/services.py:36` | `if Membership.objects.filter(project=project, user=user).count() > 0:` | no oracle call with a target | function::tests/integration/test_userstories.py::test_api_filters_data_respects_archived_… | no edge |  |  |  |  |
| 6 | `taiga/projects/milestones/api.py:116` | `'total_userstories': milestone.cached_user_stories.count(),` | no oracle call with a target | function::tests/integration/test_userstories.py::test_api_filters_data_respects_archived_… | no edge |  |  |  |  |
| 7 | `taiga/projects/milestones/api.py:205` | `class MilestoneWatchersViewSet(WatchersViewSetMixin, ModelListViewSet):` | no oracle call with a target | class::taiga/projects/notifications/serializers.py::WatcherSerializer | no edge |  |  |  |  |
| 8 | `taiga/projects/notifications/services.py:147` | `elif isinstance(obj, Task):` | no oracle call with a target | class::taiga/projects/tasks/models.py::Task | no edge |  |  |  |  |
| 9 | `taiga/projects/services/bulk_update_order.py:270` | `'swimlane_id': [s_id] * s.user_stories.count()` | no oracle call with a target | function::tests/integration/test_userstories.py::test_api_filters_data_respects_archived_… | no edge |  |  |  |  |
| 10 | `tests/integration/test_history.py:68` | `assert qs_all.count() == 0` | no oracle call with a target | function::tests/integration/test_userstories.py::test_api_filters_data_respects_archived_… | no edge |  |  |  |  |

## Both right (spot check) (10 of 4415)
<!-- kind: both_right -->

The machine says both engines are right. Check a few: if these are wrong, every score is too high.

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `taiga/export_import/validators/fields.py:160` | `user = UserRelatedField().from_native(data[0])` | taiga/export_import/validators/fields.py:91 UserRelatedField# | class::taiga/export_import/validators/fields.py::UserRelatedField; method::taiga/export_import/validators/fields.py::UserRelatedField::from_native | name python::.::taiga/export_import/validators/fields.py::taiga/export_import/validators/field… | dev has 2 targets on this line |  |  |  |
| 2 | `taiga/projects/api.py:141` | `flt = filters.get_filter_expression_can_view_projects(request.user)` | taiga/base/filters.py:24 get_filter_expression_can_view_projects(). | function::taiga/base/filters.py::get_filter_expression_can_view_projects | import python::.::taiga/base/filters.py::taiga/base/filters/get_filter_expression_can_view_proje… |  |  |  |  |
| 3 | `taiga/projects/custom_attributes/validators.py:83` | `attributes_values = JSONField(source="attributes_values", label="attributes values")` | taiga/base/fields.py:22 JSONField# | class::taiga/base/fields.py::JSONField | import python::.::taiga/base/fields.py::taiga/base/fields/JSONField# |  |  |  |  |
| 4 | `taiga/projects/epics/serializers.py:67` | `return mdrender(obj.project, obj.description)` | taiga/mdrender/service.py:129 render(). | function::taiga/mdrender/service.py::render | import python::.::taiga/mdrender/service.py::taiga/mdrender/service/render().#0b082246 |  |  |  |  |
| 5 | `taiga/timeline/api.py:102` | `return service.get_user_timeline(user, accessing_user=self.request.user)` | taiga/timeline/service.py:235 get_user_timeline(). | function::taiga/timeline/service.py::get_user_timeline | import python::.::taiga/timeline/service.py::taiga/timeline/service/get_user_timeline().#81cdbfce |  |  |  |  |
| 6 | `taiga/timeline/serializers.py:83` | `thumb_url = get_thumbnail_url(attached_file,` | taiga/base/utils/thumbnails.py:80 get_thumbnail_url(). | function::taiga/base/utils/thumbnails.py::get_thumbnail_url | import python::.::taiga/base/utils/thumbnails.py::taiga/base/utils/thumbnails/get_thumbnail_url(… |  |  |  |  |
| 7 | `taiga/timeline/timeline_implementations.py:105` | `@register_timeline_implementation("wiki.wikipage", "create")` | taiga/timeline/service.py:252 register_timeline_implementation(). | function::taiga/timeline/service.py::register_timeline_implementation | import python::.::taiga/timeline/service.py::taiga/timeline/service/register_timeline_implementa… |  |  |  |  |
| 8 | `tests/integration/test_timeline.py:600` | `service.register_timeline_implementation("epics.relateduserstory", "test", lambda x, extra_data=None: id(x))` | taiga/timeline/service.py:252 register_timeline_implementation(). | function::taiga/timeline/service.py::register_timeline_implementation; method::taiga/auth/models.py::TokenUser::id | import python::.::taiga/timeline/service.py::taiga/timeline/service/register_timeline_implementa… | dev has 2 targets on this line |  |  |  |
| 9 | `tests/integration/test_userstories_update_backlog_order.py:522` | `response = client.json.post(url, json.dumps(data))` | taiga/base/utils/json.py:15 dumps(). | function::taiga/base/utils/json.py::dumps | import python::.::taiga/base/utils/json.py::taiga/base/utils/json/dumps().#35deb74e |  |  |  |  |
| 10 | `tests/integration/test_watch_userstories.py:71` | `user_story = f.create_userstory(owner=user, status=None)` | tests/factories.py:708 create_userstory(). | function::tests/factories.py::create_userstory | import python::.::tests/factories.py::tests/factories/create_userstory().#4c205102 |  |  |  |  |

