from django.contrib.auth.models import User, Group
from rest_framework import serializers

from RecommendApi.models import RecommendTask


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
