from rest_framework import serializers
from django.contrib.auth.models import User
from website.models import (
    Attachment, PostType, Post, Comments,
    ElementWord, Task, Events
)


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ('id', 'filename', 'url')


class PostTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostType
        fields = ('id', 'post_type')

class PostSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # post_type = serializers.PrimaryKeyRelatedField(queryset=PostType.objects.all())
    # attachment = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'summary', 'content', 'post_type', 'attachment')


class CommentsSerializer(serializers.ModelSerializer):
    # post = serializers.PrimaryKeyRelatedField(read_only=True)
    # author = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Comments
        fields = ('id', 'post', 'author', 'comment')


class ElementWordSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = ElementWord
        fields = ('id', 'author', 'testimony', 'approved')
        # read_only_fields = ('approved',)


# class SubmissionSerializer(serializers.ModelSerializer):
#     # user = serializers.PrimaryKeyRelatedField(read_only=True)
#     # attachment = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
#     class Meta:
#         model = Submission
#         fields = ('id', 'user', 'attachment')


class TaskSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(read_only=True)
    # submission = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'author', 'start_time',
                  'end_time', 'type', 'amount',
                  'expected_amount'
        )


class EventsSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(read_only=True)
    # submission = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Events
        fields = ('id', 'name', 'description', 'author', 'location',
                  'start_time', 'end_time', 'type',
                  'attendee', 'expected_attendee'
        )
