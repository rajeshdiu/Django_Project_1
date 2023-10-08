from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from myApp.models import customUser

from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def home(request):
    
    return render(request,"myAdmin/adminhome.html")

