from django.contrib import admin
from django.urls import path
from accounts import views
from django.contrib.auth import logout
from django.shortcuts import redirect

def my_logout(request):
    logout(request)
    return redirect('/')

urlpatterns = [
    path('send_login_email', views.send_login_email, name='send_login_email'),
    path('login', views.login, name='login'),
    path('logout', my_logout, name='logout'),
]
