from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import ServiceProvider


def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not all([first_name, last_name, email, username, password, confirm_password]):
            messages.error(request, "All fields are required!")
            return redirect('signup')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect('signup')

        try:
            user = User.objects.create_user(
                username=username,
                email=email.lower(),
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()

            messages.success(request, "Account created successfully! Please login.")
            return redirect('signup_success')

        except Exception:
            messages.error(request, "Something went wrong. Please try again.")
            return redirect('signup')

    return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        password = request.POST.get('password')

        if not name or not password:
            messages.error(request, "Email/Username and Password are required!")
            return redirect('login')

        user_obj = User.objects.filter(email=name).first()
        username = user_obj.username if user_obj else name

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Your account is inactive.")
                return redirect('login')
        else:
            messages.error(request, "Invalid email/username or password!")
            return redirect('login')

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def forgot(request):

    return render(
        request,
        'forgot-pass.html'
    )


def register(request):
    if request.method == "POST":
        try:
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
            messages.success(request, "Registration request submitted successfully!")
            return redirect('home')
        except Exception:
            messages.error(request, "Something went wrong. Please try again.")
            return redirect('register')

    return render(request, 'provider-register.html')


@login_required(login_url='login')
def dashboard(request):
    context = {
        'user': request.user,
        'full_name': request.user.get_full_name() or request.user.username,
    }
    return render(request, 'dashboard.html', context)


def signup_successfull(request):
    return render(request, 'signup_successfull.html')