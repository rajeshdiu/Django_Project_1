from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from myApp.models import customUser

from django.contrib import messages

def signupPage(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")

        if pass1 != pass2:
            return HttpResponse("Passwords do not match")
        else:
            # Use your customUser model to create a user
            myuser = customUser.objects.create_user(username=uname, email=email, password=pass1)
            myuser.save()
            return redirect("loginPage")

    messages.success(request, 'Signup successful.')
    return render(request, "signup.html")

def loginPage(request):
    
     if request.method=="POST":
        username=request.POST.get("username")
        pass1=request.POST.get("pass")
        user=authenticate(request,username=username,password=pass1)
        
        if user is not None:
            login(request,user)
            return redirect("homePage")
        else:
            return HttpResponse("username not found")
    
     return render(request,"login.html")

def homePage(request):
    
    return render(request,"base.html")