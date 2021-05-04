from django import forms
from django.contrib.auth.models import User
from .models import Doctor, Nurse, Report

# Doctor Related Forms
class DoctorUserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class DoctorCustomForm(forms.ModelForm):
    
    class Meta:
        model = Doctor
        fields = ['name','hospital', 'profilePicture']

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

class ReportUpdateForm(forms.ModelForm):

    class Meta:
        model =  Report
        fields = ['comments', 'completed']