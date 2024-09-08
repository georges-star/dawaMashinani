# Create your models here.
from django.db import models

class field_officers(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.IntegerField()
    county = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    # password = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'field_officers'

class counties(models.Model):
    county_name = models.CharField(max_length=100)

    def __str__(self):
        return self.county_name