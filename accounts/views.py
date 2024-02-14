from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import SignupForm


class SignupView(CreateView):
    form_class = SignupForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL) # reverse_lazyを使って参照している

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
