from django import forms
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, TemplateView, View

from tweets.models import Tweet

from .forms import SignupForm
from .models import FriendShip, User


class SignupView(CreateView):
    form_class = SignupForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data["username"]
        # パスワード入力確認処理をしているため
        password = form.cleaned_data["password1"]
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return response


class UserProfileView(TemplateView, LoginRequiredMixin):

    template_name = "accounts/user_profile.html"

    # 継承元のget_context_dataをオーバーライド（要勉強）
    def get_context_data(self, **kwargs):
        # 親クラスのget_context_dataを呼び出して基本的なコンテキストデータを取得
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs["username"])
        context["user"] = user
        context["tweets"] = Tweet.objects.filter(creator__username=user.username)
        context["follow"] = FriendShip.objects.filter(follow=user.id).count()
        context["follower"] = FriendShip.objects.filter(follower=user.id).count()
        context["check"] = FriendShip.objects.filter(follow=self.request.user, follower=user.id).exists()
        print(context)
        return context


# CreateViewはTempleteViewを継承しているのでTempleteが必要。
class FollowView(LoginRequiredMixin, View):
    def get(self, request, username):
        user_to_follow = get_object_or_404(User, username=username)

        if user_to_follow == request.user:
            return HttpResponseRedirect(reverse_lazy("tweets:home"))

        if FriendShip.objects.filter(follow=request.user, follower=user_to_follow).exists():
            None
        else:
            FriendShip.objects.create(follow=request.user, follower=user_to_follow)

        return HttpResponseRedirect(reverse_lazy("tweets:home"))


class UnFollowView(LoginRequiredMixin, View):
    def get(self, request, username):
        user_to_follow = get_object_or_404(User, username=username)

        if user_to_follow == request.user:
            return HttpResponseRedirect(reverse_lazy("tweets:home"))

        if FriendShip.objects.filter(follow=request.user, follower=user_to_follow).exists():
            FriendShip.objects.filter(follow=request.user, follower=user_to_follow).delete()

        return HttpResponseRedirect(reverse_lazy("tweets:home"))


class FollowingListView(TemplateView, LoginRequiredMixin):

    template_name = "accounts/following_list.html"

    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs["username"])
        context = super().get_context_data(**kwargs)
        context["following_list"] = FriendShip.objects.filter(follow=user.id)
        return context


class FollowerListView(TemplateView, LoginRequiredMixin):

    template_name = "accounts/follower_list.html"

    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs["username"])
        context = super().get_context_data(**kwargs)
        context["follower_list"] = FriendShip.objects.filter(follower=user.id)
        return context
