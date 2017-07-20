from rest_framework import generics, permissions
from website.serializers import (
    PostTypeSerializer, PostSerializer,
    CommentsSerializer, ElementWordSerializer,
    TaskTypeSerializer, TaskSerializer,
    SubmissionSerializer, EventsSerializer,
    AttachmentSerializer,
)

from website.models import (
    PostType, Post, Comments,
    ElementWord, TaskType, Task,
    Submission, Events, Attachment,
)


class PostTypeList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = PostType.objects.all()
    serializer_class = PostTypeSerializer


class PostTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = PostType.objects.all()
    serializer_class = PostTypeSerializer


class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class ElementWordList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = ElementWord.objects.all()
    serializer_class = ElementWordSerializer


class ElementWordDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = ElementWord.objects.all()
    serializer_class = ElementWordSerializer


class TaskTypeList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = TaskType.objects.all()
    serializer_class = TaskTypeSerializer


class TaskTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = TaskType.objects.all()
    serializer_class = TaskTypeSerializer


class TaskList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class SubmissionList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer


class SubmissionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer


class EventsList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


class AttachmentList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer


class AttachmentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
