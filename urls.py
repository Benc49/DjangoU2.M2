"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
import app.views
from app.views import sign_up, login, home, log_out, players, update

urlpatterns = [

    path('admin/', admin.site.urls),
    path("", app.views.home, name="home"),
    path("login/", app.views.log_in, name = "login"),\
    path("logout/", app.views.log_out, name="logout"),
    path("sign_up/", app.views.sign_up, name = "sign_up"),
    path("user-page/", app.views.user_page, name = "user-page"),
    path("players/", app.views.players, name = "players"),
    path("update/<str:pk>/", app.views.update, name = "update"),
    path("delete/<str:pk>/", app.views.delete, name = "delete")
]
