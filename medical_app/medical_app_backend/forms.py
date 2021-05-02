from django import forms
from django.contrib.auth.models import User
from .models import Doctor, Nurse

# Doctor Related Forms
class DoctorUserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class DoctorCustomForm(forms.ModelForm):
    
    class Meta:
        model = Doctor
        fields = ['hospital', 'profilePicture']

# Nurse Related Form
class NurseUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class NurseCustomForm(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = ['name', 'hospital','profilePicture'] 

