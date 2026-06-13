from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('forgot-pass/',views.forgot, name='forgot'),
    path('register/',views.register, name='register'),
]