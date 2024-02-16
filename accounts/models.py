from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField()

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


# from django.contrib.auth.models import AbstractUser
# from django.db import models


# class User(AbstractUser):


# class FriendShip(models.Model):
