from django.contrib import admin
from django.urls import path
from myProject import views,adminviews,staffviews,studentviews

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.signupPage,name="signupPage"),
    path("loginPage",views.loginPage,name="loginPage"),
    path("homePage",views.homePage,name="homePage"),
    path("logoutPage",views.logoutPage,name="logoutPage"),

    #admin Panel
    path("myAdmin/home", adminviews.home, name="adminHome"),
    
    #Staff Panel
    path("staff/home", staffviews.home, name="staffHome"),
    
    #StudentPanel
    path("students/home", studentviews.home, name="studentHome"),
]
