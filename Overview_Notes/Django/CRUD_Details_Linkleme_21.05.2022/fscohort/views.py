
from django.shortcuts import redirect, render
from .models import Student
from .forms import StudentForm


def index(request):
    return render(request, "fscohort/index.html")


### Simdi db den student verilerini cekecegiz ve bunu frontend de yayinlayacagiz:

    ## READ:

def student_list(request):
    students = Student.objects.all()
    context = {
        "students" : students
    }
    return render(request, "fscohort/student_list.html", context)



## template lerle islem yaparken get ve post kullaniriz sadece.
## okurken get. diger 3 islemde post methodu

    ####  WRITE:
# Not: Ilk etap da kullaninin bos bir form görmesi icin get methodu ile bos form return edilir. Daha sonra kullanici veri girdiginde method post olur. Eger Method post oldugunda da database e veri kaydetme islemleri yapilir. cünkü post oldugunda if condition icine girer
# iki form olsaydi, hangi formun submitine bastiysak onun verilerini alacakti

def student_add(request):
    form = StudentForm()
    # print(request.POST)
    
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list") 

    context = {
        "form" : form
    }

    return render(request, "fscohort/student_add.html", context)






        ##### UPDATE:
        # update isleminde sadece bir tane elemena ihtiyac oldugu icin id kullaniyoruz. peki id nereden geliyor bize? urls.py daki int:id den geliyor. Bu url buradaki func i tetikliyor.

        ## Formun kullaniciya ilk geldigi hali get ile geliyor. Kullanici verilerde degisiklik yaptiktan sonra update tusuna bastiginda post methodu ile geliyor.


def student_update(request, id):
    # print(request)
    student = Student.objects.get(id=id)
    # print(student)
    
    
    ## burada instance bir objecttir. form gelirken ici bos gelmesin bu object ile gelsin diyoruz. instance da bize modelFormun sagladigi kolayliklardan
    form = StudentForm(instance=student)
    print(form)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        ## Önemli: eger burada instance kullanmazsak, update etmez yeni eleman olusturur
        if form.is_valid():
            form.save()
            return redirect("student_list") 

    context = {
        "form" : form
    }

    return render(request, "fscohort/student_update.html", context)









    ###### DELETE:


def student_delete(request, id):
    student = Student.objects.get(id = id)
    
    if request.method == "POST":
        student.delete()
        return redirect("student_list")

    context = {
        "student" : student
    }
    return render(request, "fscohort/student_delete.html", context)






    ##### DETAIL:

def student_details(request, id):
    student = Student.objects.get(id = id)
    context = {
        "student" : student
    }

    return render(request, "fscohort/student_details.html", context)
