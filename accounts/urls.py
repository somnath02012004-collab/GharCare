from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
     path('logout/', views.logout_user, name='logout'),
    path('forgot-pass/', views.forgot, name='forgot'),
    path('register/', views.register, name='register'),
    path('signup-success/', views.signup_successfull, name='signup_success'),

    path('dashboard/', views.dashboard, name='dashboard'),
]