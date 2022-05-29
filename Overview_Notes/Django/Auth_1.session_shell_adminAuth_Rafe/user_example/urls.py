from django.urls import path
from .views import home_view, special, register
from django.contrib.auth import views as auth_views
## bu sekilde isim degistirdik ki bunun normal viewlerden farkli oldugunu ve auth ile ilgili oldugunu belirttik.
from django.contrib.auth.views import PasswordChangeDoneView

urlpatterns = [
    path('', home_view, name="home"),
    path('special/', special, name="special"),
    path('register/', register, name="register"),

    ## Note: password change icin view yazmadik. Bu nedenle view dan degil direkt django dan hazir form import ettik. Ayrica docs da belirilen formata uygun olmayan kendimiz yazdigimiz bir path ve isim yazdik. normalde path yazarken basinda 8000/accounts/ olmasi gerekirdi.
    ## Bunun haricinde, normalde admin panelde hazir bir password change sayfasi var. ama bu sayfada admin ile ilgili bilgilerde bulundugundan biz bu sayfayi kullanmak istemedik. o nedenle yeni template yaptik

    path('change-password/', auth_views.PasswordChangeView.as_view(template_name="registration/change-password.html"), name="change-password"),


        ### bu kodu done sayfasini override etmek icin yazdim ama olmadi
    # path('password_change/done/', PasswordChangeDoneView.as_view(template_name="registration/password_change_done.html"), name='password_change_done'),



    ### Reset password:
    ## burada da view yazmayacagiz. class based view i direkt burada kullanacagiz.
    ## rest 4 tane template sayfasi icerir:
    # 1: bizden email istenen sayfa
    # 2: reset done (email gönderildi yazan sayfa)
    # 3: email e tikladigimizda gittigimiz sayfa olacak burada bizden yeni password girmemizi isteyecek. girip onayladiktan sonra 4. sayfaya onay sayfasina gönderecek
    # 4: email i onayladiktan sonra email done sayfasi

    path('reset-password/', auth_views.PasswordResetView.as_view(template_name="registration/reset-password.html"), name="reset-password"),



    ### Login,  Logout:
    ## Bu iki islem gerceklestikten sonra user i hangi sayfaya yönlendirecegimizi settings.py da belirliyoruz. 
    #  LOGOUT_REDIRECT_URL = '/'  bu kodlari yaziyoruz.

    ## Logout sayfasi olarak django ya ait hazir sayfayi kullandik.
    ## login icin ise docs a göre sadece registration klasörü altinda login.html adinda bir dosya olusturmamiz yeterli. bunun icin url de yazmadik view da  


]






