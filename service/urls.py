from django.urls import path
from . import views

urlpatterns = [
    path('Engineers/', views.engineers, name='engineers'),
    path('Cleaners/', views.cleaners, name='cleaners'),
    path('Plumbers/', views.plumbers, name='plumbers'),
    path('Therapists/', views.therapists, name='therapists'),
    path('barbers/', views.barbers, name='barbers'),
    path('beauticians/', views.beauticians, name='beauticians'),
    path('AcCare/', views.acCare, name='acCare'),
    path('services/', views.services, name='services'),
]