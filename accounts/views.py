from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, View

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
        password = form.cleaned_data["password1"]
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return response


class UserProfileView(ListView, LoginRequiredMixin):
    template_name = "accounts/user_profile.html"
    model = Tweet

    def get_queryset(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs["username"])
        return Tweet.objects.filter(creator__username=user.username).order_by("-created")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs["username"])
        context["user"] = user
        context["follow"] = FriendShip.objects.filter(follow=user.id).count()
        context["follower"] = FriendShip.objects.filter(follower=user.id).count()
        context["check"] = FriendShip.objects.filter(follow=self.request.user, follower=user.id).exists()
        return context

    # def get_queryset(self, **kwargs):
    #     records = super().get_queryset(**kwargs)  # Article.objects.all() と同じ結果
    #     records = records.filter(creator__username=self.kwargs["username"])
    #     records = records.order_by("-created")
    #     return records


class FollowView(LoginRequiredMixin, View):
    def get(self, request, username):
        user_to_follow = get_object_or_404(User, username=username)

        if user_to_follow == request.user:
            response = HttpResponse(status=400)
            return response

        if FriendShip.objects.filter(follow=request.user, follower=user_to_follow).exists():
            None
        else:
            FriendShip.objects.create(follow=request.user, follower=user_to_follow)

        return HttpResponseRedirect(reverse_lazy("accounts:user_profile", kwargs={"username": username}))


class UnFollowView(LoginRequiredMixin, View):
    def get(self, request, username):
        user_to_follow = get_object_or_404(User, username=username)

        if user_to_follow == request.user:
            response = HttpResponse(status=400)
            return response

        if FriendShip.objects.filter(follow=request.user, follower=user_to_follow).exists():
            FriendShip.objects.filter(follow=request.user, follower=user_to_follow).delete()
        else:
            None

        return HttpResponseRedirect(reverse_lazy("accounts:user_profile", kwargs={"username": username}))


class FollowingListView(ListView, LoginRequiredMixin):

    template_name = "accounts/following_list.html"
    context_object_name = "following_list"

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs["username"])
        return FriendShip.objects.filter(follow=user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = get_object_or_404(User, username=self.kwargs["username"])
        return context


class FollowerListView(ListView, LoginRequiredMixin):

    template_name = "accounts/follower_list.html"
    context_object_name = "follower_list"

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs["username"])
        return FriendShip.objects.filter(follower=user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = get_object_or_404(User, username=self.kwargs["username"])
        return context
