from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("Welcome to Homepage")


def about(request):
    return HttpResponse("Welcome to About Page")


def login(request):
    return HttpResponse("Welcome to Login Page")