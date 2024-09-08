# Create your models here.
from django.db import models  
class reports(models.Model):
    pestName = models.CharField(max_length=200)
    diseaseName = models.CharField(max_length=200)
    countyName = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    recorded_by = models.CharField(max_length=200)

    # New fields to store location
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    class Meta:
        db_table = 'reports'
