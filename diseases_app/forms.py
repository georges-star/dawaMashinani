from django import forms
from .models import diseases

class diseasesForm(forms.ModelForm):  
    class Meta:  
        model = diseases
        fields = "__all__" 