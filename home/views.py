from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render ,  HttpResponse
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate


# Create your views here.
def index (request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def login (request):
    if request.method=="post":
        username = request.post.get('username')
        password = request.post.get('password')
        user = authenticate(username='username', password='password')
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request,'login.html') 

    return render(request,'login.html') 

def logout (request):
    logout(request)
    return redirect("/login")