# taiga-back (python): HANDLES, graph v2 against dev

Engines: v2 `5a6074642e06`, dev `25ae40bf8662`. No oracle: you judge each row.

## Counts

v2 4 pairs, dev 449 pairs (dev types: ROUTE_HANDLER 364, MIDDLEWARE 85).
Both 0, only v2 4, only dev 449; agreement 0.0% of the union.
Pairs are matched on (file, name with only letters and digits) of both ends, so the engines' different spellings of one test or scope meet; an edge to a route, data or package node (v2) has no dev counterpart. v2 unresolved and external edges are left out.

Verdict: `confirmed` (the group is right), `v2 wrong`, `dev wrong`, `both wrong`, or `?`. Cause: one short phrase.

## Only v2 has it (4 of 4)
<!-- group: only_v2 -->

v2 has this edge, dev does not. Check: is the edge real in the code (v2 gain) or wrong (v2 wrong)?

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|
| 1 | `surface::taiga.base.routers::http_route::ALL::/{?}` | `taiga/base/routers.py::DRFDefaultRouter.get_api_root_view` | yes | no | taiga/base/routers.py:298 |  |  |
| 2 | `surface::taiga.export_import.api::http_route::ALL::/{?}/{?}` | `taiga/base/response.py::Ok` | yes | no | taiga/export_import/api.py:81 |  |  |
| 3 | `surface::taiga.feedback.apps::http_route::ALL::/{?}/api/v1` | `` | yes | no | - |  |  |
| 4 | `surface::taiga.timeline.serializers::http_route::ALL::/{?}/{?}` | `taiga/base/utils/thumbnails.py::get_thumbnail_url` | yes | no | taiga/timeline/serializers.py:83 |  |  |

## Only dev has it (25 of 449)
<!-- group: only_dev -->

dev has this edge, v2 does not. Check: is it real (a v2 gap) or wrong (dev wrong)?

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|
| 1 | `route:ALL:/api/v1/history/task/` | `taiga/projects/history/api.py::TaskHistory` | no | ROUTE_HANDLER | - |  |  |
| 2 | `route:ALL:/api/v1/issue-due-dates/{id}/` | `taiga/projects/api.py::IssueDueDateViewSet` | no | ROUTE_HANDLER | - |  |  |
| 3 | `route:ALL:/api/v1/projects/(?P<resource_id>\d+)/fans/{id}/` | `taiga/projects/api.py::ProjectFansViewSet` | no | ROUTE_HANDLER | - |  |  |
| 4 | `route:ALL:/api/v1/roles/{id}/` | `taiga/users/api.py::RolesViewSet` | no | ROUTE_HANDLER | - |  |  |
| 5 | `route:ALL:/api/v1/sections/` | `taiga/projects/settings/api.py::SectionsViewSet` | no | ROUTE_HANDLER | - |  |  |
| 6 | `route:ALL:/api/v1/userstories/(?P<resource_id>\d+)/voters/` | `taiga/projects/userstories/api.py::UserStoryVotersViewSet` | no | ROUTE_HANDLER | - |  |  |
| 7 | `route:ALL:/api/v1/wiki-links/` | `taiga/projects/wiki/api.py::WikiLinkViewSet` | no | ROUTE_HANDLER | - |  |  |
| 8 | `route:ALL:/api/v1/wiki/(?P<resource_id>\d+)/watchers/{id}/` | `taiga/projects/wiki/api.py::WikiWatchersViewSet` | no | ROUTE_HANDLER | - |  |  |
| 9 | `route:ALL:/api/v1/wiki/attachments/{id}/` | `taiga/projects/attachments/api.py::WikiAttachmentViewSet` | no | ROUTE_HANDLER | - |  |  |
| 10 | `route:GET:/api/v1/history/wiki/{id}/comment_versions/` | `taiga/projects/history/api.py::HistoryViewSet.comment_versions` | no | ROUTE_HANDLER | - |  |  |
| 11 | `route:GET:/api/v1/projects/{id}/issues_stats/` | `taiga/projects/api.py::ProjectViewSet.issues_stats` | no | ROUTE_HANDLER | - |  |  |
| 12 | `route:GET:/api/v1/projects/{id}/modules/` | `taiga/projects/api.py::ProjectViewSet.modules` | no | ROUTE_HANDLER | - |  |  |
| 13 | `route:GET:/api/v1/userstories/by_ref/` | `taiga/projects/mixins/by_ref.py::ByRefMixin.by_ref` | no | ROUTE_HANDLER | - |  |  |
| 14 | `route:POST:/api/v1/epic-statuses/bulk_update_order/` | `taiga/projects/mixins/ordering.py::BulkUpdateOrderMixin.bulk_update_order` | no | ROUTE_HANDLER | - |  |  |
| 15 | `route:POST:/api/v1/history/wiki/{id}/undelete_comment/` | `taiga/projects/history/api.py::HistoryViewSet.undelete_comment` | no | ROUTE_HANDLER | - |  |  |
| 16 | `route:POST:/api/v1/importer/{id}/wiki_page/` | `taiga/export_import/api.py::ProjectImporterViewSet.wiki_page` | no | ROUTE_HANDLER | - |  |  |
| 17 | `route:POST:/api/v1/issues/{id}/upvote/` | `taiga/projects/votes/mixins/viewsets.py::VotedResourceMixin.upvote` | no | ROUTE_HANDLER | - |  |  |
| 18 | `route:POST:/api/v1/projects/{id}/like/` | `taiga/projects/likes/mixins/viewsets.py::LikedResourceMixin.like` | no | ROUTE_HANDLER | - |  |  |
| 19 | `route:POST:/api/v1/projects/{id}/regenerate_userstories_csv_uuid/` | `taiga/projects/api.py::ProjectViewSet.regenerate_userstories_csv_uuid` | no | ROUTE_HANDLER | - |  |  |
| 20 | `route:POST:/api/v1/userstories/{id}/upvote/` | `taiga/projects/votes/mixins/viewsets.py::VotedResourceMixin.upvote` | no | ROUTE_HANDLER | - |  |  |
| 21 | `route:POST:/api/v1/userstory-due-dates/create_default/` | `taiga/projects/api.py::UserStoryDueDateViewSet.create_default` | no | ROUTE_HANDLER | - |  |  |
| 22 | `taiga/locale/api.py::LocalesPermission` | `taiga/locale/api.py::LocalesViewSet` | no | MIDDLEWARE | - |  |  |
| 23 | `taiga/projects/api.py::IssueTypePermission` | `taiga/projects/api.py::IssueTypeViewSet` | no | MIDDLEWARE | - |  |  |
| 24 | `taiga/projects/history/api.py::EpicHistoryPermission` | `taiga/projects/history/api.py::EpicHistory` | no | MIDDLEWARE | - |  |  |
| 25 | `taiga/projects/settings/api.py::UserProjectSettingsPermission` | `taiga/projects/settings/api.py::UserProjectSettingsViewSet` | no | MIDDLEWARE | - |  |  |

## Both have it (spot check) (0 of 0)
<!-- group: both -->

Both engines agree. Check a few: an agreement can still be wrong.

| # | from | to | v2 | dev | where | verdict | cause |
|---|---|---|---|---|---|---|---|

