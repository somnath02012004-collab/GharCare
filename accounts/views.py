from django.contrib.auth import authenticate, login as auth_login
from .models import ServiceProvider
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password

def signup(request):

    if request.method == "POST":

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username') or email
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # check password
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        # check duplicate email
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('signup')

        # create user
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        user.save()

        messages.success(request, "Account created successfully!")
        return redirect('login')

    return render(request, 'signup.html')


def login(request):

    if request.method == "POST":

        name = request.POST.get('name')
        password = request.POST.get('password')

        user_obj = User.objects.filter(email=name).first()

        username = user_obj.username if user_obj else name

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('services')  # better than 'service'

        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'login.html')

def forgot(request):
    return render(request, 'forgot-pass.html')

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

def signup_success(request):
    return render(request, 'signup_success.html')

def dashboard(request):
    return render(request, 'dashboard.html')
