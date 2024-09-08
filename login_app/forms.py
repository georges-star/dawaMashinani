# from django import forms
# # from .models import CustomUser
# from .models import CustomUser
# from field_officers_app.models import field_officers

# class UserForm(forms.ModelForm):
#     role = forms.ChoiceField(choices=[('field officer', 'field officer')])
#     # role = forms.ChoiceField(choices=[(name, name) for name in 
#     # CustomUser.objects.values_list('role', flat=True).distinct()])
#     password = forms.CharField(widget=forms.PasswordInput)
#     phone_number = forms.CharField(max_length=10)
#     class Meta:
#         model = CustomUser
#         fields = ['first_name', 'last_name', 'email', 'phone_number', 'role', 'username', 'password']

# def clean_username(self):
#         username = self.cleaned_data.get('username')
#         if not field_officers.objects.filter(username=username).exists():
#             raise forms.ValidationError("This username is not registered in the system. Please use the correct username.")
#         return username

# class UserLoginForm(forms.Form):
#     role = forms.ChoiceField(choices=[(name, name) for name in 
#     CustomUser.objects.values_list('role', flat=True).distinct()])
    
#     username = forms.CharField(max_length=100)

#     password = forms.CharField(widget=forms.PasswordInput)


from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from field_officers_app.models import field_officers

class UserForm(UserCreationForm):
    role = forms.ChoiceField(choices=[('field officer', 'field officer')])
    phone_number = forms.CharField(max_length=10)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'role', 'username', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not field_officers.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is not registered in the system. Please use the correct username.")
        return username

class UserLoginForm(forms.Form):
    role = forms.ChoiceField(choices=[(name, name) for name in 
    CustomUser.objects.values_list('role', flat=True).distinct()])
    
    username = forms.CharField(max_length=100)

    password = forms.CharField(widget=forms.PasswordInput)