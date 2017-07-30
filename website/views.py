from rest_framework import generics, permissions, exceptions
from website.serializers import (
    PostTypeSerializer, PostSerializer,
    CommentsSerializer, ElementWordSerializer,
    TaskSerializer, SubmissionSerializer, EventSerializer,
    AlbumSerializer, TaskStatisticSerializer, EventStatisticSerializer,
    UserStatisticSerializer,
)

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
)


class PostTypeList(generics.ListCreateAPIView):
    permission_classes = (IsPmbAdmin,)
    queryset = PostType.objects.all()
    serializer_class = PostTypeSerializer


class PostTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsPmbAdmin,)
    queryset = PostType.objects.all()
    serializer_class = PostTypeSerializer


class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_fields = ('post_type',)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    filter_fields = ('post', )


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwner, )
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer


class ElementWordList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = ElementWord.objects.all()
    serializer_class = ElementWordSerializer


class ElementWordDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwner, )
    queryset = ElementWord.objects.all()
    serializer_class = ElementWordSerializer


class TaskList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

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

    def get_queryset(self):
        queryset = Submission.objects.filter(user=self.request.user)
        return  queryset


class SubmissionDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (IsOwner,)
    serializer_class = SubmissionSerializer

    def get_queryset(self):
        queryset = Submission.objects.filter(user=self.request.user)
        return queryset


class EventList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer

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

    def perform_create(self, serializer):
        if is_pmb_admin(self.request.user):
            serializer.save()
        else:
            raise exceptions.PermissionDenied


class EventStatisticDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = EventStatistic.objects.all()
    serializer_class = EventStatisticSerializer

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


class TaskStatisticList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = TaskStatistic.objects.all()
    serializer_class = TaskStatisticSerializer

    def perform_create(self, serializer):
        if is_pmb_admin(self.request.user):
            serializer.save()
        else:
            raise exceptions.PermissionDenied


class TaskStatisticDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = TaskStatistic.objects.all()
    serializer_class = TaskStatisticSerializer

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


class UserStatisticList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserStatisticSerializer

    def get_queryset(self):
        queryset = UserStatistic.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        if is_pmb_admin(self.request.user):
            serializer.save()
        else:
            raise exceptions.PermissionDenied


class UserStatisticDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = UserStatistic.objects.all()
    serializer_class = UserStatisticSerializer

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
