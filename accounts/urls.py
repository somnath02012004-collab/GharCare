from django.urls import path
from . import views

urlpatterns = [
    path('admins/',views.admins, name='admins'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('forgot-pass/', views.forgot, name='forgot'),
    path('register/', views.register, name='register'),
    path('signup-success/', views.signup_success, name='signup_success'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
]