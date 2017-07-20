from rest_framework import generics, permissions
from website.serializers import (
    AttachmentSerializer, PostSerializer,
    CommentsSerializer, ElementWordSerializer,
    TaskSerializer, EventsSerializer, SubmissionSerializer
)
from website.models import (
    Attachment, Post, Comments, ElementWord,
    Task, Events, Submission
)

# Create your views here.

class CreatePost(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostListDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CreateComments(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class CommentList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class CreateElementWord(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = ElementWord.objects.all()
    serializer_class = ElementWordSerializer


class ElementWordList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = ElementWord.objects.all()
    serializer_class = ElementWordSerializer


class ElementWordListDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = ElementWord.objects.all()
    serializer_class = ElementWordSerializer


class CreateTask(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskListDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CreateSubmission(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer


class SubmissionList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer


class SubmissionListDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer


class CreateEvent(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


class EventsList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


class EventListDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


class CreateAttachments(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer


class AttachmentList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer


class AttachmentListDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
