from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User


def login(request):

    if request.method == "POST":

        name = request.POST.get('name')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(email=name).first()

        if user_obj:
            username = user_obj.username
        else:
            username = name


        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            auth_login(request, user)

            return redirect('service')

    return render(request, 'login.html', {
        'hide_navbar': True
    })


def signup(request):
    return render(request, 'signup.html', {
        'hide_navbar': True
    })

def forgot(request):
    return render(request, 'forgot-pass.html')