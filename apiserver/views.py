from django.contrib.auth.models import Group
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from apiserver.models import MyUser, Ranking, Announcement, ServerStatus
from apiserver.serializers import UserSerializer, GroupSerializer, RankingSerializer, AnnouncementSerializer, \
    ServerStatusSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RankingViewSet(viewsets.ModelViewSet):
    queryset = Ranking.objects.all()
    serializer_class = RankingSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class ServerStatusViewSet(viewsets.ModelViewSet):
    queryset = ServerStatus.objects.all()
    serializer_class = ServerStatusSerializer


def get_help(request):
    lang = request.GET.get('lang', 'en')

    return

