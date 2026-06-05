from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from .models import ServiceProvider



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

def register(request):

    if request.method == "POST":

        ServiceProvider.objects.create(
            full_name=request.POST.get('full_name'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            service=request.POST.get('service'),
            experience=request.POST.get('experience'),
            address=request.POST.get('address'),
            profile_picture=request.FILES.get('profile_picture'),
            id_proof=request.FILES.get('id_proof')
        )

        return redirect('register')

    return render(request, 'provider-register.html')