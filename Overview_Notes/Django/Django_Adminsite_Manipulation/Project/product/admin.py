from django.contrib import admin
from .models import Product

# Register your models here.


admin.site.register(Product)


# Bu kod browser in tab in da bulunan title i degistirir
admin.site.site_title = "Tarik's Webpage"



## Admin page de baslik olan Django administration  ismini degistirmek
admin.site.site_header = "Tarik's Admin Page"



#Site administration isimli basligi degistirmek:
admin.site.index_title = "Tarik's Administration"


