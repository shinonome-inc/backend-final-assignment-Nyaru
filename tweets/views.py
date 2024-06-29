# from django.shortcuts import render
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, TemplateView

from .forms import TweetCreateForm
from .models import Tweet


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "tweets/home.html"
    
    def get_context_data(self, **kwargs):
        # 親クラスのget_context_dataを呼び出して基本的なコンテキストデータを取得
        context = super().get_context_data(**kwargs)
        context['tweets'] = Tweet.objects.all()
        return context
    

class TweetCreateView(CreateView):
    model = Tweet
    form_class = TweetCreateForm
    template_name = "tweets/create.html"
    success_url = reverse_lazy("tweets:home")

    def form_valid(self, form):
        form.instance.creator = self.request.user  # ログイン中のユーザーを設定
        return super().form_valid(form)


class TweetDetailView(TemplateView):
    model = Tweet
    template_name = "tweets/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tweet"] = Tweet.objects.get(pk=self.kwargs["pk"])
        return context
    

class TweetDeleteView(DeleteView):
    model = Tweet
    template_name = "tweets/delete.html"
    success_url = reverse_lazy("tweets:home")

    

    
    
        
