from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import StudentForm
from .models import Student

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.base import TemplateView


## Note: func based i class based e dönüstürürken 2 yöntem var:
# Birincisi önce view yazip sonra url de kullanmak
# Ikincisi ise dogrudan tüm islemleri urls.py da yapmaktir. views da hicbir sey yapmiyoruz.
## Önemli: Eger context eklemeyeceksek dogrudan django TemplateView kullanmak istersek, view da islem yapmaya gerek yok. 2. yöntem mantikli. ama hem gjango temp kullanacak hem de kendimiz de context eklemeleri yapacaksak 1. yöntem olmali.  

#Note: Django;  cok sik kullanilan view lar icin class based view lar hazirlamis.
# Bunlar:
# 1: TemplateView:  Home.html icin kullandik.  Eger elimizde bir template varsa, ve bu template üzerinde herhangi bir segisiklik yaparak yada yapmayarak bunu kullaniciya göstermek istersek kullanilirlar.
# 2: Generic Display Views:
    # a: ListView:  database de bulunan student list gibi listeleri göstermek icin hazir template
    # b: DetailView: detail page icin hazir view
# 3: son olarak da crud islemleri icin hazirlanmis hazir view ler

    #func
def home(request):
    return render(request, "fscohort/home.html")

    #class
class HomeView(TemplateView):
    template_name = "fscohort/home.html"
    # burada template_name haricinde bir isim kullandigimizda hata aliyoruz.
    ## eger context eklemek istersek su sekilde:

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['latest_articles'] = Article.objects.all()[:5]
    #     return context






    # func
def student_list(request):
    students = Student.objects.all()
    context = {
        "students":students
    }
    return render(request, "fscohort/student_list.html", context)



    # class based (yukarida import ettik ListView):

class StudentListView(ListView):
    #burada db den hangi tabloyu hangi listeyi model olarak alacagini yaziyoruz.
    model = Student
    context_object_name: "students"
    # Önemli: Docs a göre, eger burada context name i ni student_name olarak vermis olsak, bu durumda bunu tekrar burada yazmaya gerek yok. django bunu algiliyor. Ama hoca daha önce template ihazirladigi icin ve bizim template icin de context i cagirma seklimiz {{ student }} oldugu icin biz burada yazmak zorunda kaldik.

    # istersek paginatatin kullanabiliyoruz. su sekilde:
    # paginate_by = 10

    ## Önemli: Burada normalde template_name de yazmamiz gerekir.
    # ancak bizim db mizdeki listemizi gösterecegimiz html template imizin adi student_list yani _  ile bittigi icin yani docs daki standarta uygun oldugu icin tekrardan burada yazmiyoruz.
    # yani docs su sekilde istiyor:
    # appismi/modelismi_list.html  bu bizde suna tekabül eder.
    # fscohort/student_list.html  (bizim zaten böyle)

    ## listView üzerinde farkli farkli attribute lar kullanabiliriz. Bunlara docs dan bakmamiz lazim













def student_add(request):
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list")

    context = {
       "form":form
    }
    return render(request, "fscohort/student_add.html", context)


    ## class based:
    ## attribute olarak template_name_suffix ve birde object var. docs dan bakilabilir



class StudentCreateView(CreateView):
    model = Student 
    form_class = StudentForm
    template_name = "fscohort/student_add.html"
    success_url = reverse_lazy("list")

        ### Bir field i overwrite etmek. Yani number field zorunlu degil. eger kullanici number girmedi ise, otomatik olarak 9999 atansin. 
        ## Bunlarin hepsi docs da var ama bizim projemizde nerede oldugunu bulmak istersek birincisi ctrl ile bu kod üzerine tikla
        ## ikincisi ise  env klasörü icinde Lib klasörü ve daha sonra bu dosyanin en yukarisinda import ederken takip ettigimiz siralamaya göre klasör isimlerini takip edersek, tüm bu kodlara ulasabilirz.
        ## geri planda class based lerde django bizim yerimize post ve get islemlerini ayirir.
        ## burada dikkat.  model de number alani unique olursa, birden kullaniciya 9999 verdiginde hata aliriz

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
       
        if not self.object.number:
            self.object.number = 9999
        self.object.save()
    
        return super().form_valid(form)  












    ### details page
def student_detail(request,id):
    student = Student.objects.get(id=id)
    context = {
        "student":student
    }

    return render(request, "fscohort/student_detail.html", context)

    ## class based:

class StudentDetailView(DetailView):
    model = Student    ## hdb de hangi tablodan veri cekecegimiz
    pk_url_kwarg = "id"  ## eger pk ile calisacaksak bu zaten default oldugu icin 
                        ## burada yazmaya ihtiyac yoktu. ama id istiyorsak bu sekilde
    ## benim database de student lerin id si 3 den basliyor. arama ona göre olmali



















def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect("list")

    context= {
        "student":student,
        "form":form
    }

    return render(request, "fscohort/student_update.html", context)

    ## default  appname/modelname_form.html olsaydi template_name yazmamiza gerek yoktu. 


    ### class based:

class StudentUpdateView(UpdateView):
    model = Student 
    form_class = StudentForm
    template_name = "fscohort/student_update.html"
    success_url = reverse_lazy("list")
    # burada success_url nin alternatif yolu olarak, path in adresi yazilarak yapilir.
    # success_url = "/student_list/"
    ## Burada pk_url_kwargs kullanmadik, cünkü id yerine pk kullandik
















def student_delete(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.delete()
        return redirect("list")

    context= {
        "student":student
    }
    return render(request, "fscohort/student_delete.html",context)



    # class based:
    ## docs da delete methodunun class based i icin post yöntemi ile gidildiginde bu islemi kendisi yaptigini, get yöntemi ile gidildiginde sadece user a gösterdigini yaziyor. Bu nedenle class based in delete inde func da oldugu gibi, request.method == post yazmiyoruz

class StudentDeleteView(DeleteView):
    model = Student 
    template_name = "fscohort/student_delete.html"
    # template_name default a uygun degil
    success_url = reverse_lazy("list")

    ## Not: su ana kadar ki kodlar ile delete islemi calismaz. Bunun icin iki yöntem var.
    # Birinci yöntem:
    # pk_url_kwarg = "id"

    ## ikinci yöntem ise url deki <int:id>  kismini pk yapmaktir
    # biz bu kez ikinci yöntemi yaptik

