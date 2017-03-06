from django.contrib.auth.models import User, Group
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from RecommendApi.file_updater import update_book_user_file, update_book_file, update_book_raiting_file
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


@api_view(['GET'])
def recommend_task_list_detail(request, pk):
    try:
        task = RecommendTask.objects.get(pk=pk)
    except RecommendTask.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RecommendTaskSerializer(task)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def recommend_task_list(request):
    if request.method == 'GET':
        recommend_tasks = RecommendTask.objects.all()
        serializer = RecommendTaskSerializer(recommend_tasks, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = RecommendTaskSerializer(data=request.data)
        if serializer.is_valid():
            task = RecommendTask(**serializer.validated_data)
            if not RecommendTask.objects.filter(training=task.training) \
                    or not RecommendTask.objects.filter(similarity=task.similarity)\
                    or not RecommendTask.objects.filter(algorithm=task.algorithm):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.data, status=status.HTTP_302_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def book_user_list(request):
    if request.method == 'GET':
        book_users = BookUser.objects.all()
        serializer = BookUserSerializer(book_users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            book_user = BookUser.objects.latest("id")
            update_book_user_file(book_user.user_id, book_user.location, book_user.age)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            book = Book.objects.latest("id")
            update_book_file(book.isbn, book.book_title, book.book_author, book.year_publish
                             , book.publisher, book.image_small, book.image_medium, book.image_large)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def book_raiting_list(request):
    if request.method == 'GET':
        book_raitings = BookRaiting.objects.all()
        serializer = BookRaitingSerializer(book_raitings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookRaitingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            book_raiting = BookRaiting.objects.latest("id")
            update_book_raiting_file(book_raiting.user_id, book_raiting.isbn, book_raiting.raiting)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
