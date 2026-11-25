# taiga-back (python): graph differences to verify, REFERENCES

Repo `https://github.com/taigaio/taiga-back` at `8ab6a4e3b5f6fbbfcbf108a6449011f07b7308aa`. Old engine `25ae40bf8662`, graph v2 `4e50b002a213`.

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

In-repo references (a name used, not called) found by the oracle: 9163. Both right 538, gap 73, v2 gain 1850, both miss 6702.
Scored edges: v2 2433 (24 wrong), dev 669 (58 wrong). Not scored: v2 356, dev 142.
REFERENCES recall: dev 6.7% (611/9163), v2 26.1% (2388/9163). REFERENCES precision: dev 91.3% (611/669), v2 99.0% (2409/2433).
dev's REFERENCES are its READS / WRITES: module-level variables only, so its recall is low by design. v2 REFERENCES are reads, writes and type annotations; only the target is judged, not the access.
Line precision judges each engine only on lines where the oracle has a call it can map, and counts edges that sit on no oracle call (decorator lines) as wrong. Do not rank the engines on it alone.
v2 precision at exact call sites (published): 0.988.
Flags: {"dev_multi_both_right": 76, "dev_multi_gap": 16} (def_line_* = the line defines a function of the target's own name, usually the oracle's mistake; dev_multi_* = dev was right but had several targets on the line).
Scorer notes: {"dev_edges_with_file_source_never_scored": 0, "dev_references_without_site_line": 0}.
Check against the published scores: OK (full (dev only; v2 is published by exact site)).

## How each v2 miss happened

| group | v2 miss | reason | calls |
|---|---|---|---|
| both_miss | silent | - | 5035 |
| both_miss | no_node | - | 1010 |
| both_miss | reported | dynamic_dispatch | 524 |
| both_miss | reported | no_candidate | 101 |
| gap | silent | - | 72 |
| both_miss | wrong_target | - | 22 |
| both_miss | reported | many_candidates | 10 |
| gap | reported | many_candidates | 1 |

`no_node`: v2 has no node for the target. `wrong_target`: v2 resolved this call to another target. `external`: v2 called it external. `reported`: only unresolved edges, with v2's reason. `silent`: no v2 edge at this call at all.

Verdict: `confirmed` (the row is what its group says), `oracle wrong`, `dev wrong`, `v2 right after all`, or `?`.
Cause: one short phrase for the code shape (for example `method on a constructor-injected field`). Reuse phrases.
Reason true: for a `reported` miss, `yes` or `no`.

## Gaps: dev is right, v2 is not (25 of 73)
<!-- kind: gap -->

What v2 loses against the old engine. Check: is the oracle target right, does dev's edge really go there, and is v2 really wrong?

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `taiga/auth/authentication.py:76` | `AUTH_HEADER_TYPES[0],` | taiga/auth/authentication.py:39 AUTH_HEADER_TYPES. | variable::taiga/auth/authentication.py::AUTH_HEADER_TYPES | unresolved unresolved::python::AUTH_HEADER_TYPES | reported (many_candidates) |  |  |  |
| 2 | `taiga/base/filters.py:272` | `logger.error("Filtering project diferent value than an integer: {}".format(` | taiga/base/filters.py:21 logger. | variable::taiga/base/filters.py::logger | no edge | silent |  |  |  |
| 3 | `taiga/events/middleware.py:58` | `_local.session_id = None` | taiga/events/middleware.py:10 _local. | variable::taiga/events/middleware.py::_local | no edge | silent |  |  |  |
| 4 | `taiga/export_import/serializers/fields.py:32` | `logger.error("UnicodeEncodeError in %s", obj.name,` | taiga/export_import/serializers/fields.py:21 logger. | variable::taiga/export_import/serializers/fields.py::logger | no edge | silent |  |  |  |
| 5 | `taiga/importers/asana/tasks.py:38` | `logger.error('Error importing Asana project %s (by %s)', project_id, user, exc_info=sys.exc_info())` | taiga/importers/asana/tasks.py:18 logger. | variable::taiga/importers/asana/tasks.py::logger | no edge | silent |  |  |  |
| 6 | `taiga/importers/github/importer.py:260` | `rewritten = GITHUB_INLINE_IMAGE_RE.sub(replace_image, markdown or "")` | taiga/importers/github/importer.py:46 GITHUB_INLINE_IMAGE_RE. | variable::taiga/importers/github/importer.py::GITHUB_INLINE_IMAGE_RE | exact python::.::taiga/importers/github/importer.py::taiga/importers/github/importer/GithubImpo… | silent |  |  |  |
| 7 | `taiga/importers/github/importer.py:261` | `return GITHUB_INLINE_IMAGE_HTML_RE.sub(replace_image, rewritten)` | taiga/importers/github/importer.py:50 GITHUB_INLINE_IMAGE_HTML_RE. | variable::taiga/importers/github/importer.py::GITHUB_INLINE_IMAGE_HTML_RE | exact python::.::taiga/importers/github/importer.py::taiga/importers/github/importer/GithubImpo… | silent |  |  |  |
| 8 | `taiga/importers/jira/common.py:657` | `color=EPIC_COLORS.get(history_item['toString'], "#999999")` | taiga/importers/jira/common.py:41 EPIC_COLORS. | variable::taiga/importers/jira/common.py::EPIC_COLORS | no edge | silent |  |  |  |
| 9 | `taiga/importers/pivotal/tasks.py:38` | `logger.error('Error importing PivotalTracker project %s (by %s)', project_id, user, exc_info=sys.exc_info())` | taiga/importers/pivotal/tasks.py:18 logger. | variable::taiga/importers/pivotal/tasks.py::logger | no edge | silent |  |  |  |
| 10 | `taiga/importers/trello/tasks.py:38` | `logger.error('Error importing Trello project %s (by %s)', project_id, user, exc_info=sys.exc_info())` | taiga/importers/trello/tasks.py:18 logger. | variable::taiga/importers/trello/tasks.py::logger | no edge | silent |  |  |  |
| 11 | `taiga/projects/filters.py:52` | `logger.error("Filtering project diferent value than an integer: {}".format(` | taiga/projects/filters.py:19 logger. | variable::taiga/projects/filters.py::logger | no edge | silent |  |  |  |
| 12 | `taiga/projects/notifications/apps.py:32` | `signal_comment.connect(handlers.on_comment)` | taiga/projects/notifications/apps.py:17 signal_comment. | variable::taiga/projects/notifications/apps.py::signal_comment | no edge | silent |  |  |  |
| 13 | `taiga/projects/notifications/apps.py:33` | `signal_comment_mentions.connect(handlers.on_comment_mentions)` | taiga/projects/notifications/apps.py:18 signal_comment_mentions. | variable::taiga/projects/notifications/apps.py::signal_comment_mentions | no edge | silent |  |  |  |
| 14 | `taiga/timeline/rebuilder.py:126` | `bulk_creator.flush()` | taiga/timeline/rebuilder.py:40 bulk_creator. | variable::taiga/timeline/rebuilder.py::bulk_creator | no edge | silent |  |  |  |
| 15 | `tests/unit/auth/test_backends.py:122` | `hmac_token = hmac_token_backend.encode(payload)` | tests/unit/auth/test_backends.py:94 hmac_token_backend. | variable::tests/unit/auth/test_backends.py::hmac_token_backend; variable::tests/unit/auth/test_backends.py::payload | no edge | silent; dev has 2 targets on this line |  |  |  |
| 16 | `tests/unit/auth/test_backends.py:149` | `rsa_token = aud_iss_token_backend.encode(payload)` | tests/unit/auth/test_backends.py:96 aud_iss_token_backend. | variable::tests/unit/auth/test_backends.py::aud_iss_token_backend; variable::tests/unit/auth/test_backends.py::payload | no edge | silent; dev has 2 targets on this line |  |  |  |
| 17 | `tests/unit/auth/test_backends.py:180` | `assert hmac_token_backend.decode(no_exp_token, verify=False) == payload` | tests/unit/auth/test_backends.py:94 hmac_token_backend. | variable::tests/unit/auth/test_backends.py::hmac_token_backend; variable::tests/unit/auth/test_backends.py::payload | name python::.::tests/unit/auth/test_backends.py::tests/unit/auth/test_backends/payload. | silent; dev has 2 targets on this line |  |  |  |
| 18 | `tests/unit/auth/test_backends.py:203` | `hmac_token_backend.decode(invalid_token)` | tests/unit/auth/test_backends.py:94 hmac_token_backend. | variable::tests/unit/auth/test_backends.py::hmac_token_backend | no edge | silent |  |  |  |
| 19 | `tests/unit/auth/test_backends.py:229` | `assert hmac_token_backend.decode(token) == payload` | tests/unit/auth/test_backends.py:94 hmac_token_backend. | variable::tests/unit/auth/test_backends.py::hmac_token_backend; variable::tests/unit/auth/test_backends.py::payload | name python::.::tests/unit/auth/test_backends.py::tests/unit/auth/test_backends/payload. | silent; dev has 2 targets on this line |  |  |  |
| 20 | `tests/unit/auth/test_backends.py:235` | `rsa_token_backend.decode(no_exp_token)` | tests/unit/auth/test_backends.py:95 rsa_token_backend. | variable::tests/unit/auth/test_backends.py::rsa_token_backend | no edge | silent |  |  |  |
| 21 | `tests/unit/auth/test_backends.py:263` | `rsa_token_backend.decode(invalid_token)` | tests/unit/auth/test_backends.py:95 rsa_token_backend. | variable::tests/unit/auth/test_backends.py::rsa_token_backend | no edge | silent |  |  |  |
| 22 | `tests/unit/auth/test_backends.py:278` | `assert hmac_token_backend.decode(invalid_token, verify=False) == payload` | tests/unit/auth/test_backends.py:94 hmac_token_backend. | variable::tests/unit/auth/test_backends.py::hmac_token_backend; variable::tests/unit/auth/test_backends.py::payload | name python::.::tests/unit/auth/test_backends.py::tests/unit/auth/test_backends/payload. | silent; dev has 2 targets on this line |  |  |  |
| 23 | `tests/unit/auth/test_backends.py:302` | `assert aud_iss_token_backend.decode(token) == payload` | tests/unit/auth/test_backends.py:96 aud_iss_token_backend. | variable::tests/unit/auth/test_backends.py::aud_iss_token_backend; variable::tests/unit/auth/test_backends.py::payload | name python::.::tests/unit/auth/test_backends.py::tests/unit/auth/test_backends/payload. | silent; dev has 2 targets on this line |  |  |  |
| 24 | `tests/unit/auth/test_backends.py:319` | `hmac_token_backend.decode(token)` | tests/unit/auth/test_backends.py:94 hmac_token_backend. | variable::tests/unit/auth/test_backends.py::hmac_token_backend | no edge | silent |  |  |  |
| 25 | `tests/unit/test_mdrender.py:317` | `mock.assert_called_with(dummy_project.id, 42)` | tests/unit/test_mdrender.py:17 dummy_project. | variable::tests/unit/test_mdrender.py::dummy_project | no edge | silent |  |  |  |

## Wrong v2 edges (24 of 24)
<!-- kind: v2_wrong -->

A v2 edge on a line where the oracle has a call, whose target is none of that line's oracle targets. `at call site: no` means the edge sits on no call the oracle saw (for example a decorator line). Check: is v2's target wrong?

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `taiga/base/api/generics.py:161` | `model = self.model` | taiga/base/api/generics.py:59 GenericAPIView#model. | no edge | name python::.::taiga/base/api/generics.py::taiga/base/api/generics/GenericAPIView#get_seriali… (at reference site: yes) |  |  |  |  |
| 2 | `taiga/base/api/generics.py:177` | `model = self.model` | taiga/base/api/generics.py:59 GenericAPIView#model. | no edge | name python::.::taiga/base/api/generics.py::taiga/base/api/generics/GenericAPIView#get_validat… (at reference site: yes) |  |  |  |  |
| 3 | `taiga/base/api/serializers.py:180` | `if isinstance(obj, Field)]` | taiga/base/api/fields.py:276 WritableField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/Field# (at reference site: yes) |  |  |  |  |
| 4 | `taiga/base/api/serializers.py:711` | `models.AutoField: IntegerField,` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/IntegerField# (at reference site: yes) |  |  |  |  |
| 5 | `taiga/base/api/serializers.py:712` | `models.FloatField: FloatField,` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/FloatField# (at reference site: yes) |  |  |  |  |
| 6 | `taiga/base/api/serializers.py:713` | `models.IntegerField: IntegerField,` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/IntegerField# (at reference site: yes) |  |  |  |  |
| 7 | `taiga/base/api/serializers.py:714` | `models.PositiveIntegerField: IntegerField,` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/IntegerField# (at reference site: yes) |  |  |  |  |
| 8 | `taiga/base/api/serializers.py:715` | `models.SmallIntegerField: IntegerField,` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/IntegerField# (at reference site: yes) |  |  |  |  |
| 9 | `taiga/base/api/serializers.py:716` | `models.PositiveSmallIntegerField: IntegerField,` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/IntegerField# (at reference site: yes) |  |  |  |  |
| 10 | `taiga/base/api/serializers.py:717` | `models.DateTimeField: DateTimeField,` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/DateTimeField# (at reference site: yes) |  |  |  |  |
| 11 | `taiga/base/api/serializers.py:718` | `models.DateField: DateField,` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/DateField# (at reference site: yes) |  |  |  |  |
| 12 | `taiga/base/api/serializers.py:719` | `models.TimeField: TimeField,` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/TimeField# (at reference site: yes) |  |  |  |  |
| 13 | `taiga/base/api/serializers.py:720` | `models.DecimalField: DecimalField,` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/DecimalField# (at reference site: yes) |  |  |  |  |
| 14 | `taiga/base/api/serializers.py:721` | `models.EmailField: EmailField,` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/EmailField# (at reference site: yes) |  |  |  |  |
| 15 | `taiga/base/api/serializers.py:723` | `models.URLField: URLField,` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/URLField# (at reference site: yes) |  |  |  |  |
| 16 | `taiga/base/api/serializers.py:724` | `models.SlugField: SlugField,` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/SlugField# (at reference site: yes) |  |  |  |  |
| 17 | `taiga/base/api/serializers.py:727` | `models.BooleanField: BooleanField,` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/BooleanField# (at reference site: yes) |  |  |  |  |
| 18 | `taiga/base/api/serializers.py:728` | `models.NullBooleanField: BooleanField,` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/BooleanField# (at reference site: yes) |  |  |  |  |
| 19 | `taiga/base/api/serializers.py:729` | `models.FileField: FileField,` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/FileField# (at reference site: yes) |  |  |  |  |
| 20 | `taiga/base/api/serializers.py:730` | `models.ImageField: ImageField,` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/ImageField# (at reference site: yes) |  |  |  |  |
| 21 | `taiga/base/api/serializers.py:1177` | `_hyperlink_field_class = HyperlinkedRelatedField` | taiga/base/api/fields.py:276 WritableField# | no edge | import python::.::taiga/base/api/relations.py::taiga/base/api/relations/HyperlinkedRelatedField# (at reference site: yes) |  |  |  |  |
| 22 | `taiga/base/api/serializers.py:1178` | `_hyperlink_identify_field_class = HyperlinkedIdentityField` | taiga/base/api/fields.py:276 WritableField# | no edge | import python::.::taiga/base/api/relations.py::taiga/base/api/relations/HyperlinkedIdentityField# (at reference site: yes) |  |  |  |  |
| 23 | `taiga/base/api/throttling.py:256` | `self.scope = getattr(view, self.scope_attr, None)` | taiga/base/api/throttling.py:247 ScopedRateThrottle#scope_attr. | no edge | name python::.::taiga/base/api/throttling.py::taiga/base/api/throttling/SimpleRateThrottle#sco… (at reference site: no) |  |  |  |  |
| 24 | `taiga/projects/history/models.py:311` | `value = [resolve_value(key, x) for x in self.diff[key]]` | taiga/projects/history/models.py:51 HistoryEntry#diff. | no edge | name python::.::taiga/projects/history/models.py::taiga/projects/history/models/HistoryEntry#k… (at reference site: yes) |  |  |  |  |

## v2 gains: v2 is right, dev is not (25 of 1850)
<!-- kind: v2_gain -->

What v2 adds. Verify a few so the gain is real.

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `taiga/base/api/authentication.py:110` | `auth_parts = base64.b64decode(auth[1]).decode(HTTP_HEADER_ENCODING).partition(':')` | taiga/base/api/__init__.py:37 HTTP_HEADER_ENCODING. | module:::HTTP_HEADER_ENCODING | import python::.::taiga/base/api/__init__.py::taiga/base/api/HTTP_HEADER_ENCODING. |  |  |  |  |
| 2 | `taiga/base/api/fields.py:110` | `format = ", ".join(formats).replace(ISO_8601,` | taiga/base/api/__init__.py:40 ISO_8601. | module:::ISO_8601 | import python::.::taiga/base/api/__init__.py::taiga/base/api/ISO_8601. |  |  |  |  |
| 3 | `taiga/base/api/fields.py:857` | `if self.format.lower() == ISO_8601:` | taiga/base/api/__init__.py:40 ISO_8601. | module:::ISO_8601 | import python::.::taiga/base/api/__init__.py::taiga/base/api/ISO_8601. |  |  |  |  |
| 4 | `taiga/base/api/relations.py:99` | `self.empty_label = BLANK_CHOICE_DASH[0][1]` | taiga/base/api/relations.py:76 RelatedField#empty_label. | module:django.db.models.fields::BLANK_CHOICE_DASH | name python::.::taiga/base/api/relations.py::taiga/base/api/relations/RelatedField#empty_label. |  |  |  |  |
| 5 | `taiga/base/api/serializers.py:722` | `models.CharField: CharField,` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/CharField# |  |  |  |  |
| 6 | `taiga/base/api/viewsets.py:98` | `update_wrapper(view, cls, updated=())` | taiga/base/api/viewsets.py:77 ViewSetMixin#view(). | no edge | exact python::.::taiga/base/api/viewsets.py::taiga/base/api/viewsets/ViewSetMixin#as_view().vie… | dev has no node for the target |  |  |  |
| 7 | `taiga/base/api/viewsets.py:102` | `update_wrapper(view, cls.dispatch, assigned=())` | taiga/base/api/viewsets.py:77 ViewSetMixin#view(). | no edge | exact python::.::taiga/base/api/viewsets.py::taiga/base/api/viewsets/ViewSetMixin#as_view().vie… | dev has no node for the target |  |  |  |
| 8 | `taiga/base/filters.py:397` | `values = map(_transform_value, values)` | taiga/base/filters.py:388 BaseRelatedFieldsFilter#_transform_value(). | no edge | exact python::.::taiga/base/filters.py::taiga/base/filters/BaseRelatedFieldsFilter#_prepare_fil… | dev has no node for the target |  |  |  |
| 9 | `taiga/export_import/serializers/serializers.py:251` | `if project.id not in _tasks_statuses_cache:` | taiga/export_import/serializers/cache.py:16 _tasks_statuses_cache. | no edge | import python::.::taiga/export_import/serializers/cache.py::taiga/export_import/serializers/cach… |  |  |  |  |
| 10 | `taiga/importers/github/importer.py:260` | `rewritten = GITHUB_INLINE_IMAGE_RE.sub(replace_image, markdown or "")` | taiga/importers/github/importer.py:235 GithubImporter#replace_image(). | variable::taiga/importers/github/importer.py::GITHUB_INLINE_IMAGE_RE | exact python::.::taiga/importers/github/importer.py::taiga/importers/github/importer/GithubImpo… | dev has no node for the target |  |  |  |
| 11 | `taiga/importers/github/importer.py:261` | `return GITHUB_INLINE_IMAGE_HTML_RE.sub(replace_image, rewritten)` | taiga/importers/github/importer.py:235 GithubImporter#replace_image(). | variable::taiga/importers/github/importer.py::GITHUB_INLINE_IMAGE_HTML_RE | exact python::.::taiga/importers/github/importer.py::taiga/importers/github/importer/GithubImpo… | dev has no node for the target |  |  |  |
| 12 | `taiga/mdrender/extensions/emojify.py:187` | `line = pattern.sub(emojify, line)` | taiga/mdrender/extensions/emojify.py:175 EmojifyPreprocessor#emojify(). | no edge | exact python::.::taiga/mdrender/extensions/emojify.py::taiga/mdrender/extensions/emojify/Emojif… | dev has no node for the target |  |  |  |
| 13 | `taiga/permissions/services.py:139` | `anon_permissions = list(map(lambda perm: perm[0], ANON_PERMISSIONS))` | taiga/permissions/choices.py:10 ANON_PERMISSIONS. | module:choices::ANON_PERMISSIONS | import python::.::taiga/permissions/choices.py::taiga/permissions/choices/ANON_PERMISSIONS. |  |  |  |  |
| 14 | `taiga/projects/custom_attributes/validators.py:74` | `model = models.IssueCustomAttribute` | taiga/projects/custom_attributes/models.py:79 IssueCustomAttribute# | no edge | import python::.::taiga/projects/custom_attributes/models.py::taiga/projects/custom_attributes/m… |  |  |  |  |
| 15 | `taiga/projects/issues/models.py:115` | `self.modified_date = timezone.now()` | taiga/projects/issues/models.py:87 Issue#modified_date. | no edge | name python::.::taiga/projects/issues/models.py::taiga/projects/issues/models/Issue#modified_d… |  |  |  |  |
| 16 | `taiga/projects/models.py:476` | `return Q(notify_policies__project_id=self.id) & ~Q(notify_policies__notify_level=NotifyLevel.none)` | taiga/projects/notifications/choices.py:15 NotifyLevel#none. | module:django.db.models::Q | import python::.::taiga/projects/notifications/choices.py::taiga/projects/notifications/choices/… |  |  |  |  |
| 17 | `taiga/projects/tagging/fields.py:69` | `self.validators.append(_validate_tag_field)` | taiga/projects/tagging/fields.py:62 TagsField#_validate_tag_field(). | no edge | exact python::.::taiga/projects/tagging/fields.py::taiga/projects/tagging/fields/TagsField#__in… | dev has no node for the target |  |  |  |
| 18 | `taiga/projects/tasks/api.py:56` | `filters.ModifiedDateFilter,` | taiga/base/filters.py:597 ModifiedDateFilter# | no edge | import python::.::taiga/base/filters.py::taiga/base/filters/ModifiedDateFilter# |  |  |  |  |
| 19 | `taiga/routers.py:86` | `router.register(r"issue-statuses", IssueStatusViewSet, base_name="issue-statuses")` | taiga/projects/api.py:898 IssueStatusViewSet# | no edge | import python::.::taiga/projects/api.py::taiga/projects/api/IssueStatusViewSet# |  |  |  |  |
| 20 | `taiga/routers.py:179` | `router.register(r"milestones", MilestoneViewSet,` | taiga/projects/milestones/api.py:39 MilestoneViewSet# | no edge | import python::.::taiga/projects/milestones/api.py::taiga/projects/milestones/api/MilestoneViewS… |  |  |  |  |
| 21 | `taiga/telemetry/tasks.py:28` | `'version': taiga.__version__,` | taiga/__init__.py:8 __version__. | no edge | exact python::.::taiga/__init__.py::taiga/__version__. | dev has no node for the target |  |  |  |
| 22 | `tests/integration/resources_permissions/test_modules_resources.py:201` | `with mock.patch.object(OCCResourceMixin, "_validate_and_update_version"):` | taiga/projects/occ/mixins.py:16 OCCResourceMixin# | no edge | import python::.::taiga/projects/occ/mixins.py::taiga/projects/occ/mixins/OCCResourceMixin# |  |  |  |  |
| 23 | `tests/integration/test_epics.py:332` | `with mock.patch.object(OCCResourceMixin, "_validate_and_update_version"):` | taiga/projects/occ/mixins.py:16 OCCResourceMixin# | no edge | import python::.::taiga/projects/occ/mixins.py::taiga/projects/occ/mixins/OCCResourceMixin# |  |  |  |  |
| 24 | `tests/integration/test_projects.py:713` | `logo.write(DUMMY_BMP_DATA)` | tests/utils.py:10 DUMMY_BMP_DATA. | module:utils::DUMMY_BMP_DATA | import python::.::tests/utils.py::tests/utils/DUMMY_BMP_DATA. |  |  |  |  |
| 25 | `tests/integration/test_users.py:750` | `avatar.write(DUMMY_BMP_DATA)` | tests/utils.py:10 DUMMY_BMP_DATA. | module:utils::DUMMY_BMP_DATA | import python::.::tests/utils.py::tests/utils/DUMMY_BMP_DATA. |  |  |  |  |

## Both miss (25 of 6702)
<!-- kind: both_miss -->

Neither engine has a right edge. Check the oracle target first; real rows are shared blind spots.

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `docker/config.py:108` | `if not CELERY_BROKER_URL:` | docker/config.py:107 CELERY_BROKER_URL. | no edge | unresolved unresolved::python::CELERY_BROKER_URL | reported (many_candidates) |  |  |  |
| 2 | `taiga/auth/authentication.py:46` | `for h in AUTH_HEADER_TYPES` | taiga/auth/authentication.py:39 AUTH_HEADER_TYPES. | no edge | unresolved unresolved::python::AUTH_HEADER_TYPES | reported (many_candidates) |  |  |  |
| 3 | `taiga/auth/utils.py:63` | `format_lazy = lazy(format_lazy, str)` | taiga/auth/utils.py:59 format_lazy(). | no edge | unresolved unresolved::python::format_lazy | reported (many_candidates) |  |  |  |
| 4 | `taiga/base/api/pagination.py:163` | `cutoff=self.max_paginate_by` | taiga/base/api/pagination.py:138 PaginationMixin#max_paginate_by. | no edge | no edge | silent |  |  |  |
| 5 | `taiga/base/api/serializers.py:711` | `models.AutoField: IntegerField,` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/IntegerField# | wrong_target |  |  |  |
| 6 | `taiga/base/api/serializers.py:712` | `models.FloatField: FloatField,` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/FloatField# | wrong_target |  |  |  |
| 7 | `taiga/base/api/serializers.py:721` | `models.EmailField: EmailField,` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/EmailField# | wrong_target |  |  |  |
| 8 | `taiga/base/api/serializers.py:727` | `models.BooleanField: BooleanField,` | taiga/base/api/fields.py:495 CharField# | no edge | import python::.::taiga/base/api/fields.py::taiga/base/api/fields/BooleanField# | wrong_target |  |  |  |
| 9 | `taiga/base/api/utils/__init__.py:62` | `raise NotAuthenticated` | taiga/base/exceptions.py:76 NotAuthenticated# | no edge | unresolved unresolved::python::NotAuthenticated | reported (many_candidates) |  |  |  |
| 10 | `taiga/importers/jira/agile.py:145` | `for sprint in self._client.get_agile("/board/{}/sprint".format(project_id))['values']:` | taiga/importers/jira/common.py:165 JiraImporterCommon#_client. | no edge | no edge | no_node; dev has no node for the target |  |  |  |
| 11 | `taiga/importers/trello/api.py:95` | `"is_backlog_activated": project.is_backlog_activated,` | taiga/projects/models.py:200 Project#is_backlog_activated. | no edge | unresolved unresolved::python::project.is_backlog_activated | reported (no_candidate) |  |  |  |
| 12 | `taiga/importers/trello/api.py:96` | `"is_kanban_activated": project.is_kanban_activated,` | taiga/projects/models.py:202 Project#is_kanban_activated. | no edge | unresolved unresolved::python::project.is_kanban_activated | reported (no_candidate) |  |  |  |
| 13 | `taiga/projects/management/commands/sample_data.py:435` | `task.status=self.sd.db_object_from_queryset(project.task_statuses.all())` | taiga/projects/tasks/models.py:43 Task#status. | no edge | unresolved unresolved::python::task.status | reported (no_candidate) |  |  |  |
| 14 | `taiga/projects/management/commands/sample_data.py:630` | `user=self.sd.db_object_from_queryset(User.objects.all())` | taiga/users/models.py:190 User#objects. | no edge | no edge | silent |  |  |  |
| 15 | `taiga/projects/userstories/api.py:98` | `if self.action == "list":` | taiga/base/api/viewsets.py:117 ViewSetMixin#action. | no edge | no edge | no_node; dev has no node for the target |  |  |  |
| 16 | `taiga/projects/userstories/services.py:339` | `start_order = after_userstory.kanban_order + 1` | taiga/projects/userstories/models.py:98 UserStory#kanban_order. | no edge | unresolved unresolved::python::after_userstory.kanban_order | reported (no_candidate) |  |  |  |
| 17 | `taiga/userstorage/api.py:34` | `if self.request.user.is_authenticated:` | taiga/base/api/views.py:434 APIView#request. | no edge | no edge | no_node; dev has no node for the target |  |  |  |
| 18 | `tests/integration/test_memberships.py:237` | `f.MembershipFactory(project=project, user=project.owner, is_admin=True)` | tests/factories.py:79 ProjectFactory#owner. | no edge | unresolved unresolved::python::project.owner | reported (dynamic_dispatch) |  |  |  |
| 19 | `tests/integration/test_notifications.py:850` | `role = f.RoleFactory.create(project=project, permissions=["view_issues"])` | tests/factories.py:91 RoleFactory# | no edge | no edge | silent |  |  |  |
| 20 | `tests/integration/test_projects.py:367` | `f.MembershipFactory(user=point_1.project.owner, project=point_1.project, is_admin=True)` | tests/factories.py:108 PointsFactory#project. | no edge | unresolved unresolved::python::point_1.project | reported (dynamic_dispatch) |  |  |  |
| 21 | `tests/integration/test_tasks.py:130` | `project = f.ProjectFactory.create(owner=user, default_task_status=None)` | tests/factories.py:69 ProjectFactory# | no edge | no edge | silent |  |  |  |
| 22 | `tests/integration/test_tasks.py:289` | `"status_id": us.project.default_task_status.id` | tests/factories.py:302 UserStoryFactory#project. | no edge | unresolved unresolved::python::us.project | reported (dynamic_dispatch) |  |  |  |
| 23 | `tests/integration/test_timeline.py:69` | `timeline = Timeline.objects.exclude(event_type="users.user.create")` | taiga/timeline/models.py:18 Timeline# | no edge | no edge | silent |  |  |  |
| 24 | `tests/integration/test_userstorage_api.py:62` | `client.login(username=user1.username, password=user1.username)` | tests/factories.py:196 UserFactory#username. | no edge | unresolved unresolved::python::user1.username | reported (dynamic_dispatch) |  |  |  |
| 25 | `tests/unit/auth/test_tokens.py:128` | `assert t.token == encoded_good_token` | taiga/auth/tokens.py:63 Token#token. | no edge | unresolved unresolved::python::t.token | no_node; dev has no node for the target |  |  |  |

## Wrong dev edges (15 of 58)
<!-- kind: dev_wrong -->

A dev edge whose target is none of the line's oracle targets. Check a few: this is where dev's precision goes.

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `taiga/auth/api.py:62` | `AUTH_HEADER_TYPES[0],` | taiga/auth/authentication.py:39 AUTH_HEADER_TYPES. | module:authentication::AUTH_HEADER_TYPES | no edge |  |  |  |  |
| 2 | `taiga/base/api/fields.py:562` | `self.choices = BLANK_CHOICE_DASH + self.choices` | taiga/base/api/fields.py:573 ChoiceField#choices. | module:django.db.models.fields::BLANK_CHOICE_DASH | python::.::taiga/base/api/fields.py::taiga/base/api/fields/ChoiceField#choices. |  |  |  |  |
| 3 | `taiga/base/api/fields.py:774` | `if format.lower() == ISO_8601:` | taiga/base/api/__init__.py:40 ISO_8601. | module:::ISO_8601 | python::.::taiga/base/api/__init__.py::taiga/base/api/ISO_8601. |  |  |  |  |
| 4 | `taiga/base/api/fields.py:857` | `if self.format.lower() == ISO_8601:` | taiga/base/api/__init__.py:40 ISO_8601.; taiga/base/api/fields.py:816 TimeField#format. | module:::ISO_8601 | python::.::taiga/base/api/__init__.py::taiga/base/api/ISO_8601. |  |  |  |  |
| 5 | `taiga/base/api/relations.py:99` | `self.empty_label = BLANK_CHOICE_DASH[0][1]` | taiga/base/api/relations.py:76 RelatedField#empty_label. | module:django.db.models.fields::BLANK_CHOICE_DASH | python::.::taiga/base/api/relations.py::taiga/base/api/relations/RelatedField#empty_label. |  |  |  |  |
| 6 | `taiga/base/api/utils/formatting.py:105` | `if apply_markdown:` | taiga/base/api/utils/formatting.py:49 apply_markdown(). | variable::taiga/base/api/utils/formatting.py::apply_markdown | no edge |  |  |  |  |
| 7 | `taiga/importers/management/commands/import_from_asana.py:84` | `users_bindings[user['id']] = User.objects.get(Q(username=username_or_email) \| Q(email=username_or_email))` | taiga/users/models.py:117 User#; taiga/users/models.py:190 User#objects. | module:django.db.models::Q | no edge |  |  |  |  |
| 8 | `taiga/importers/management/commands/import_from_pivotal.py:56` | `users_bindings[user['person']['id']] = User.objects.get(Q(email=user['person'].get('email', "not-valid")))` | taiga/users/models.py:117 User#; taiga/users/models.py:190 User#objects. | module:django.db.models::Q | no edge |  |  |  |  |
| 9 | `taiga/projects/models.py:424` | `members = members.filter(Q(is_admin=True) \| Q(user__id=self.owner.id))` | taiga/projects/models.py:181 Project#owner. | module:django.db.models::Q | no edge |  |  |  |  |
| 10 | `taiga/projects/notifications/api.py:30` | `Q(owner=self.request.user) \|` | taiga/base/api/request.py:247 Request#user(). | module:django.db.models::Q | no edge |  |  |  |  |
| 11 | `taiga/projects/notifications/api.py:31` | `Q(memberships__user=self.request.user)` | taiga/base/api/request.py:247 Request#user(). | module:django.db.models::Q | no edge |  |  |  |  |
| 12 | `taiga/projects/notifications/api.py:44` | `Q(project__owner=self.request.user) \| Q(project__memberships__user=self.request.user)` | taiga/base/api/request.py:247 Request#user(). | module:django.db.models::Q | no edge |  |  |  |  |
| 13 | `tests/integration/test_projects.py:696` | `logo.write(DUMMY_BMP_DATA)` | tests/utils.py:10 DUMMY_BMP_DATA. | module:utils::DUMMY_BMP_DATA | python::.::tests/utils.py::tests/utils/DUMMY_BMP_DATA. |  |  |  |  |
| 14 | `tests/integration/test_users.py:735` | `avatar.write(DUMMY_BMP_DATA)` | tests/utils.py:10 DUMMY_BMP_DATA. | module:utils::DUMMY_BMP_DATA | python::.::tests/utils.py::tests/utils/DUMMY_BMP_DATA. |  |  |  |  |
| 15 | `tests/unit/auth/test_backends.py:122` | `hmac_token = hmac_token_backend.encode(payload)` | tests/unit/auth/test_backends.py:94 hmac_token_backend. | variable::tests/unit/auth/test_backends.py::payload | no edge |  |  |  |  |

## v2 edges the score cannot judge (10 of 356)
<!-- kind: v2_unscored -->

v2 edges on lines where the oracle has no call with a target v2 has a node for. Not in any score. Look for calls the oracle misses (v2 right, oracle silent) and for v2 edges that are plainly wrong.

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `taiga/base/api/fields.py:481` | `self.default = False` | no oracle call with a target | no edge | name python::.::taiga/base/api/fields.py::taiga/base/api/fields/WritableField#default. (at reference site: no) |  |  |  |  |
| 2 | `taiga/base/api/fields.py:558` | `self.empty = kwargs.pop("empty", "")` | no oracle call with a target | no edge | name python::.::taiga/base/api/fields.py::taiga/base/api/fields/Field#empty. (at reference site: no) |  |  |  |  |
| 3 | `taiga/base/api/serializers.py:704` | `class ModelSerializer((six.with_metaclass(SerializerMetaclass, BaseSerializer))):` | no oracle call with a target | no edge | name python::.::taiga/base/api/serializers.py::taiga/base/api/serializers/SerializerMetaclass# (at reference site: no) |  |  |  |  |
| 4 | `taiga/projects/models.py:1245` | `self.tags = project.tags` | no oracle call with a target | no edge | name python::.::taiga/projects/tagging/models.py::taiga/projects/tagging/models/TaggedMixin#ta… (at reference site: no) |  |  |  |  |
| 5 | `taiga/projects/models.py:1246` | `self.tags_colors = project.tags_colors` | no oracle call with a target | no edge | name python::.::taiga/projects/tagging/models.py::taiga/projects/tagging/models/TagsColorsMixi… (at reference site: no) |  |  |  |  |
| 6 | `tests/integration/test_importer_api.py:1474` | `client.login(user)` | no oracle call with a target | no edge | name python::.::tests/integration/test_feedback.py::tests/integration/test_feedback/user().#f9… (at reference site: yes) |  |  |  |  |
| 7 | `tests/integration/test_issues.py:815` | `client.login(user)` | no oracle call with a target | no edge | name python::.::tests/integration/test_feedback.py::tests/integration/test_feedback/user().#f9… (at reference site: yes) |  |  |  |  |
| 8 | `tests/integration/test_projects.py:2131` | `client.login(user)` | no oracle call with a target | no edge | name python::.::tests/integration/test_feedback.py::tests/integration/test_feedback/user().#f9… (at reference site: yes) |  |  |  |  |
| 9 | `tests/integration/test_userstories.py:722` | `client.login(user)` | no oracle call with a target | no edge | name python::.::tests/integration/test_feedback.py::tests/integration/test_feedback/user().#f9… (at reference site: yes) |  |  |  |  |
| 10 | `tests/unit/auth/test_authentication.py:89` | `reload(authentication)` | no oracle call with a target | no edge | import python::.::taiga/auth/authentication.py:: (at reference site: yes) |  |  |  |  |

## dev edges the score cannot judge (10 of 142)
<!-- kind: dev_unscored -->

The same for dev.

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `scripts/manage_translations.py:192` | `stdout=PIPE, stderr=PIPE, shell=True)` | no oracle call with a target | module:subprocess::PIPE | no edge |  |  |  |  |
| 2 | `taiga/base/filters.py:492` | `return Q(query)` | no oracle call with a target | module:django.db.models::Q | no edge |  |  |  |  |
| 3 | `taiga/base/routers.py:181` | `ret.append(Route(` | no oracle call with a target | variable::taiga/base/routers.py::Route | no edge |  |  |  |  |
| 4 | `taiga/front/sitemaps/tasks.py:23` | `queryset = task_model.objects.filter(Q(project__is_private=False) \|` | no oracle call with a target | module:django.db.models::Q | no edge |  |  |  |  |
| 5 | `taiga/projects/history/freeze_impl.py:158` | `values["type"] = _get_issue_type_values(diff["type"])` | no oracle call with a target | variable::taiga/projects/history/freeze_impl.py::_get_issue_type_values | no edge |  |  |  |  |
| 6 | `taiga/projects/services/projects.py:49` | `current_memberships += (Membership.objects.filter(Q(project__is_private=not project.is_private,  # public/private member` | no oracle call with a target | module:django.db.models::Q | no edge |  |  |  |  |
| 7 | `taiga/projects/services/projects.py:136` | `current_memberships = (Membership.objects.filter(Q(project__is_private=project.is_private,  # public/private members` | no oracle call with a target | module:django.db.models::Q | no edge |  |  |  |  |
| 8 | `taiga/projects/userstories/filters.py:105` | `qs_method(Q(get_assigned_users_filter(user_story_model, memberships)))` | no oracle call with a target | module:django.db.models::Q | no edge |  |  |  |  |
| 9 | `taiga/timeline/api.py:71` | `qs = qs.exclude(Q(event_type=["issues.issue.change",` | no oracle call with a target | module:django.db.models::Q | no edge |  |  |  |  |
| 10 | `taiga/timeline/service.py:168` | `tl_filter \|= Q(project__is_private=True,` | no oracle call with a target | module:django.db.models::Q | no edge |  |  |  |  |

## Both right (spot check) (10 of 538)
<!-- kind: both_right -->

The machine says both engines are right. Check a few: if these are wrong, every score is too high.

| # | file:line | source | oracle | dev | v2 | notes | verdict | cause | reason true |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `taiga/hooks/gitlab/event_hooks.py:43` | `ISSUE_ACTION_CREATE,` | taiga/hooks/event_hooks.py:25 ISSUE_ACTION_CREATE. | variable::taiga/hooks/event_hooks.py::ISSUE_ACTION_CREATE | import python::.::taiga/hooks/event_hooks.py::taiga/hooks/event_hooks/ISSUE_ACTION_CREATE. |  |  |  |  |
| 2 | `taiga/projects/management/commands/sample_data.py:355` | `subject=self.sd.choice(SUBJECT_CHOICES),` | taiga/projects/management/commands/sample_data.py:71 SUBJECT_CHOICES. | variable::taiga/projects/management/commands/sample_data.py::SUBJECT_CHOICES | name python::.::taiga/projects/management/commands/sample_data.py::taiga/projects/management/c… |  |  |  |  |
| 3 | `tests/integration/resources_permissions/test_wiki_resources.py:370` | `role__permissions=list(map(lambda x: x[0], MEMBERS_PERMISSIONS)))` | taiga/permissions/choices.py:21 MEMBERS_PERMISSIONS. | variable::taiga/permissions/choices.py::MEMBERS_PERMISSIONS | import python::.::taiga/permissions/choices.py::taiga/permissions/choices/MEMBERS_PERMISSIONS. |  |  |  |  |
| 4 | `tests/integration/test_hooks_gitlab.py:1255` | `payload = deepcopy(issue_comment_base_payload)` | tests/integration/test_hooks_gitlab.py:353 issue_comment_base_payload. | variable::tests/integration/test_hooks_gitlab.py::issue_comment_base_payload | name python::.::tests/integration/test_hooks_gitlab.py::tests/integration/test_hooks_gitlab/is… |  |  |  |  |
| 5 | `tests/integration/test_userstories.py:1494` | `public_permissions=list(map(lambda x: x[0], ANON_PERMISSIONS)))` | taiga/permissions/choices.py:10 ANON_PERMISSIONS. | variable::taiga/permissions/choices.py::ANON_PERMISSIONS | import python::.::taiga/permissions/choices.py::taiga/permissions/choices/ANON_PERMISSIONS. |  |  |  |  |
| 6 | `tests/integration/test_userstories.py:1499` | `role__permissions=list(map(lambda x: x[0], MEMBERS_PERMISSIONS)))` | taiga/permissions/choices.py:21 MEMBERS_PERMISSIONS. | variable::taiga/permissions/choices.py::MEMBERS_PERMISSIONS | import python::.::taiga/permissions/choices.py::taiga/permissions/choices/MEMBERS_PERMISSIONS. |  |  |  |  |
| 7 | `tests/unit/auth/test_authentication.py:71` | `assert backend.get_header(request) == fake_header` | tests/unit/auth/test_authentication.py:57 fake_header. | variable::tests/unit/auth/test_authentication.py::fake_header | name python::.::tests/unit/auth/test_authentication.py::tests/unit/auth/test_authentication/fa… |  |  |  |  |
| 8 | `tests/unit/auth/test_authentication.py:76` | `request = factory.get('/test-url/', HTTP_X_ACCESS_TOKEN=fake_header)` | tests/unit/auth/test_authentication.py:57 fake_header. | variable::tests/unit/auth/test_authentication.py::factory; variable::tests/unit/auth/test_authentication.py::fake_header | name python::.::tests/unit/auth/test_authentication.py::tests/unit/auth/test_authentication/fa… | dev has 2 targets on this line |  |  |  |
| 9 | `tests/unit/auth/test_backends.py:269` | `token = jwt.encode(payload, PRIVATE_KEY, algorithm='RS256')` | tests/unit/auth/test_backends.py:47 PRIVATE_KEY. | variable::tests/unit/auth/test_backends.py::PRIVATE_KEY; variable::tests/unit/auth/test_backends.py::payload | name python::.::tests/unit/auth/test_backends.py::tests/unit/auth/test_backends/PRIVATE_KEY. | dev has 2 targets on this line |  |  |  |
| 10 | `tests/unit/test_mdrender.py:313` | `result = render(dummy_project, md)` | tests/unit/test_mdrender.py:17 dummy_project. | variable::tests/unit/test_mdrender.py::dummy_project | name python::.::tests/unit/test_mdrender.py::tests/unit/test_mdrender/dummy_project. |  |  |  |  |

