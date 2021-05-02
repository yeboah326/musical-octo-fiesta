from django.contrib import admin
from .models import Doctor, Hospital, Nurse, Report

# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name','hospital']

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ['name','hospital']

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['name','hospital','doctor','nurse']

