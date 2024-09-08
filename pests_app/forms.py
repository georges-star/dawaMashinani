from django import forms
from .models import pests

class pestsForm(forms.ModelForm):  
    class Meta:  
        model = pests
        fields = "__all__"