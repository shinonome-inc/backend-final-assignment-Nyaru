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
        widgets = {"content": forms.Textarea(attrs={"rows": 4, "cols": 35, "placeholder": "いまどうしているのですわ？"})}

        error_messages = {
            'body': {
                'max_length': "ツイートが" + str(Tweet.body.field.max_length) + "字を超えていますわ～！",
                'required': "ツイート内容がありませんわ～！",
            },
        }
