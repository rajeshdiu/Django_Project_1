from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from myApp.models import customUser
from django.contrib import messages
from django.contrib import messages
from myApp import EmailBackEnd

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

from django.http import HttpResponse  # Import HttpResponse

from django.shortcuts import render
from django.contrib import messages

def loginPage(request):
    error_messages = {
        'username_error': 'Username is required.',
        'password_error': 'Password is required.',
        'login_error': 'Invalid username or password. Please try again.',
    }

    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("pass")
        
        if not username:
            messages.error(request, error_messages['username_error'])
        elif not pass1:
            messages.error(request, error_messages['password_error'])
        else:
            user =authenticate(request, username=username, password=pass1)

            if user is not None:
                user_type = user.user_type

                if user_type == "1":
                    return HttpResponse("Admin")
                elif user_type == "2":
                    return HttpResponse("Staff")
                elif user_type == "3":
                    return HttpResponse("Students")
            else:
                messages.error(request, error_messages['login_error'])

    return render(request, "login.html")


def homePage(request):
    
    return render(request,"base.html")



