from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('forgot-pass/',views.forgot, name='forgot'),
    path('ragister/',views.ragister, name='ragister'),
]