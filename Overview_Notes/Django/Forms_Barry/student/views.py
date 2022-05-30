from django.shortcuts import render, redirect
from .forms import StudentForm, StudentFormSimple
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "student/home.html")

## Not: kendi olusturdugumuz form veya model form dan hangisinin ismini view de form un karsisina yazarsak o calisir. yani isim degisikligi ypmamiz yeterli burada.

def student_page(request):
        # burada forms da modelden olusturdugumuz form dan bir instance türetiyoruz.
        # user in girdigi forma ait verileri alma ile ilgili notlar asagida (1)
    # print(request.POST)

    # form dolu ise post u koy degilse hicbirsey. normalde bu islemi if ile yapiyoruz
    # if request.method == post 
    form = StudentForm(request.POST or None) 
    if form.is_valid():
        ## foto kaydetmek icin su islemler yapilir.
        student = form.save()
        if "profile_pic" in request.FILES:
            # student.profile_pic = request.FILES["profile_pic"]
            ## alternatif:
            student.profile_pic = request.FILES.get("profile_pic")
            student.save()
        messages.success(request, "Student saved succesfully")
        return redirect("student")


    # eger manuel form kullansaydik tüm alanlari tek tek su sekilde alacaktik:
    # daha sonra student modeli cekip db ye kayit edecektik
    # first_name = form.cleaned_data.get("first_name")
    # last_name = form.cleaned_data.get("last_name")
    # password = form.cleaned_data.get("password")

    context = {
        "form" : form
    }
    messages.success(request, "Welcome to our Homepage")
    return render(request, 'student/student.html', context)



## biz form = StudentForm()  yazarak bos bir form olusturduk
# biz frontend de sayfayi refresh ettigimizde bizim terminalimize GET olarak bir yazi gelir ve terminalde bir hareketlilik olur. cünkü biz bir get islemi yaptik ve bos form return edildi. form dolu oldugu an post olur

## csrf token, django nun hackleme olaylarina karsi gelistiridgi bir güvenlik mekanizmasidir.

# (1) :  user tarafindan gönderilen formun kendisine, view icinde print(form) dedigimizde ulasiriz. ancak bu kod ile formun html kodlarina yani sablonuna ulasiriz.
## icindeki verilere ise request vasitasi ile ulasiirz.

## print(request.POST) yazdigimizda karsimiza form icinde olusturdugumuz field lara ait bilgiler ve csrf token cikar karsimiza.

## is_valid() :  bizim formumuzda ilk 2 alan zorunlu son iki alan ise degil. bu iki alan zorunlu oldugu icin bos biraktigimizda front end tarafi bizi uyariyor. ancak buaralara space koydugumuzda front end i kandirabiliyoruz. iste bunun önüne gecebilmek icin; model den türettigimiz formun bir özelligi olan is_valid i kullanarak bir kontrol yapiyoruz. ve db ye formu save islemini daha sonra gerceklestiriyoruz.

## Database deki verilerimi görmenin iki yolu var. birisi sqlite, digeri admin panel

## redirect:  formu doldurup submit ettigimizde; formun ici dolu kaliyor ve her tikladigimizda ayniverileri db ye yeniden kaydediyor. bunun önüne gecmek iin post isleminde sonra user i baska bir sayfaya yönlendiriyoruz.  
## eger user formu doldurduktan sonra yine form sayfasinda kalsin ancak formun ici bos olsun istiyorsak, bu durumda redirect islemi icine yine student yazilir ve ayni sayfa render edilir. bu durumda önce post islemi yapilir daha sonra get islemi ypilarak bos form gösterilir.

## student = form.save()  yazdigimizda; hem database e form u kaydeder hem de db ye kaydettigi verilerin aynisini student degiskenine atar.