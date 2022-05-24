

from django.urls import path
from .views import index, student_delete, student_details, student_list, student_add, student_update

urlpatterns = [
    path("", index, name="index"),
    path("students/", student_list, name="student_list"),
    path("add/", student_add, name="student_add"),
    path("update/<int:id>", student_update, name="student_update"),
    ## burada int yerine str de yazilabilirdi
    path("delete/<int:id>", student_delete, name="student_delete"),

    path("students/<int:id>", student_details, name="student_details")
]