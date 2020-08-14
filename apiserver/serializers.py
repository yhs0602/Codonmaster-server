from django.contrib.auth.models import Group
from rest_framework import serializers

from apiserver.models import MyUser, Ranking, Announcement, ServerStatus


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ['url', 'google_id', 'username', 'email', 'money', 'jewel', 'jewel_2', 'experience', 'level']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class RankingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ranking
        fields = ['time', 'score', 'user']


class AnnouncementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Announcement
        fields = ['time', 'image', 'title', 'content', 'title_ko', 'content_ko', 'type']


class ServerStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServerStatus
        fields = ['data', 'description']
