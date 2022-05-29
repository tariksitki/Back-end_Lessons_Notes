from django.urls import path
from .views import user_logout, register, user_login

urlpatterns = [
    path("logout/", user_logout, name="logout"),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    
]


# settingse bu komutu koyup
# LOGOUT_REDIRECT_URL = "home"
# daha sonra home da logoutu a tagi içine alıncada oluyor hocam
#  <a href="accounts/login">Login</a>