from rest_framework import generics, permissions, exceptions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser, FileUploadParser
from rest_framework.response import Response
from django.db import IntegrityError
from website.serializers import (
    PostTypeSerializer, PostSerializer,
    CommentsSerializer, ElementWordSerializer,
    TaskSerializer, SubmissionSerializer, EventSerializer,
    AlbumSerializer, TaskStatisticSerializer, EventStatisticSerializer,
    UserStatisticSerializer, GetPostSerializer, GetCommentsSerializer,
    GetElementWordSerializer, GetSubmissionSerializer, GetEventStatisticSerializer,
    VoteSerializer, GetVoteSerializer, VoteOptionSerializer, GetVoteOptionSerializer,
    VotingSerializer, GetVotingSerializer, FileSerializer, QnASerializer, GetQnASerializer,
    TaskScoreSerializer,
)

from account import permissions as account_permissions


from website.models import (
    PostType, Post, Comment,
    ElementWord, Task, Submission,
    Event,
    Album, TaskStatistic,
    UserStatistic, EventStatistic,
    Vote, VoteOption, Voting, QnA,
    TaskScore,
)
from account.permissions import (
    IsPmbAdmin,
    IsOwner,
    IsMabaOrAdmin,
    is_pmb_admin,
    IsElemenOrAdmin,
)

from rest_framework.test import APIRequestFactory
import datetime
from backend.settings import HOST_URL

class FileView(APIView):
    permission_classes = (permissions.AllowAny,)
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        try:
            file_serializer = FileSerializer(data=request.data)
            if file_serializer.is_valid():
                result = file_serializer.save()
                serializer_data = file_serializer.data
                serializer_data['file'] = HOST_URL + serializer_data['file']
                return Response(serializer_data, status=status.HTTP_201_CREATED)
            else:
                return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)

class PostTypeList(generics.ListCreateAPIView):
    permission_classes = (IsPmbAdmin,)
    queryset = PostType.objects.all()
    serializer_class = PostTypeSerializer
    parser_classes = (JSONParser,)


class PostTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsPmbAdmin,)
    queryset = PostType.objects.all()
    serializer_class = PostTypeSerializer
    parser_classes = (JSONParser,)


class AnnouncementList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Post.objects.filter(post_type__post_type='pengumuman').order_by('-created_at')
    filter_fields = ('post_type', 'author__profile__angkatan', )
    parser_classes = (JSONParser, )
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = GetPostSerializer(queryset, many=True)
        return Response(serializer.data, status=200)


class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Post.objects.all().order_by('-created_at')
    filter_fields = ('post_type', 'author__profile__angkatan', )
    parser_classes = (JSONParser, )
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = GetPostSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_update(self, serializer):
        if is_pmb_admin(self.request.user):
            serializer.save(author=self.request.user)
        else:
            raise exceptions.PermissionDenied

    def perform_create(self, serializer):
        if is_pmb_admin(self.request.user):
            serializer.save()
        else:
            raise exceptions.PermissionDenied

    def post(self, request, *args, **kwargs):
        data = request.data
        data['author'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        instance = Post.objects.get(id=serializer.data['id'])
        response_serializer = GetPostSerializer(instance)
        headers = self.get_success_headers(response_serializer.data)
        return Response(response_serializer.data, status=201, headers=headers)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = (JSONParser,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = GetPostSerializer(instance)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def update(self, request, *args, **kwargs):
        self.permission_classes = (IsOwner, )
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(GetPostSerializer(instance).data)

    def delete(self, request, *args, **kwargs):
        self.permission_classes = (IsOwner, )
        return self.destroy(request, *args, **kwargs)


class CommentList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentsSerializer
    filter_fields = ('post', )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = GetCommentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def post(self, request, *args, **kwargs):
        data = request.data
        data['author'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        instance = Comment.objects.get(id=serializer.data['id'])
        response_serializer = GetCommentsSerializer(instance)
        headers = self.get_success_headers(response_serializer.data)
        return Response(response_serializer.data, status=201, headers=headers)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwner, )
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = GetCommentsSerializer(instance)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        post = instance.post
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(GetCommentsSerializer(instance).data)

class ElementWordList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = ElementWord.objects.all().order_by('-created_at')
    serializer_class = ElementWordSerializer
    parser_classes = (JSONParser, )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = GetElementWordSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, approved=False)

    def post(self, request, *args, **kwargs):
        self.permission_classes = (IsElemenOrAdmin, )
        data = request.data
        data['author'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        instance = ElementWord.objects.get(id=serializer.data['id'])
        response_serializer = GetElementWordSerializer(instance)
        headers = self.get_success_headers(response_serializer.data)
        return Response(response_serializer.data, status=201, headers=headers)


class ElementWordDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwner, )
    queryset = ElementWord.objects.all()
    serializer_class = ElementWordSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = GetElementWordSerializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(GetCommentsSerializer(instance).data)


class TaskList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    parser_classes = (JSONParser,)

    def perform_create(self, serializer):
        if is_pmb_admin(self.request.user):
            serializer.save()
        else:
            raise exceptions.PermissionDenied


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def put(self, request, *args, **kwargs):
        if is_pmb_admin(request.user):
            return self.update(request, *args, **kwargs)
        else:
            raise exceptions.PermissionDenied

    def patch(self, request, *args, **kwargs):
        if is_pmb_admin(request.user):
            return self.update(request, *args, **kwargs)
        else:
            raise exceptions.PermissionDenied

    def delete(self, request, *args, **kwargs):
        if is_pmb_admin(request.user):
            return self.destroy(request, *args, **kwargs)
        else:
            raise exceptions.PermissionDenied

class TaskLatestSubmission(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = SubmissionSerializer

    def get_queryset(self):
        queryset = Submission.objects.filter(user=self.request.user, task=self.kwargs['pk'])
        return queryset

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.latest('updated_at')
        return obj

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = GetSubmissionSerializer(instance)
        return Response(serializer.data)

class TaskScoreList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TaskScoreSerializer

    def get_queryset(self):
        queryset = TaskScore.objects.filter(user=self.request.user)
        return queryset


class TaskScoreDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = TaskScore.objects.all()
    serializer_class = TaskScoreSerializer

class QnAList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = QnA.objects.all().order_by('created_at')
    serializer_class = QnASerializer
    filter_fields = ('task', )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = GetQnASerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def post(self, request, *args, **kwargs):
        data = request.data
        data['author'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        instance = QnA.objects.get(id=serializer.data['id'])
        response_serializer = GetQnASerializer(instance)
        headers = self.get_success_headers(response_serializer.data)
        return Response(response_serializer.data, status=201, headers=headers)

class QnADetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwner, )
    queryset = QnA.objects.all()
    serializer_class = QnASerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = GetQnASerializer(instance)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        task = instance.task
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(GetQnASerializer(instance).data)

class SubmissionList(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SubmissionSerializer
    parser_classes = (JSONParser,)
    filter_fields = ('task', )

    def get_queryset(self):
        task_id_table = set()
        queryset = Submission.objects.filter(user=self.request.user).order_by('-updated_at', '-created_at')
        result = []
        for q in queryset:
            if q.task_id not in task_id_table:
                result.append(q)
                task_id_table.add(q.task_id)
        return result

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = GetSubmissionSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        try:
            data = request.data.copy()
            data['user'] = self.request.user.id
            serializer = SubmissionSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            task = Task.objects.get(id=data['task'])
            if task.end_time < datetime.datetime.now():
                return Response({"message": "The submission deadline has been overdue"}, status=400)
            serializer.save()
            instance = Submission.objects.get(id=serializer.data['id'])
            response_serializer = GetSubmissionSerializer(instance)
            return Response(response_serializer.data, status=201)
        except Exception as e:
            return Response(status=400)


class SubmissionDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (IsOwner,)
    serializer_class = SubmissionSerializer

    def get_queryset(self):
        queryset = Submission.objects.filter(user=self.request.user)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = GetSubmissionSerializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if instance.task.end_time < datetime.datetime.now():
            return Response({"message": "The submission deadline has been overdue"}, status=400)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(GetSubmissionSerializer(instance).data)

class EventList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Event.objects.all().order_by('-created_at')
    serializer_class = EventSerializer
    parser_classes = (JSONParser,)

    def perform_create(self, serializer):
        if is_pmb_admin(self.request.user):
            serializer.save()
        else:
            raise exceptions.PermissionDenied


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def put(self, request, *args, **kwargs):
        if is_pmb_admin(request.user):
            return self.update(request, *args, **kwargs)
        else:
            raise exceptions.PermissionDenied

    def patch(self, request, *args, **kwargs):
        if is_pmb_admin(request.user):
            return self.update(request, *args, **kwargs)
        else:
            raise exceptions.PermissionDenied

    def delete(self, request, *args, **kwargs):
        if is_pmb_admin(request.user):
            return self.destroy(request, *args, **kwargs)
        else:
            raise exceptions.PermissionDenied


class AlbumList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    parser_classes = (JSONParser,)

    def perform_create(self, serializer):
        if is_pmb_admin(self.request.user):
            serializer.save()
        else:
            raise exceptions.PermissionDenied


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def put(self, request, *args, **kwargs):
        if is_pmb_admin(request.user):
            return self.update(request, *args, **kwargs)
        else:
            raise exceptions.PermissionDenied

    def patch(self, request, *args, **kwargs):
        if is_pmb_admin(request.user):
            return self.update(request, *args, **kwargs)
        else:
            raise exceptions.PermissionDenied

    def delete(self, request, *args, **kwargs):
        if is_pmb_admin(request.user):
            return self.destroy(request, *args, **kwargs)
        else:
            raise exceptions.PermissionDenied


class EventStatisticList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = EventStatistic.objects.all()
    serializer_class = EventStatisticSerializer
    parser_classes = (JSONParser,)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = GetEventStatisticSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if is_pmb_admin(request.user):
            data = request.data
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            instance = EventStatistic.objects.get(id=serializer.data['id'])
            response_serializer = GetEventStatisticSerializer(instance)
            headers = self.get_success_headers(response_serializer.data)
            return Response(response_serializer.data, status=201, headers=headers)
        else:
            raise exceptions.PermissionDenied


class EventStatisticDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = EventStatistic.objects.all()
    serializer_class = EventStatisticSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = GetEventStatisticSerializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        if is_pmb_admin(request.user):
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            return Response(GetEventStatisticSerializer(instance).data)
        else:
            raise exceptions.PermissionDenied

    def delete(self, request, *args, **kwargs):
        if is_pmb_admin(request.user):
            return self.destroy(request, *args, **kwargs)
        else:
            raise exceptions.PermissionDenied


class TaskStatisticList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = TaskStatistic.objects.all()
    serializer_class = TaskStatisticSerializer


class TaskStatisticDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = TaskStatistic.objects.all()
    serializer_class = TaskStatisticSerializer


class UserStatisticList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserStatisticSerializer

    def get_queryset(self):
        queryset = UserStatistic.objects.filter(user=self.request.user)
        return queryset


class UserStatisticDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = UserStatistic.objects.all()
    serializer_class = UserStatisticSerializer


class VoteList(generics.ListAPIView):
    permission_classes = (account_permissions.IsElemenOrAdmin, )
    serializer_class = GetVoteSerializer
    queryset = Vote.objects.all()


class VotingListCreate(generics.ListCreateAPIView):
    permission_classes = (account_permissions.IsElemenOrAdmin, )
    serializer_class = VotingSerializer

    def get_queryset(self):
        queryset = Voting.objects.filter(user=self.request.user)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = GetVotingSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            vote_option = VoteOption.objects.get(id=data['vote_option'])
            vote = vote_option.vote
            if vote.end_time < datetime.datetime.now():
                return Response({"message": "The voting period is over"}, status=400)

            if vote.start_time > datetime.datetime.now():
                return Response({"message": "The voting period has not started yet"}, status=400)

            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            instance = Voting.objects.get(id=serializer.data['id'])
            response_serializer = GetVotingSerializer(instance)
            headers = self.get_success_headers(response_serializer.data)
            return Response(response_serializer.data, status=201, headers=headers)
        except Exception:
            return Response(status=400)


class VotingDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (account_permissions.IsElemenOrAdmin, )
    serializer_class = VotingSerializer

    def get_queryset(self):
        queryset = Voting.objects.filter(user=self.request.user)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = GetVotingSerializer(instance)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        vote_option = VoteOption.objects.get(id=request.data['vote_option'])
        vote = vote_option.vote
        if vote.end_time < datetime.datetime.now():
            return Response({"message": "The voting period is over"}, status=400)

        if vote.start_time > datetime.datetime.now():
            return Response({"message": "The voting period has not started yet"}, status=400)

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(GetVotingSerializer(instance).data)
