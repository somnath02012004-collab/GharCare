from django.urls import path
from . import views

urlpatterns = [
    path('Engineers/', views.engineers, name='engineers'),
    path('AcCare/', views.acCare, name='acCare'),
    path('services/', views.services, name='services'),
]