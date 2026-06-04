from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')