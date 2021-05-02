from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from . import forms
from django.http import HttpResponseRedirect
from . import models
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

# -------------------- Checking User Status --------------------
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()

def is_nurse(user):
    return user.groups.filter(name='NURSE').exists()

# -------------------- After User Log In --------------------
def afterLogInView(request):
    if is_doctor(request.user):
        return redirect('doctorDashboard')
    if is_nurse(request.user):
        return redirect('nurseDashboard')

# -------------------- Doctor Related Views --------------------
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

@login_required(login_url='doctorLogIn')
@user_passes_test(is_doctor)
def doctorDashboardView(request):
    reportcount = models.Report.objects.all().filter(doctor_id=request.user.id).count()
    reports = models.Report.objects.all()
    doctorId = request.user.doctors.id
    doctorName = request.user.doctors.name
    # appointmentcount=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).count()
    # patientdischarged=models.PatientDischargeDetails.objects.all().distinct().filter(assignedDoctorName=request.user.first_name).count()

    # #for  table in doctor dashboard
    # appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).order_by('-id')
    # patientid=[]
    # for a in appointments:
    #     patientid.append(a.patientId)
    # patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid).order_by('-id')
    # appointments=zip(appointments,patients)
    dashboardInfo={
    'reportCount':reportcount,
    'doctorId': doctorId,
    'doctorName': doctorName,
    'reports': reports,
    }
    return render(request,'doctors/doctorDashboard.html',context=dashboardInfo)


# -------------------- Nurse Related Views --------------------
def nurseSignUpView(request):
    nurseUserForm = forms.NurseUserForm()
    nurseCustomForm = forms.NurseCustomForm()
    nurseForms = {'nurseUserForm': nurseUserForm,'nurseCustomForm': nurseCustomForm}
    if request.method=='POST':
        nurseUserForm = forms.NurseUserForm(request.POST)
        nurseCustomForm = forms.NurseCustomForm(request.POST,request.FILES)
        if nurseUserForm.is_valid() and nurseCustomForm.is_valid():
            user = nurseUserForm.save()
            print("nurseUserForm saved")
            user.set_password(user.password)
            print("User Password Set")
            nurse = nurseCustomForm.save(commit=False)
            print("nurseUserForm saved not commited")
            user.save()
            nurse.user = user
            nurse = nurse.save()
            nurseGroup = Group.objects.get_or_create(name='NURSE')
            nurseGroup[0].user_set.add(user)
        return HttpResponseRedirect('nurseLogIn')
    return render(request,'nurses/nurseSignUp.html', context=nurseForms)

@login_required(login_url='nurseLogIn')
@user_passes_test(is_nurse)
def nurseDashboardView(request):
    reportcount = models.Report.objects.all().count()
    nurseId = request.user.nurses.id
    nurseName = request.user.nurses.name

    # appointmentcount=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).count()
    # patientdischarged=models.PatientDischargeDetails.objects.all().distinct().filter(assignedDoctorName=request.user.first_name).count()

    # #for  table in doctor dashboard
    # appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).order_by('-id')
    # patientid=[]
    # for a in appointments:
    #     patientid.append(a.patientId)
    # patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid).order_by('-id')
    # appointments=zip(appointments,patients)
    dashboardInfo={
    'reportCount':reportcount,
    'nurseId':nurseId,
    'nurseName':nurseName,
    }
    return render(request,'nurses/nurseDashboard.html',context=dashboardInfo)


