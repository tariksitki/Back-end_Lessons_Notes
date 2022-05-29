from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User 
## burada django nun bize sagladigi default tabloyu import ettik

# Create your models here.

## UserProfile tablomuzu normal bir model olarak models.Model den olusturuyoruz. Bu tablo ile onetoone iliski  kuracagimiz diger tablo ise, django nun default User tablosudur. 

## portfolio da, bir portfolio sayfasi render edilecegi icin url kullandik

## Önemli: Burada yazdigimiz user aslinda bir ID. Bu ne demek?   Biz portfolio = models.URLField(blank=True)  yazdigimizda,  portfolio degiskenine django tarafindan bir url atamasi yapilir. yani bu degiskenin degeri artik bir url dir. ImageField kullandigimizda degiskene foto atanir. OnetoOneField kullandigimizda ise user degiskenimize bir id atamasi yapilir. OnetoOneField  de textfield gibi bir field dir.  
# 
# onetoone iliskilerde, ikinci tabloda unique bir id üretilmek zorundadir. bunu da birinci tablodan yani django nun bize sagladigi tablodan, user create ederken üretiriz ve oradan aliriz. Aldigimiz bu id yi ikinci tablomuzda foreign key olarak kullaniriz. 
class UserProfile(models.Model):
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)
    user = models.OneToOneField(User, on_delete=CASCADE)

    def __str__(self):
        return 