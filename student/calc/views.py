from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def home(requests):
    return HttpResponse("Hello World!")

def login(requests):
    return render(requests,'login.html')

def signup(requests):
    return render(requests,'signup.html')
 
def home(requests):
    firstname="Virat"
    age=55
    return render(requests,'home.html',{'name':firstname,'age':age})

def add(requests):
    val1=int(requests.POST['num1'])
    val2=int(requests.POST['num2'])
    val3=val1+val2
    return render(requests,'add.html',{'result':val3})