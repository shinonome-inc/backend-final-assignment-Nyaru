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


# 引数にblank=Falseを入れる必要はない。
# なぜならデフォルトでblank=Falseとなるため。

# from django.contrib.auth.models import AbstractUser
# from django.db import models


# class User(AbstractUser):


# class FriendShip(models.Model):
