from django.urls import path
from .views import home,student_list, student_add, student_detail, student_update,student_delete, HomeView, StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView
from django.views.generic.base import TemplateView

urlpatterns = [
        ## home.html islemleri:
    # path('', home, name="home"),  burasi klasik func based

        # class based 1 yöntem. views.py ve burada iki islem
    # path("", HomeView.as_view(), name="home"),

        # class based ikinci yöntem. view da birsey yapmiyoruz. Bunun icin templateView i burada import ettik.
        # burada sadece gjango ya ait olan generic templateView kullanilir. 
    path("", TemplateView.as_view(template_name="fscohort/home.html"), name="home"),




        ## List:
    path('student_list/', student_list, name="list"),
    
        ## class based:
    path("student_list/", StudentListView.as_view(), name="list"),








    # path('student_add/', student_add, name="add"),
    path('student_add/', StudentCreateView.as_view(), name="add"),







        ## detail:
    #path('detail/<int:id>/', student_detail, name="detail"),  ## func based

        ##  class based:
    path("detail/<int:id>/", StudentDetailView.as_view(), name="detail" ),












    path('update/<int:id>/', student_update, name="update"),
        ## class (burada pk kullanacagiz)
     path('update/<int:pk>/', StudentUpdateView.as_view(), name="update"),
    







    # path('delete/<int:id>/', student_delete, name="delete"),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name="delete"),
]