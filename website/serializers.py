from rest_framework import serializers
from website.models import (
    Attachment, Post, Comments,
    ElementWord, Task, Events,
    Submission, PostType, TaskType
)


class PostTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostType
        fields = ('id', 'post_type')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'summary', 'content', 'post_type')


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'post', 'author', 'comment')


class ElementWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementWord
        fields = ('id', 'author', 'testimony', 'approved')


class TaskTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskType
        fields = ('id', 'task_type')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'start_time',
                  'end_time', 'task_type', 'amount', 'expected_amount'
        )


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ('id', 'user', 'task', 'file')


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id', 'name', 'description', 'location',
                  'start_time', 'end_time',
                  'attendee', 'expected_attendee'
        )


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ('id', 'filename', 'url', 'events')
