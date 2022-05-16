

from django.urls import path
from .views import home, about

urlpatterns = [
    path("home/", home),
    path("about/", about)
]

# eger path kisimlarini "" bos yaparsak sayfa acilir acilmaz direkt orada yazan func calisir.