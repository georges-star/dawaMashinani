from django.urls import path
from . import views

urlpatterns = [
    path('countyStatus/', views.countyStatus, name='search_status'),
    path('findDisease/', views.findDisease, name='search_disease'),
    path('findPest/', views.findPest, name='search_pest'),
    path('createReport', views.create_report, name='create_report'),
    path('searchReport/', views.retrieve_report, name='retrieve_report'),
    path('updateReport/<int:pk>', views.update_report, name='update_report'),
    path('deleteReport/<int:pk>', views.delete_report, name='delete_report'),
    path('test/', views.test, name='test'),
]