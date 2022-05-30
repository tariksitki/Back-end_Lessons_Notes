from django.db import models
from django.contrib.auth.models import User 
## burada django nun bize sagladigi default tabloyu import ettik

## UserProfile tablomuzu normal bir model olarak models.Model den olusturuyoruz. Bu tablo ile onetoone iliski  kuracagimiz diger tablo ise, django nun default User tablosudur. 

## portfolio da, bir portfolio sayfasi render edilecegi icin url kullandik

## Önemli: Burada yazdigimiz user aslinda bir ID. Bu ne demek?   Biz portfolio = models.URLField(blank=True)  yazdigimizda,  portfolio degiskenine django tarafindan bir url atamasi yapilir. yani bu degiskenin degeri artik bir url dir. ImageField kullandigimizda degiskene foto atanir. OnetoOneField kullandigimizda ise user degiskenimize bir id atamasi yapilir. OnetoOneField  de textfield gibi bir field dir.  
# 
# onetoone iliskilerde, ikinci tabloda unique bir id üretilmek zorundadir. bunu da birinci tablodan yani django nun bize sagladigi tablodan, user create ederken üretiriz ve oradan aliriz. Aldigimiz bu id yi ikinci tablomuzda foreign key olarak kullaniriz. 

class UserProfile(models.Model):
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
        ## cascade den önce models yazilir

    def __str__(self):
        return self.user.username

    # class Meta:
    #     verbose_name_plural = "ali"

## Önemli:

## Admin panele gittigimizde; karsimiza üst tarafta Groups ve users cikacak
## alt tarafta ise User Profiles tablosu cikacak. 
## Groups ve users, djangonun authentication and authorization kismindan gelir. Biz bu iki tablo icin herhangi bir tanimlama yapmadik. Mevcut django tablolarini kullaniyoruz. 
## user Profiles kisminda ise Users yazar üzerinde.
## Bu user profiles tablomuzun, users app inden geldigini gösterir.

## Iki tablo arasinda onetoone iliski yaptik. yeni bir profil eklemek istedigimizde, yeni kullanici eklememize izin vermez. sadece var olan kullanicilar arasindan secim yapmamizi ister. Bunun sebebi sudur: "user" secenegi bizim tablomuzda olusturdugumuz 3 alandan bir tanesidir. Ve biz bu alanin onetoone olmasini istedik.

## Önemli bilgi: Bizim tablomuzda 3 tane alan bulunur. ilk iki alan db de normal isimleri ile görünür. ama 3. alan olan user, user ismi ile görünmez. Cünkü burada onetoone iliski var ve bu user_id ismi ile bir id olarak görünür. django ya ait User tablosu ile iliski halindedir.



