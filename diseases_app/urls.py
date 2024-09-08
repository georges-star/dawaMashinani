from django.urls import path
from . import views

urlpatterns = [
    path('createDisease/', views.create_disease, name='create_disease'),
    path('searchDisease/', views.retrieve_disease, name='retrieve_disease'),
    path('updateDisease/<int:pk>', views.update_disease, name='update_disease'),
    path('deleteDisease/<int:pk>', views.delete_disease, name='delete_disease'),
]