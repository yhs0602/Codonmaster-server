from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.utils import timezone


class MyUser(AbstractUser):
    first_name = None
    last_name = None
    google_id = models.TextField(max_length=512)
    money = models.IntegerField()
    jewel = models.IntegerField()
    jewel_2 = models.IntegerField()
    experience = models.PositiveIntegerField()
    level = models.PositiveIntegerField()


class Announcement(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    title = models.TextField()
    content = models.TextField()
    title_ko = models.TextField()
    content_ko = models.TextField()
    type = models.IntegerField()


class Ranking(models.Model):
    time = models.DateTimeField(auto_created=True, default=timezone.now)
    score = models.IntegerField()
    user = models.ForeignKey(MyUser, null=True, on_delete=models.SET_NULL)


class ServerStatus(models.Model):
    data = models.CharField(max_length=16)
    description = models.CharField(max_length=16)
