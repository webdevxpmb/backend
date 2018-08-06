import uuid
from rest_framework import serializers
from website.models import (
    Post, Comment, ElementWord,
    Task, Event, Submission,
    PostType,
    Album, EventStatistic,
    TaskStatistic, UserStatistic,
    Vote, VoteOption, Voting, File
)
from account.serializers import UserSerializer
from dropbox import Dropbox

class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model = File
        fields = '__all__'

    def create(self, validated_data):
        dbx = Dropbox('bTgof9agI8AAAAAAAAAACqcCQi31fo9vEaDVqkuU3RkONXR_dbyoHE6difvZCU4i')
        filename = str(uuid.uuid4()) + '.' + validated_data['file'].name.split('.')[1]
        print(filename)
        dbx.files_upload(validated_data['file'].file.getvalue(), '/' + filename)
        result = dbx.sharing_create_shared_link('/' + filename)
        validated_data['file'] = result.url
        return validated_data

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
        fields = ('id', 'title', 'author', 'cover_image_link', 'summary', 'content',
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
        fields = ('id', 'name', 'description', 'start_time', 'attachment_link',
                  'end_time', 'is_kenalan', 'expected_amount_tarung',
                  'expected_amount_omega', 'expected_amount_capung',
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
                  'amount_capung', 'amount_orion', 'amount_alumni',
                  'amount_approved_omega', 'amount_approved_capung',
                  'amount_approved_orion', 'amount_approved_alumni')


class VoteOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteOption
        fields = ('id', 'name', 'description', 'vote', 'total_voters', 'created_at', 'updated_at',)


class GetVoteSerializer(serializers.ModelSerializer):
    options = VoteOptionSerializer(many=True)

    class Meta:
        model = Vote
        fields = ('id', 'title', 'description', 'start_time', 'end_time', 'total_voters', 'options', 'created_at', 'updated_at')


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('id', 'title', 'description', 'start_time', 'end_time', 'total_voters', 'created_at', 'updated_at')


class GetVoteOptionSerializer(serializers.ModelSerializer):
    vote = VoteSerializer()

    class Meta:
        model = VoteOption
        fields = ('id', 'name', 'description', 'vote', 'total_voters', 'created_at', 'updated_at')


class VotingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voting
        fields = ('id', 'user', 'vote_option', 'created_at', 'updated_at')


class GetVotingSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    vote_option = GetVoteOptionSerializer()

    class Meta:
        model = Voting
        fields = ('id', 'user', 'vote_option', 'created_at', 'updated_at')