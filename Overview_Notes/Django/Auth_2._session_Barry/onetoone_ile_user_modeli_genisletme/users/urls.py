from django.urls import path
from .views import user_logout, register, user_login


## Önemli Note: url ler icindeki name lerin  kullanimi: 
## navbar a gidiyoruz. logout butonuna diyoruz ki;  url listsi icinde, name i logut olan url ibul ve onun adres karsiligi ne ise o adrese git.

## Cok önemli: urls yazarken name i unutursak "string is not mapping hatasi verir"

## Önemli: burada bulunan register, logout gibi url leri 8000 den sonra direkt olarak yazamayiz. cünkü ana projenin url inde tanimlama yaparken, basinda users olan url leri include ile buraya gönderiyoruz. o nedenle basina users koymamiz gerekir.

urlpatterns = [
    path("logout/", user_logout, name="logout"),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
        ## dikkat: templates lerde, name ile url leri cagirirken isimleri dogru yazmaya dikkat.
    
]


# settingse bu komutu koyup
# LOGOUT_REDIRECT_URL = "home"
# daha sonra home da logoutu a tagi içine alıncada oluyor hocam
#  <a href="accounts/login">Login</a>