from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from kenalan import views, utils

# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^token/$',
        views.TokenList.as_view(), name='token-list'),
    url(r'^token/create$',
        views.TokenCreate.as_view(), name='token-create'),
    url(r'^token/(?P<pk>[0-9]+)/$',
        views.TokenDetail.as_view(), name='token-detail'),
   
    url(r'^kenalan/$',
        views.KenalanList.as_view(), name='kenalan-list'),
    url(r'^kenalan/(?P<pk>[0-9]+)/$',
        views.KenalanDetail.as_view(), name='kenalan-detail'),
   
    url(r'^kenalan-status/$',
        views.KenalanStatusList.as_view(), name='kenalan-status-list'),
    url(r'^kenalan-status/(?P<pk>[0-9]+)/$',
        views.KenalanStatusDetail.as_view(), name='kenalan-status-detail'),
   
    url(r'^kenalan-detail/$',
        views.KenalanDetailList.as_view(), name='kenalan-detail-list'),
    url(r'^kenalan-detail/(?P<pk>[0-9]+)/$',
        views.KenalanDetailDetail.as_view(), name='kenalan-detail-detail'),

    url(r'^generate-token/$',
        utils.generate_token, name='generate-token'),
    url(r'^delete-expired-token/$',
        utils.delete_expired_token, name='delete-expired-token')

])