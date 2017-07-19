from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from website import views

urlpatterns = format_suffix_patterns([
    url(r'^attachments/$',
        views.AttachmentList.as_view(), name='attachment-list')
])