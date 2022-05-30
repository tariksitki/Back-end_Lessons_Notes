

from django import forms
from .models import Student

## forms.py adinda bir dosya olusturmak zorunda degiliz. form ile ilgil kodlari views.py da da yazabilirz. ancak biz kodlarimiz derli toplu olsun diye olusturuyoruz.

# Form olusturmanin iki farkli yolu vardir. Birincisi, tek tek tüm field lari kendimiz olusturmaktir. Ikincisi ise model kullanmaktir.

# birinci: (forms.Form dan türetilir)
## Not: Burada normal database e tablo olusturmak icin models de yazdigimiz veriler gibi alanlar yaziyoruz ama class tanimlamasi yaparken forms.Form dedigimiz icin bizim yazdigimiz bu alanlari kendisi forma dönüstürür

# Bu formu kullanmyaya gerek yok cünkü;
# her bir alan tek tek olusturulur.
# database e veri gönderme esnasinda extra islemler gerekir.
# model form da tek bir save komutu ile db ye veri gönderilir.

class StudentFormSimple(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    number = forms.IntegerField(required=False)



# Ikinci Method: (Burada forms.Modelform dan türetilir)
## models den StudentForm import edilir.

## Modelform olusturmanin adimlari:
# ilk olarak model.py da modeli olustur.
# 1: app icinde forms.py olustur
# 2: Bunun icinde form u import etmek gerekir
# 3: asagidaki form u olustur
# 4: view.py da func olustur (icinde context ve form degiskeni olmali)
# 5: daha sonra template icindeki student.html e giderek burada model icin template olusturulur.


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

        # istersek tüm field lari almadan istediklerimizi alabilirz.
        # bu durumda liste formati kullanmamiz gerekir
        # fields = ["first_name", "last_name"]

        # istersek modelden gelen label isimlerini degistirebilirz.
        labels = {"last_name" : "Surname"}


        ## Not: docs a bakarak buraya class atamasi yapilabilir ve widget lar degistirilebilir

