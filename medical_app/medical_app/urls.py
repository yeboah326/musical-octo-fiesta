"""medical_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# TODO: Work on the naming of the views
from medical_app_backend import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Generic URLs
urlpatterns += [
    path('afterLogIn', views.afterLogInView,name="afterLogIn"),
    path('logOut', LogoutView.as_view(template_name="main/home.html"),name="logOut")
]

# Doctor URLs
urlpatterns += [
    path('doctorSignUp', views.doctorSignUpView,name='doctorSignUp'),
    path('doctorLogIn', LoginView.as_view(template_name='doctors/doctorLogIn.html'),name="doctorLogIn"),
    path('doctorDashboard', views.doctorDashboardView,name='doctorDashboard'),
    path('doctorDashboardPendingReports', views.doctorDashboardPendingReportsView, name="doctorDashboardPendingReports"),
    path('doctorDashboardCompletedReports', views.doctorDashboardCompletedReportsView, name="doctorDashboardCompletedReports"),
]

# Nurse URLs
urlpatterns += [
    path('nurseSignUp', views.nurseSignUpView,name='nurseSignUp'),
    path('nurseLogIn', LoginView.as_view(template_name='nurses/nurseLogIn.html'),name="nurseLogIn"),
    path('nurseDashboard', views.nurseDashboardView,name='nurseDashboard'),
    path('nurseDashboardPendingReports', views.nurseDashboardPendingReportsView, name='nurseDashboardPendingReports'),
    path('nurseDashboardCompletedReports', views.nurseDashboardCompletedReportsView, name='nurseDashboardCompletedReports')
]
