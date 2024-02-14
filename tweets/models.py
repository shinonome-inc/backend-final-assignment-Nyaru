from django.db import models


class Tweet(models.Model):
    image = models.ImageField()
    body = models.TextField(max_length=140)
    creator = models.CharField(max_length=255)
    created = models.DateTimeField()
    likes = models.IntegerField()
