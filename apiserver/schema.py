from datetime import datetime

import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType

from graphene_generator.holder import QueriesHolder, MutationsHolder

from apiserver.models import Announcement, ServerStatus, Ranking, MyUser


class AnnouncementType(DjangoObjectType):
    class Meta:
        model = Announcement


class ServerstatusType(DjangoObjectType):
    class Meta:
        model = ServerStatus


class RankingType(DjangoObjectType):
    class Meta:
        model = Ranking


class UserType(DjangoObjectType):
    class Meta:
        model = MyUser


class Query(ObjectType):
    announcements = graphene.List(AnnouncementType)
    announcement = graphene.Field(AnnouncementType, id=graphene.Int())
    serverstati = graphene.List(ServerstatusType)
    rankings = graphene.List(RankingType)
    user = graphene.Field(UserType, username=graphene.String(), google_id=graphene.String())
    userOfID = graphene.Field(UserType, id=graphene.Int())

    def resolve_announcements(self, info, **kwargs):
        return Announcement.objects.all()

    def resolve_announcement(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Announcement.objects.get(pk=id)
        return None

    def resolve_serverstati(self, info, **kwargs):
        return ServerStatus.objects.all()

    def resolve_rankings(self, info, **kwargs):
        rankings = Ranking.objects.all()
        for ranking in rankings:
            ranking.user.password = "None"
            ranking.user.google_id = "None"
            ranking.user.email = "None"
            ranking.user.jewel = 0
            ranking.user.jewel_2 = 0
            ranking.user.experience = 0
            ranking.user.money = 0
        return rankings


    def resolve_user(self, info, **kwargs):
        username = kwargs.get('username')
        google_id = kwargs.get('google_id')
        if username is not None and google_id is not None:
            user = MyUser.objects.get(username=username, google_id=google_id)
            user.password = "unknown"
            user.google_id = "unknown"
            user.email = "unknown"
            return user

        return None

    def resolve_userOfID(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            theUser = MyUser.objects.get(pk=id)
            theUser.password = "None"
            theUser.google_id = "None"
            theUser.email = "None"
            # theUser.ranking_set = None
            theUser.jewel = 0
            theUser.money = 0
            theUser.experience = 0
            theUser.jewel_2 = 0
            return theUser
        return None


class UserInput(graphene.InputObjectType):
    # id = graphene.ID()
    name = graphene.String(required=True)
    password = graphene.String()
    google_id = graphene.String()


class LiveResultInput(graphene.InputObjectType):
    # id = graphene.ID()
    userId = graphene.Int()
    time = graphene.Int()
    score = graphene.Int(required=True)


class CreateNewUser(graphene.Mutation):
    class Arguments:
        input = UserInput(required=True)

    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, input=None):
        myuser_instance = MyUser(username=input.name, password=input.password, google_id=input.google_id, money=0,
                                 jewel=0, jewel_2=0, experience=0, level=0)
        myuser_instance.save()
        return CreateNewUser()


class NewLiveResult(graphene.Mutation):
    class Arguments:
        input = LiveResultInput(required=True)

    newliveresult = graphene.Field(RankingType)

    @staticmethod
    def mutate(root, info, input=None):
        ranking_instance = Ranking(score=input.score, user_id=input.userId)
        ranking_instance.save()
        return NewLiveResult()


class Mutation(graphene.ObjectType):
    createNewUser = CreateNewUser.Field()
    newLiveResult = NewLiveResult.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
