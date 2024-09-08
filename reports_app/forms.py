from django import forms
from .models import *
from pests_app.models import pests
from counties_app.models import counties
from diseases_app.models import diseases
class reportsForm(forms.ModelForm): 
    # pestName = forms.ModelChoiceField(queryset =  pests.objects.all().values_list('pest_name', flat=True).distinct())
    pestName = forms.ChoiceField(choices=[(name, name) for name in 
    pests.objects.values_list('pest_name', flat=True).distinct()])
    # diseaseName = forms.ModelChoiceField(queryset =  diseases.objects.all().values_list('disease_name', flat=True).distinct())
    diseaseName = forms.ChoiceField(choices=[(name, name) for name in 
    diseases.objects.values_list('disease_name', flat=True).distinct()])
    # countyName = forms.ModelChoiceField(queryset =  counties.objects.all().values_list('county_name', flat=True).distinct())
    countyName = forms.ChoiceField(choices=[(name, name) for name in 
    counties.objects.values_list('county_name', flat=True).distinct()])
    class Meta:  
        model = reports
        fields = ['pestName', 'diseaseName', 'countyName']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.recorded_by = self.user.username
        if commit:
            instance.save()
        return instance

class SearchDiseaseForm(forms.Form):
    diseaseName = forms.ChoiceField(choices=[(name, name) for name in
    reports.objects.values_list('diseaseName', flat=True).distinct()],
    label="Select Disease"  # Custom label
    )
    created_at = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}),
    label="Enter Start Date"  # Custom label
    )
    updated_at = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}),
    label="Enter End Date"  # Custom label
    )

    class Meta:  
        model = reports
        fields = ['diseaseName', 'countyName']


class SearchPestForm(forms.Form):
    pestName = forms.ChoiceField(choices=[(name, name) for name in 
    reports.objects.values_list('pestName', flat=True).distinct()],
    label="Select Pest" # Custom label
    )
    created_at = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}),
    label="Enter Start Date"  # Custom label
    )
    updated_at = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}),
    label="Enter End Date"  # Custom label
    )


    class Meta:  
        model = reports
        fields = ['pestName', 'countyName']

class CountyStatusForm(forms.Form):
    countyName = forms.ChoiceField(choices=[(name, name) for name in
    reports.objects.values_list('countyName', flat=True).distinct()],
    label="Select County" #custom label
    )
    created_at = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}),
    label="Enter Start Date"  # Custom label
    )
    updated_at = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}),
    label="Enter End Date"  # Custom label
    )
    
    class Meta:  
        model = reports
        fields = ['countyName']
        