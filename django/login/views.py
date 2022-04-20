from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "login/index.html")

def signup(request):
    return render(request, "login/signup.html")

def signin(request):
    return render(request, "login/login.html")

def signout(request):
    pass
