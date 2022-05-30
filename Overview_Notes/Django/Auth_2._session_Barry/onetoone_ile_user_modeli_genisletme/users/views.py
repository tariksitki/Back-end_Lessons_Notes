from multiprocessing import context
from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm  ## login de kullandik
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from .forms import UserForm, UserProfileForm

###Önemli Note: 
##  Admin dashboard a giris yapabilmek icin, user in ya superuser omasi yada staff olmasi gerekir. eger bunlardan ikisi de yoksa, hic giris yapamaz. eger sadece staff ise giris yapabilir ama degisiklik yapamaz sadece okuma yetkisi. 

def home(request):
    # print(request.user)
    return render(request, 'users/home.html')
    ## view lerimiz icerisine request aldiklari icin template kisminda bu request icindeki user larin login olup olmadiklarini kullanarak, sayfada hosgeldin diye ismi ile hitap ederiz. 


def user_logout(request):
    messages.success(request, "You logged out")
    logout(request)
    return redirect("home")



# Dikkat: forms.py da model = UserProfile derken en sona () koymadik.
# ama burada form_profile = UserProfileForm() derken koyuyoruz.

## Note: django da bir tusa tiklandiginda onclick olmadigi icin tüm islemler view da tanimlanir. Kullanici template de bulunan register tusuna tikladiginda formun altinda bulunan submit butonu vasitasi ile form submit olur. Ve biz o formun icinin bos olup olmadigini view de kontrol ederek ona göre yapmak istedigimiz tüm islemleri burada yapariz.

## Biz register view i icerisine, iki tane form koydugumuz icin, front end de iki form birlestirilmis sekilde kullaniciya gösterilir. Ve kullanici birlestirilmis bu formu doldurdugunda, hem user tablosunda bir user olusur hem de profile tablosunda bir user profile olusur.

def register(request):
    form_profile = UserProfileForm()
    form_user = UserForm()
    if request.method == "POST":
        form_profile = UserProfileForm(request.POST, request.FILES)
        form_user = UserForm(request.POST)
        ## cok önemli: döküman ve resimler db ye kaydedilmez. Bu nedenle profile formunda FILES kullanmak zorundayiz.

        if form_profile.is_valid() and form_user.is_valid():
            user = form_user.save()
            profile = form_profile.save(commit=False) ## aciklama asagida (1):
            profile.user = user 
            profile.save()

            ## register olan kisinin ayni zamanda login olmasini istiyoruz.
            login(request, user)
            messages.success(request, "Registered succesfully")

            return redirect("home")

    context = {
        "form_profile" : form_profile,
        "form_user" : form_user
    }
        ## form bos gelirse sunu yap:
    return render(request, "users/register.html", context)


# (1): Burada form_profile i direkt save demedik. Cünkü böyle söylemis olsaydik; bize user i tanimadigini söyleyecek ve hata verecekti.
# # Burada yaptigimiz islem tam manasi ile su:
# iki tablomut onetoone ile birbirine bagli oldugu icin;  ikinci tablomuzda user_id belirlemeden iki tabloyu birbirine baglayamiyoruz.
# user form direkt save edilir problemsiz. ve böylece o anda olusturdugumuz user ile islem yapariz.
# daha sonra commit yapmadan bize bir profile olustur deriz. commit yapmak db ye kaydetmek demek.
# sonra profile in user ini belirleriz.  ve save ederiz. 





##  Önemli: login islemlerinde AuthenticationForm kullanacagiz.
# Bu forma özel birkac husus bulunmaktadir.
# 1: form = AuthenticationForm()  burada () icinde formun icini doldururuz.
# bu islemden sonra bir daha request.method == post demeye gerek kalmaz. direkt olarak is_valid sorgusu yapariz.
# 2: bu form ile islem yaparken user bilgisine ihtiyac duydugumuzda kullanamk icin user degiskeni üretirken bize "get_user" methodu ile kolaylik saglar. Bu method sadece bu forma özeldir.

## AuthenticationForm kullandigimizda default olarak bize sadece username ve password secenekleri sunar.

def user_login(request):
    form = AuthenticationForm(request, data = request.POST)

    if form.is_valid():
        user = form.get_user()
        if user:
            messages.success(request, "You logged in succesfully")
            login(request, user)
            return redirect("home")

        ## form bos gelirse:
    return render(request, "users/user_login.html", {"form" : form})

    ### Önemli: biz burada login islemi icin hazir AuthenticationForm kullandik. 
    # Bu form bizim yapmamaiz gereken bircok islemi otomatik yapti.  Eger kendimizin manuel olusturdugu bir form ile islem yapsaydik; icerisindeki verileri su sekilde alacaktik:

    #username = form.cleaned_data.get("username")
    #password = form.cleaned_data.get("password")
    #user = authenticate(username=username, password=password)
    # bu bilgileri elde ettikten sonra normal if islemleri olacakti.
    # Su an hazir form kullandigimizdan dolayi; ger login islemi basarisiz olursa, otomatik olarak kendisi hata mesaji verir. ancak diger durumda bizim onu da kendimiz vermemiz gerekirdi. Bunun icin else diyerek messages.error kullanmamiz gerekirdi.


