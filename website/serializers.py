from rest_framework import serializers
from django.contrib.auth.models import User
from website.models import (
    Attachment, PostType, Post, Comments,
    ElementWord, Submission, Task, Events
)


class AttachmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attachment
        fields = ('filename', 'url')


class PostTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostType
        fields = ('post_type')


class PostSerializer(serializers.HyperlinkedModelSerializer):
