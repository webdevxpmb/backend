from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from kenalan import views, utils

# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'/token/$',
        views.TokenList.as_view(), name='token-list'),

    url(r'/kenalan/$',
        views.KenalanList.as_view(), name='kenalan-list'),
    url(r'/kenalan/(?P<pk>[0-9]+)/$',
        views.KenalanDetail.as_view(), name='kenalan-detail'),

    url(r'/kenalan-status/$',
        views.KenalanStatusList.as_view(), name='kenalanstatus-list'),
    url(r'/kenalan-status/(?P<pk>[0-9]+)/$',
        views.KenalanStatusDetail.as_view(), name='kenalanstatus-detail'),

    url(r'/detail-kenalan/$',
        views.DetailKenalanList.as_view(), name='detailkenalan-list'),
    url(r'/detail-kenalan/(?P<pk>[0-9]+)/$',
        views.DetailKenalanDetail.as_view(), name='detailkenalan-detail', ),

    url(r'/friend-list/$',
        views.FriendList.as_view(), name='friend-list'),

    url(r'/generate-token/$',
        utils.generate_token, name='generate-token'),

    url(r'delete-expired-token/$',
        utils.delete_expired_token, name='delete-expired-token'),

    url(r'create-kenalan/$',
        utils.create_kenalan_by_token, name='create-kenalan'),


])
