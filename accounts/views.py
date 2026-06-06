from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')


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

    if request.method == "POST":
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:

            return render(request, 'signup.html', {
                'error': 'Passwords do not match',
                'hide_navbar': True
            })

        username = email

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )

        auth_login(request, user)

        return redirect('service')

    return render(request, 'signup.html', {
        'hide_navbar': True
    })