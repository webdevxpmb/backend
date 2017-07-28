from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from website import views

urlpatterns = format_suffix_patterns([
    url(r'post-type/$',
        views.PostTypeList.as_view(), name='posttype-list'),
    url(r'post-type/(?P<pk>[0-9]+)/$',
        views.PostTypeDetail.as_view(), name='posttype-detail'),

    url(r'post/$',
        views.PostList.as_view(), name='post-list'),
    url(r'post/(?P<pk>[0-9]+)/$',
        views.PostDetail.as_view(), name='post-detail'),
    url(r'post-update/(?P<pk>[0-9]+)/$',
        views.PostDetailUpdate.as_view(), name='postupdate-detail'),

    url(r'comment/$',
        views.CommentList.as_view(), name='comment-list'),
    url(r'comment/(?P<pk>[0-9]+)/$',
        views.CommentDetail.as_view(), name='comment-detail'),

    url(r'element-word/$',
        views.ElementWordList.as_view(), name='elementword-list'),
    url(r'element-word/(?P<pk>[0-9]+)/$',
        views.ElementWordDetail.as_view(), name='elementword-detail'),

    url(r'submission/$',
        views.SubmissionList.as_view(), name="submission-list"),
    url(r'submission/(?P<pk>[0-9]+)/$',
        views.SubmissionDetail.as_view(), name='submission-detail'),

    url(r'task/$',
        views.TaskList.as_view(), name="task-list"),
    url(r'task/(?P<pk>[0-9]+)/$',
        views.TaskDetail.as_view(), name='task-detail'),

    url(r'event/$',
        views.EventList.as_view(), name="event-list"),
    url(r'event/(?P<pk>[0-9]+)/$',
        views.EventDetail.as_view(), name='event-detail'),

    url(r'album/$',
        views.AlbumList.as_view(), name="album-list"),
    url(r'album/(?P<pk>[0-9]+)/$',
        views.AlbumDetail.as_view(), name='album-detail'),

    url(r'task-statistic/$',
        views.TaskStatisticList.as_view(), name="taskstatistic-list"),
    url(r'task-statistic/(?P<pk>[0-9]+)/$',
        views.TaskStatisticDetail.as_view(), name='taskstatistic-detail'),

    url(r'kenalan-statistic/$',
        views.KenalanStatisticList.as_view(), name="kenalanstatistic-list"),
    url(r'kenalan-statistic/(?P<pk>[0-9]+)/$',
        views.KenalanStatisticDetail.as_view(), name='kenalanstatistic-detail'),

    url(r'event-statistic/$',
        views.EventStatisticList.as_view(), name="eventstatistic-list"),
    url(r'event-statistic/(?P<pk>[0-9]+)/$',
        views.EventStatisticDetail.as_view(), name='eventstatistic-detail'),



])
