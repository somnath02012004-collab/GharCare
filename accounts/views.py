from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import ServiceProvider
from django.contrib.auth.decorators import login_required
from bookings.models import Booking
def signup(request):

    if request.method == "POST":

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username') or email
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # empty field check
        if not first_name or not last_name or not email or not username or not password or not confirm_password:
            messages.error(request, "Please fill all the fields!")
            return redirect('signup')

        # check password
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

       # check duplicate email
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('signup')

        # check duplicate username
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
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
        return redirect('signup_success')

    return render(request, 'signup.html')

def login(request):

    if request.method == "POST":

        name = request.POST.get('name')
        password = request.POST.get('password')

        user_obj = User.objects.filter(email=name).first()

        username = user_obj.username if user_obj else name

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            auth_login(request, user)

            messages.success(
                request,
                f"Welcome back, {user.first_name}!"
            )

            return redirect('dashboard')

        else:

            messages.error(
                request,
                "Invalid Email/Username or Password!"
            )

            return redirect('login')

    return render(request, 'login.html')

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

def signup_success(request):
    return render(request, 'signup_successfull.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):

    total_bookings = Booking.objects.filter(
        user=request.user
    ).count()

    pending_bookings = Booking.objects.filter(
        user=request.user,
        status='Pending'
    ).count()

    completed_bookings = Booking.objects.filter(
        user=request.user,
        status='Completed'
    ).count()

    recent_bookings = Booking.objects.filter(
        user=request.user
    ).order_by('-created_at')[:5]

    context = {
        'total_bookings': total_bookings,
        'pending_bookings': pending_bookings,
        'completed_bookings': completed_bookings,
        'recent_bookings': recent_bookings,
    }

    return render(request, 'dashboard.html', context)