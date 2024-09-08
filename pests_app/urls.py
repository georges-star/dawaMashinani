from django.urls import path
from . import views

urlpatterns = [
    path('createPest', views.create_pest, name='create_pest'),
    path('searchPest/', views.retrieve_pest, name='retrieve_pest'),
    path('updatePest/<int:pk>', views.update_pest, name='update_pest'),
    path('deletePest/<int:pk>', views.delete_pest, name='delete_pest'),
]