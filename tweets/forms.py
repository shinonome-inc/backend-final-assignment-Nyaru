from django import forms
from django.forms import ModelForm

from .models import Tweet


class TweetCreateForm(ModelForm):

    class Meta:
        model = Tweet
        fields = (
            "image",
            "body",
        )
        widgets = {"content": forms.Textarea(attrs={"rows": 4, "cols": 35, "placeholder": "いまどうしてる？"})}
