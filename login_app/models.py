from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=20)  # Assuming roles like 'admin', 'user', etc.
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

# class User(models.Model):
#     firstname = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=15)
#     role = models.CharField(max_length=20)  # Assuming roles like 'admin', 'user', etc.
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
