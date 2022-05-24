
from django import forms
from .models import Student


# Burada fom olusturduk. Bunu views araciligi ile template e gönderecegiz. Sebebei kullanicinin veri girisi yapabilmesi icin bos bir form a ihtiyaci var.

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        labels = {"first_name" : "Adiniz", "last_name" : "Soyadiniz", "number" : "Numaraniz"}

