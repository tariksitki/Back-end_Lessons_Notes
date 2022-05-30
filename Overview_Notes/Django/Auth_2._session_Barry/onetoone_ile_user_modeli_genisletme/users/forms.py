from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django import forms

## form olusturmak icin elimizde 3 tane secenek var. 
# 1: klasik method her alani kendimiz olusturma
# 2: models den olusturma
# 3: hazir UserCreationForm kullanma (son iki method hazir oldugu icin bunlarda meta kullanmamiz gerekir)

## simdi 2 tane form olusturacagiz: 
# birincisi user icin yani bu form da user bilgilerini girecegiz
# ikincisi user profile,  yani user profile bilgilerini girecegiz
### daha sonra template e gidip bir form tagi acacagiz. burada ürettigimiz iki formu da o form icine atacagiz. Kullanici bu iki form daki bilgileri doldurup tikladiginda register olabilecek.


class UserForm(UserCreationForm):
    class Meta:
        model = User  
        # fields = "__all__"
        fields = ("username", "email")

# burada hem hazir UserCreationForm hem de bunu üretmek icin hazir User modeli kullandik
## Önemli: biz formlari tanimlarken, burada password kullanmiyoruz. Cünkü biz burada password kullandigimizda, bize model deki password u getirir. Ancak db e kayit yapilirken sifreli bir password kullanilir. o nedenle biz burada kullanmayiz.
## buna ragmen template render edilirken, bizim karsimiza password secenegi cikar.



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ("user",)


### önemli: fields tanimlarken 3 secenegimiz vardir.
# 1: all
# 2: specific isimler ile sadece istediklerimizi alma
# 3: exclude: yani istemediklerimizi cikarma

## exclude tanimlamada tuple kullanmak önemli

## Önemli: ikinci formumuzda user i cikardik. eger cikarmasaydik; bize user secmek icin bir select box cikaracakti ve buradan daha önce olusturulmus olan user lardan birini secmek zorunda kalacaktik. ama biz bunu istemiyoruz. Hem o anda bir user olusturmak hem de bu user a ait profile olusturmak istiyoruz.