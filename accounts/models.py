from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField()
    # https://github.com/django/django/blob/main/django/contrib/auth/models.py#L405より。
    # ここでAUTH_USER_MODELに返すよ！って設定している。

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class FriendShip(models.Model):
    follow = models.ForeignKey(User, related_name="follower", on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name="follow", on_delete=models.CASCADE)
