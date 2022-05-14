
from django.urls import path
from .views import home, about, login


urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("login/", login, name="login")
]