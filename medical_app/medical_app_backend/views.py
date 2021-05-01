from django.shortcuts import render
from django.contrib.auth.models import Group
from . import forms
from django.http import HttpResponseRedirect

# Create your views here.

def doctorSignUpView(request):
    doctorUserForm = forms.DoctorUserForm()
    doctorCustomForm = forms.DoctorCustomForm()
    doctorForms = {'doctorUserForm': doctorUserForm,'doctorCustomForm': doctorCustomForm}
    if request.method=='POST':
        doctorUserForm = forms.DoctorUserForm(request.POST)
        doctorCustomForm = forms.DoctorCustomForm(request.POST,request.FILES)
        if doctorUserForm.is_valid() and doctorCustomForm.is_valid():
            user = doctorUserForm.save()
            user.set_password(user.password)
            doctor = doctorCustomForm.save(commit=False)
            user.save()
            doctor.user = user
            doctor = doctor.save()
            doctorGroup = Group.objects.get_or_create(name='DOCTOR')
            doctorGroup[0].user_set.add(user)
        return HttpResponseRedirect('doctorLogIn')
    return render(request,'doctors/doctorSignUp.html', context=doctorForms)

