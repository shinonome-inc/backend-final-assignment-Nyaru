from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from tweets.models import Tweet

from .forms import SignupForm


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
        queryset = super().get_queryset(**kwargs)  # Article.objects.all() と同じ結果
        queryset = queryset.filter(creator__username=self.kwargs["username"])
        queryset = queryset.order_by("-created")
        return queryset

    # # 継承元のget_context_dataをオーバーライド（要勉強）
    # def get_context_data(self, **kwargs):
    #     # 親クラスのget_context_dataを呼び出して基本的なコンテキストデータを取得
    #     context = super().get_context_data(**kwargs)
    #     context["tweets"] = Tweet.objects.filter(creator__username=self.kwargs["username"])
    #     return context


# class FollowView(LoginRequiredMixin, TemplateView):
