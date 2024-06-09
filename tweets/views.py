# from django.shortcuts import render
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import TweetCreateForm
from .models import Tweet


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "tweets/home.html"
    
    def get_context_data(self, **kwargs):
        # 親クラスのget_context_dataを呼び出して基本的なコンテキストデータを取得
        context = super().get_context_data(**kwargs)
        context['tweets'] = self.get_data()
        return context

    def get_data(self):
        # Tweetモデルからすべてのツイートを取得
        tweets = Tweet.objects.all()
        return tweets
    

class TweetCreateView(CreateView):
    model = Tweet
    form_class = TweetCreateForm
    template_name = "tweets/create.html"
    success_url = reverse_lazy("tweets:home")

    def form_valid(self, form):
        form.instance.creator = self.request.user  # ログイン中のユーザーを設定
        return super().form_valid(form)
