
from django.urls import path
from .views import number_of_student, index

urlpatterns = [
     path("", index),
     path("num/", number_of_student, name = "number_of_student")
]
