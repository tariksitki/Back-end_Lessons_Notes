
from django.urls import path
from .views import student_page, home



urlpatterns = [
    path('', student_page, name="student"),
    path('home/', home, name="home"),
]