from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from website import views

urlpatterns = format_suffix_patterns([
    url(r'^attachments/',
        views.AttachmentList.as_view(), name='attachment-list'),
    url(r'^attachment/(?P<pk>[0-9]+)/$',
        views.AttachmentListDetail.as_view(), name='attachment-list-detail'),
    url(r'^attachment/$',
        views.CreateAttachments.as_view(), name='create-attachment'),

    url(r'post/$', views.CreatePost.as_view(), name='create-post'),
    url(r'posts/$', views.PostList.as_view(), name='post-list'),
    url(r'post/(?P<pk>[0-9]+)/$', views.PostListDetail.as_view(),
        name='post-list-detail'),

    url(r'comment/$', views.CreateComments.as_view(), name='create-comment'),
    url(r'comments/$', views.CommentList.as_view(), name='comment-list'),

    url(r'element-word/$', views.CreateElementWord.as_view(),
        name='create-element=words'),
    url(r'element-words/$', views.ElementWordList.as_view(),
        name='element-word-list'),
    url(r'element-word/(?P<pk>[0-9]+)/$', views.ElementWordListDetail.as_view(),
        name='element-word-list-detail'),

    url(r'submission/$', views.CreateSubmission.as_view(),
        name='create-submission'),
    url(r'submissions/$', views.SubmissionList.as_view(), name="submission-list"),
    url(r'submission/(?P<pk>[0-9]+)/$', views.SubmissionListDetail.as_view(),
        name='submission-list-detail'),

    url(r'task/$', views.CreateTask.as_view(), name="create-task"),
    url(r'tasks/$', views.TaskList.as_view(), name="task-list"),
    url(r'task/(?P<pk>[0-9]+)/$', views.TaskListDetail.as_view(), name='task-list-detail'),

    url(r'event/$', views.CreateEvent.as_view(), name="create-event"),
    url(r'events/$', views.EventsList.as_view(), name="event-list"),
    url(r'event/(?P<pk>[0-9]+)/$', views.EventListDetail.as_view(), name='event-list-detail'),
])