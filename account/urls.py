from django.urls import path
from . import views

urlpatterns = [
    path('registration', views.registration, name = 'Sign UP'),
    path('login', views.login, name = 'Log In'),
]