from django.urls import path
from . import views

urlpatterns = [
    # Provider Registration
    path('register/', views.register, name='provider_register'),
]