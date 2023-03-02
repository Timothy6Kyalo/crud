from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Student


def Home(request):
    return render(request, 'index.html')


def handlesignup(request):
    return render(request, 'signup.html')

def handlelogin(request):
    return render(request, 'login.html')
def updateData(request):
    return render(request,'edit.html')
def insertData(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        age=request.POST.get("age")
        gender=request.POST.get("gender")
        query=Student(name=name, email=email,age=age,gender=gender)
        query.save()
        return redirect('my-index')
    return render(request, 'index.html')
def deleteData(request):
    return render(request, 'index.html')
def handlelogout(request):
    return render(request, 'my-signup')
