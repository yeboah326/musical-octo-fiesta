from django import forms
from django.contrib.auth.models import User
from .models import Doctor

class DoctorUserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class DoctorCustomForm(forms.ModelForm):
    
    class Meta:
        model = Doctor
        fields = ['hospital', 'profilePicture']
