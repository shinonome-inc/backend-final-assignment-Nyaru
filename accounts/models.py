from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField()

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"


# class FriendShip(models.Model):
