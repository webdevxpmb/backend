from rest_framework import generics, permissions, exceptions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from website.serializers import (
    PostTypeSerializer, PostSerializer,
    CommentsSerializer, ElementWordSerializer,
    TaskSerializer, SubmissionSerializer, EventSerializer,
    AlbumSerializer, TaskStatisticSerializer, EventStatisticSerializer,
    UserStatisticSerializer, GetPostSerializer, GetCommentsSerializer,
    GetElementWordSerializer, GetSubmissionSerializer, GetEventStatisticSerializer,
)

from website.utils import StandardResultsSetPagination

from website.models import (
    PostType, Post, Comment,
    ElementWord, Task, Submission,
    Event,
    Album, TaskStatistic,
    UserStatistic, EventStatistic,
)
from account.permissions import (
    IsPmbAdmin,
    IsOwner,
    IsMabaOrAdmin,
    is_pmb_admin,
    IsElemenOrAdmin,
)

import datetime

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


class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Post.objects.all()
    filter_fields = ('post_type', 'author__profile__angkatan', )
    parser_classes = (JSONParser, )
    serializer_class = PostSerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = GetPostSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = GetPostSerializer(queryset, many=True)
        return Response(serializer.data)

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

    def update(self, request, *args, **kwargs):
        self.permission_classes = (IsOwner, )
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        request.data['author'] = request.user.id
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(GetPostSerializer(instance).data)

    def delete(self, request, *args, **kwargs):
        self.permission_classes = (IsOwner, )
        return self.destroy(request, *args, **kwargs)


class CommentList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    filter_fields = ('post', )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = GetCommentsSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = GetCommentsSerializer(queryset, many=True)
        return Response(serializer.data)

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

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        post = instance.post
        request.data['post'] = post.id
        request.data['author'] = request.user.id
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(GetCommentsSerializer(instance).data)


class ElementWordList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = ElementWord.objects.all()
    serializer_class = ElementWordSerializer
    parser_classes = (JSONParser, )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = GetElementWordSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = GetElementWordSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        self.permission_classes = (IsElemenOrAdmin, )
        data = request.data
        data['author'] = request.user.id
        data['approved'] = False
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
        request.data['author'] = request.user.id
        if not is_pmb_admin(request.user):
            request.data['approved'] = False
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(GetCommentsSerializer(instance).data)


class TaskList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Task.objects.all()
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


class SubmissionList(generics.ListCreateAPIView):
    permission_classes = (IsMabaOrAdmin,)
    serializer_class = SubmissionSerializer
    parser_classes = (JSONParser,)
    filter_fields = ('task', )

    def get_queryset(self):
        queryset = Submission.objects.filter(user=self.request.user)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = GetSubmissionSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = GetSubmissionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        data['user'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        task = Task.objects.get(id=data['task'])
        if task.end_time < datetime.datetime.now():
            return Response({"message": "The submission deadline has been overdue"}, status=400)
        self.perform_create(serializer)
        instance = Submission.objects.get(id=serializer.data['id'])
        response_serializer = GetSubmissionSerializer(instance)
        headers = self.get_success_headers(response_serializer.data)
        return Response(response_serializer.data, status=201, headers=headers)


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
        request.data['task'] = instance.task.id
        if instance.task.end_time < datetime.datetime.now():
            return Response({"message": "The submission deadline has been overdue"}, status=400)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(GetSubmissionSerializer(instance).data)


class EventList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Event.objects.all()
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
    pagination_class = StandardResultsSetPagination

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
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = GetEventStatisticSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

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
            request.data['event'] = instance.event.id
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
    queryset = UserStatistic.objects.all()


class UserStatisticDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = UserStatistic.objects.all()
    serializer_class = UserStatisticSerializer

