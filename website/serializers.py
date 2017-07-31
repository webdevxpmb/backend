from rest_framework import serializers
from website.models import (
    Post, Comment, ElementWord,
    Task, Event, Submission,
    PostType,
    Album, EventStatistic,
    TaskStatistic, UserStatistic,
)
from account.serializers import UserSerializer


class PostTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostType
        fields = ('id', 'post_type')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'summary', 'content',
                  'post_type', 'attachment_link', 'created_at', 'updated_at')


class GetPostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    post_type = PostTypeSerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'summary', 'content',
                  'post_type', 'attachment_link', 'created_at', 'updated_at')


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'comment', 'created_at', 'updated_at')


class GetCommentsSerializer(serializers.ModelSerializer):
    post = GetPostSerializer()
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'comment', 'created_at', 'updated_at')


class ElementWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementWord
        fields = ('id', 'author', 'testimony', 'approved', 'created_at', 'updated_at')


class GetElementWordSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = ElementWord
        fields = ('id', 'author', 'testimony', 'approved', 'created_at', 'updated_at')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'start_time',
                  'end_time', 'is_kenalan', 'expected_amount_omega',
                  'expected_amount_capung', 'expected_amount_orion',
                  'expected_amount_alumni', 'created_at', 'updated_at')


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ('id', 'user', 'task', 'file_link')


class GetSubmissionSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    task = TaskSerializer()

    class Meta:
        model = Submission
        fields = ('id', 'user', 'task', 'file_link')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'location',
                  'start_time', 'end_time', 'expected_attendee',
                  'attachment_link', 'created_at', 'updated_at')


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'name', 'album_link', 'created_at', 'updated_at')


class TaskStatisticSerializer(serializers.ModelSerializer):
    task = TaskSerializer()
    class Meta:
        model = TaskStatistic
        fields = ('id', 'task', 'amount', 'created_at', 'updated_at')


class EventStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventStatistic
        fields = ('id', 'event', 'attendee', 'on_time', 'late', 'permission',
                  'absent', 'created_at', 'updated_at')


class GetEventStatisticSerializer(serializers.ModelSerializer):
    event = EventSerializer()
    class Meta:
        model = EventStatistic
        fields = ('id', 'event', 'attendee', 'on_time', 'late', 'permission',
                  'absent', 'created_at', 'updated_at')


class UserStatisticSerializer(serializers.ModelSerializer):
    task = TaskSerializer()
    class Meta:
        model = UserStatistic
        fields = ('id', 'user', 'name', 'task', 'amount_omega',
                  'amount_capung', 'amount_orion', 'amount_alumni')
