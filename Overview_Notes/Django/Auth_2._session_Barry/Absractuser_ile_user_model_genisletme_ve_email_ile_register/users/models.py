
# Bu dersin ilk projesinde, Django nun User modelinden bir tablo üretmistik. Ancak bu tablo bizim tüm ihtiyaclarimizi karsilamadigi icin, ikinci bir tablo üreterek bu tabloya ihtiyacimiz olan ilave bilgileri koymus ve iki tabloyu birbirine onetoone iliski ile baglamistik. Bu projede ayni hedefe ulasmak istiyoruz ancak farkli bir yöntem izleyecegiz. Ikinci bir tablo olusturmayacagiz, bunun yerine User modelden ürettigimiz tablo üzerinde degisiklikler yapacagiz.
# bunun icin abstractuser kullanacagiz. Burasi djangonun default modelinin türetildigi yer. ve bunun icinde User modelinde olan tüm field lar var.

## Önemli: sadece burada yaptigimiz degisiklikler yetmiyor. Django ya da bildirmemiz lazim. Senin default user ini kullanmayacagim bunun yerine users app i icindeki user modelini kullanacagim diyoruz. bunun icin settings.py da:
# AUTH_USER_MODEL = "users.User"

# abstractuser in üzerine ctrl ye basarak geliyoruz ve detaylarina bakiyoruz.

## eger bircok field imiz varsa ve hiz bizim icin önemli ise o zaman onetoone yapmak daha mantikli. Cünkü bu yöntemde iki tablo birlestiriliyor tek tablo oluyor.

## Burada neden Abstractuser dan türetiyoruz?? Cünkü; User modeli Abstractuser dan türetilmistir ve User bize hazir tablo olarak gelir. Bizde buradaki modelimizi User in türetildigi seyden türetmemiz lazim. 

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)

    ## günümüzde artik username yerine email kullaniliyor. Ancak django yapisi tamamen username ve password üzerine kuruludur. Eger biz email ve password ile giris yaptirmak istersek iki secenegimiz var. Birincisi kisa yol: username verisinin davranisini degistirecegiz ve bunun email olarak davranmasini saglayacagiz. Daha sonrasinda esas email bölmesini form dan silecegiz böylece 2 tane email bölmesi olmayacak. 
    # Diger secenekte ise tamamen herseyi bastan yazacagiz.
    # simdi biz burada Abstractuser in orijinal kodlarina gidip oradan kopyalama yapip alacagiz.

    # username = models.CharField(
    #     _('username'),
    #     max_length=150,
    #     unique=True,
    #     help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
    #     validators=[username_validator],
    #     error_messages={
    #         'unique': _("A user with that username already exists."),
    #     },
    # )

    username = models.EmailField("Email Address", unique=True)
    ## ilk parametre verbose_name yani frontend de görünecek kisim
    # girilen email ile kayit olmus baska bir user var mi diye unique ile kontrol ediyoruz.

    REQUIRED_FIELDS = []
    ## bu kod da AbstractUser in orijinal kodlarinda bulunur. Ve biz superuser olustururken bize email de sorulur. iste biz burada icini bos birakarak sorulmamasini istiyoruz











# burada bir form degil bir user modeli tanimladik. Bu modeli admin de görmek icin admin e de kayit yapariz.

# Önemli: eskiden users modeli de groups modeli de admin panelde auth basligi altinda bulunuyordu. Biz default unu degistirdikten sonra group ayni yerde duruyor. users modeli ise users app in altinda olustu

## Tüm bu islemlerden sonra; normal user modelindeki tüm field lar geliyor. Bunlara ilave olarak birde bizim ekledigimiz 2 field geliyor.


## note: eger migrate islemleri yapmamiza ragmen sikinti cikiyorsa; bu durumda db sqlite silinir ondan sonra migrate islemleri yapilir. Buradaki sikinti sundan kaynaklanir.
## Biz AUTH_USER_MODEL = "users.User"  bu komutu calistirmadan önce migrate yaptiysak db ye eski sisteme göre kayit yapildi. 

## Biz burada User modelinin field lari üzerine eklemeler yaptik. Simdi forms kismina gidip bu modelden form üretecegiz. Yine olusan tüm field lari secmek zorunda degiliz.

## oop dersinde polimorphism islemistik. iste burada default model bizim ihtiyacimizi tam karsilamiyor. Bu nedenle üzerinde oynama yapiyoruz. 