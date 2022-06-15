from django.urls import path
from .views import home, hello_world, TodoList, todoCreate, todoListCreate, todoUpdate


urlpatterns = [
    path('', home),
    path("hello/", hello_world),
    path("todoList/", TodoList),
    path("todoCreate/", todoCreate),
    path("todoListCreate/", todoListCreate),
    path("todoUpdate/<int:pk>/", todoUpdate),
    
]


## url lerdeki name alani genellikle template ve form lar icin gereklidir. rest api de buna pek ihtiyac duymayiz.
