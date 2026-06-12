from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

from bookings.models import Booking
from accounts.models import ServiceProvider
from django.contrib.auth.models import User
from .models import Service


def admin_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.is_superuser:

            login(request, user)

            messages.success(
                request,
                f"Welcome {user.username}"
            )

            return redirect('admin_dashboard')

        messages.error(
            request,
            "Invalid Admin Credentials"
        )

    return render(
        request,
        'admin-login.html'
    )


@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):

    bookings = Booking.objects.all().order_by('-created_at')

    providers = ServiceProvider.objects.all().order_by('-created_at')

    total_users = User.objects.count()

    total_bookings = Booking.objects.count()

    pending_bookings = Booking.objects.filter(
        status='Pending'
    ).count()

    completed_bookings = Booking.objects.filter(
        status='Completed'
    ).count()

    pending_providers = ServiceProvider.objects.filter(
        status='pending'
    ).count()

    approved_providers = ServiceProvider.objects.filter(
        status='approved'
    ).count()

    context = {
        'bookings': bookings,
        'providers': providers,

        'total_users': total_users,
        'total_bookings': total_bookings,

        'pending_bookings': pending_bookings,
        'completed_bookings': completed_bookings,

        'pending_providers': pending_providers,
        'approved_providers': approved_providers,
    }

    return render(
        request,
        'admin-dashboard.html',
        context
    )


@user_passes_test(lambda u: u.is_superuser)
def approve_provider(request, provider_id):

    provider = get_object_or_404(
        ServiceProvider,
        id=provider_id
    )

    provider.status = 'approved'
    provider.save()

    messages.success(
        request,
        f"{provider.full_name} approved successfully"
    )

    return redirect('admin_dashboard')


@user_passes_test(lambda u: u.is_superuser)
def reject_provider(request, provider_id):

    provider = get_object_or_404(
        ServiceProvider,
        id=provider_id
    )

    provider.status = 'rejected'
    provider.save()

    messages.success(
        request,
        f"{provider.full_name} rejected"
    )

    return redirect('admin_dashboard')


@user_passes_test(lambda u: u.is_superuser)
def update_booking_status(
    request,
    booking_id,
    status
):

    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    booking.status = status
    booking.save()

    messages.success(
        request,
        f"Booking updated to {status}"
    )

    return redirect('admin_dashboard')

def service_providers(request):

    providers = ServiceProvider.objects.filter(
        status='approved'
    )

    return render(
        request,
        'service_providers.html',
        {
            'providers': providers
        }
    )

def provider_requests(request):

    requests = ServiceProvider.objects.filter(
        status='pending'
    )

    return render(
        request,
        'provider_requests.html',
        {
            'requests': requests
        }
    )

def users_list(request):

    users = User.objects.filter(
        is_superuser=False
    )

    return render(
        request,
        'users.html',
        {
            'users': users
        }
    )

def services_list(request):

    services = Service.objects.all()

    return render(
        request,
        'services.html',
        {
            'services': services
        }
    )