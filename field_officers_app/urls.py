from django.urls import path
from . import views

urlpatterns = [
    path('createOfficer', views.create_field_officer, name='create_field_officer'),
    path('searchOfficer/', views.retrieve_field_officer, name='retrieve_field_officer'),
    path('updateOfficer/<int:pk>', views.update_field_officer, name='update_field_officer'),
    path('deleteOfficer/<int:pk>', views.delete_field_officer, name='delete_field_officer'),
]