from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField()

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class FriendShip(models.Model):
    follow = models.ForeignKey(User, related_name="follower", on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name="follow", on_delete=models.CASCADE)
