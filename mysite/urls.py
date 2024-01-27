"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

AUTH_USER_MODEL = "accounts.User"
# accountsフォルダの中にUserというモデルを作成したので、acccounts.Userと記述する。
# もし、MyUserという名前のモデルで作成していたら、accounts.MyUserとする。

# 最終課題ではならないが、usersというフォルダの中にUserというモデルを作成した場合は
# AUTH_USER_MODEL = "users.User" となる
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("tweets/", include("tweets.urls")),
    path("", include("welcome.urls")),
]
