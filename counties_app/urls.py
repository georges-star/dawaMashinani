from django.urls import path
from . import views

urlpatterns = [
    path('createCounty', views.create_county, name='create_county'),
    path('searchCounty/', views.retrieve_county, name='retrieve_county'),
    path('updateCounty/<int:pk>', views.update_county, name='update_county'),
    path('deleteCounty/<int:pk>', views.delete_county, name='delete_county'),
]