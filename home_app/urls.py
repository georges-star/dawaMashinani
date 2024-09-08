from django.urls import path
from . import views

urlpatterns = [
    path('home_app/', views.adminPage, name='adminPage'),
]