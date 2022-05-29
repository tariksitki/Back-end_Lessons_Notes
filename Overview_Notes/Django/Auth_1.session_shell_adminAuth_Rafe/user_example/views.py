from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def home_view(request):    
    return render(request, "user_example/home.html")



    ## basit bir view sadece bir sayfa render ediyor ama bu sayfaya girmek icin login olmak sart kosuyoruz. login olmayan bir user girmek isterse onu login sayfasina yönlendiriyoruz.

@login_required  
def special(request):    
    return render(request, "user_example/special.html")



    #### register
    ## buradaki form u import ediyoruz yani kendimiz olusturmadik, djangonun hazir formlarindan aldik

    ## Bu projede yazdigimiz tek view budur. cünkü 8000/accounts/ url sinde baktigimizda, register icin hazirlanmis default bir url yoktu. password_change  password_reset login logour bu 4 baslik icin hazir template ler hazir url ler oldugu icin ise bazilarini direkt olarak kullandik, bazilarinda ise ufak degisiklikler yapmak zorunda kaldik. cünkü normal kullanicilarin admin sayfasina gitmelerini istemiyoruz.

def register(request):
    if request.method == "POST":
            ## burada formun icini bilgi ile dolduruyoruz
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            ## su ana kadar gecerli bir sekilde doldurulan formu kaydettik ama bu bizim icin yeterli degil. register olan bir user in login de olmasini istiyoruz. Bunun icin bazi bilgilere ihtiyacimiz var.

                ## normalde sadece cleaned_data da calisir ama get ile daha iyi calisir.
                ## get icine yazdigimiz verileri, formun oldugu browser sayfasinda inspect yaptik. elimizdeki iki inputun html verilerine baktik. birisinde name="username"  digerinde name="password1" yaziyor
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
                ## password1 yazmazsak hata verir
            
            user =authenticate(username = username, password = password)
            login(request, user)
            return redirect("home")

        ## yukaridaki islemler post islemi icin gecerli idi. Asagidaki islemler ise get islemleri icin gecerlidir.
    form = UserCreationForm()
    context = {
        "form" : form
    }
    return render(request, "registration/register.html", context)