from django.conf import settings
from django.db import models


class Tweet(models.Model):
    # blank=True null=True で画像がなくても投稿が出来るようになる。
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    body = models.TextField(verbose_name="content", max_length=140)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="tweets", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
