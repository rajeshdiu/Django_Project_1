from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from myApp.models import customUser


def home(request):
    
    return render(request,"staff/staffhome.html")