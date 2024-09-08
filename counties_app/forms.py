from django import forms
from .models import counties

class countiesForm(forms.ModelForm):  
    class Meta:  
        model = counties
        fields = "__all__" 