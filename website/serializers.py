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
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    post_type = serializers.PrimaryKeyRelatedField(read_only=True)
    attachment = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = Post
        fields = ('title', 'author', 'summary', 'content', 'post_type', 'attachment')


class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Comments
        fields = ('post', 'author', 'comment')


class ElementWordSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = ElementWord
        fields = ('author', 'testimony', 'approved')


class SubmissionSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    attachment = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = Submission
        fields = ('user', 'attachment')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    submission = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Task
        fields = ('name', 'description', 'author', 'start_time',
                  'end_time', 'type', 'submission', 'amount',
                  'expected_amount'
        )


class EventsSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    submission = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Events
        fields = ('name', 'description', 'author', 'location',
                  'start_time', 'end_time', 'type', 'submission',
                  'attendee', 'expected_attendee'
        )
