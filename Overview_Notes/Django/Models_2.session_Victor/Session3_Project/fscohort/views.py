
from django.shortcuts import render
from .models import Student

# Create your views here.


# def home(request):
#     return HttpResponse("Welcome to Homepage")

def index(request):
    return render(request, 'fscohort/home.html')


def number_of_student(request):
    students = Student.objects.all()
    num_of_students = Student.objects.count()
    context = {
        'students' : students,
        'num' : num_of_students
    }

    return render(request, 'fscohort/student_list.html', context)
