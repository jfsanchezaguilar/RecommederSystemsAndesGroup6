from django.contrib.auth.models import User, Group
from rest_framework import serializers

from RecommendApi.models import RecommendTask, BookUser, Book, BookRaiting


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class RecommendTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendTask
        fields = ('id', 'training', 'similarity', 'algorithm', 'added_date', 'start_date', 'finish_date', 'status')


class BookUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookUser
        fields = ('id', 'user_id', 'location', 'age')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'isbn', 'book_title', 'book_author', 'year_publish', 'publisher', 'image_small', 'image_medium'
                  , 'image_large')


class BookRaitingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRaiting
        fields = ('id', 'user_id', 'isbn', 'raiting')
