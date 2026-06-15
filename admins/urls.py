from django.urls import path
from . import views

urlpatterns = [

    # Admin Login
    path(
        '',
        views.admin_login,
        name='admin_login'
    ),

    # Dashboard
    path(
        'admin-dashboard/',
        views.admin_dashboard,
        name='admin_dashboard'
    ),

    # Service Providers
    path(
        'providers/',
        views.service_providers,
        name='service_providers'
    ),

    # Provider Requests
    path(
        'provider-requests/',
        views.provider_requests,
        name='provider_requests'
    ),

    # Users
    path(
        'users/',
        views.users_list,
        name='users_list'
    ),

    # Services
    path(
        'services/',
        views.services_list,
        name='services_list'
    ),

    # Approve Provider
    path(
        'provider/approve/<int:provider_id>/',
        views.approve_provider,
        name='approve_provider'
    ),

    # Reject Provider
    path(
        'provider/reject/<int:provider_id>/',
        views.reject_provider,
        name='reject_provider'
    ),

    # Update Booking Status
    path(
        'booking/<int:booking_id>/<str:status>/',
        views.update_booking_status,
        name='update_booking_status'
    ),

]
