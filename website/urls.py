from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from website import views

urlpatterns = format_suffix_patterns([
    url(r'attachment/',
        views.AttachmentList.as_view(), name='attachment-list'),
    url(r'attachment/(?P<pk>[0-9]+)/$',
        views.AttachmentDetail.as_view(), name='attachment-detail'),

    url(r'post-type/$',
        views.PostTypeList.as_view(), name='post-type-list'),
    url(r'post-type/(?P<pk>[0-9]+)/$',
        views.PostTypeDetail.as_view(), name='post-type-detail'),

    url(r'post/$',
        views.PostList.as_view(), name='post-list'),
    url(r'post/(?P<pk>[0-9]+)/$',
        views.PostDetail.as_view(), name='post-detail'),

    url(r'comment/$',
        views.CommentList.as_view(), name='comment-list'),
    url(r'comment/(?P<pk>[0-9]+)/$',
        views.CommentDetail.as_view(), name='comment-detail'),

    url(r'element-word/$',
        views.ElementWordList.as_view(), name='element-word-list'),
    url(r'element-word/(?P<pk>[0-9]+)/$',
        views.ElementWordDetail.as_view(), name='element-word-detail'),

    url(r'submission/$',
        views.SubmissionList.as_view(), name="submission-list"),
    url(r'submission/(?P<pk>[0-9]+)/$',
        views.SubmissionDetail.as_view(), name='submission-detail'),

    url(r'task-type/$',
        views.TaskTypeList.as_view(), name="task-type-list"),
    url(r'task-type/(?P<pk>[0-9]+)/$',
        views.TaskTypeDetail.as_view(), name='task-type-detail'),

    url(r'task/$',
        views.TaskList.as_view(), name="task-list"),
    url(r'task/(?P<pk>[0-9]+)/$',
        views.TaskDetail.as_view(), name='task-detail'),

    url(r'event/$',
        views.EventsList.as_view(), name="event-list"),
    url(r'event/(?P<pk>[0-9]+)/$',
        views.EventDetail.as_view(), name='event-detail'),
])
