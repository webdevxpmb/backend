from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from account import views, utils

# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^user/$',
        views.UserList.as_view(), name='user-list'),
    url(r'^user/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(), name='user-detail'),

    url(r'^role/$',
        views.RoleList.as_view(), name='role-list'),
    url(r'^role/(?P<pk>[0-9]+)/$',
        views.RoleDetail.as_view(), name='role-detail'),
   
    url(r'^angkatan/$',
        views.AngkatanList.as_view(), name='angkatan-list'),
    url(r'^angkatan/(?P<pk>[0-9]+)/$',
        views.AngkatanDetail.as_view(), name='angkatan-detail'),
   
    url(r'^user-profile/$',
        views.UserProfileList.as_view(), name='userprofile-list'),
    url(r'^user-profile/(?P<pk>[0-9]+)/$',
        views.UserProfileDetail.as_view(), name='userprofile-detail'),

])