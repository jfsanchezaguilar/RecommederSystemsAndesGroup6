from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from RecommendApi.models import RecommendTask, BookUser, Book, BookRaiting
from RecommendApi.serializers import UserSerializer, GroupSerializer, RecommendTaskSerializer, BookUserSerializer, \
    BookSerializer, BookRaitingSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RecommendTaskViewSet(viewsets.ModelViewSet):
    queryset = RecommendTask.objects.all()
    serializer_class = RecommendTaskSerializer


class BookUserViewSet(viewsets.ModelViewSet):
    queryset = BookUser.objects.all()
    serializer_class = BookUserSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRaitingViewSet(viewsets.ModelViewSet):
    queryset = BookRaiting.objects.all()
    serializer_class = BookRaitingSerializer
