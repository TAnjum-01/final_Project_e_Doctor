"""pythonProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
import django.contrib.auth.views as auth_views
import e_Doctor.views
import doctor.views as doctor_views
import patient.views as patient_views
import prescription.views as prescription_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', e_Doctor.views.homepage, name='homepage'),
    path('register/', e_Doctor.views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('about_us/', e_Doctor.views.about_us, name='about_us'),
    path('doctors_profile/', e_Doctor.views.doctors_profile, name='doctors_profile'),
    path('patients_profile/', e_Doctor.views.patients_profile, name='patients_profile'),
    path('contact_us/', e_Doctor.views.contact_us, name='contact_us'),
    path('terms_&_conditions/', e_Doctor.views.terms_conditions, name='terms_&_conditions'),
    path('available_specialists', e_Doctor.views.available_specialists, name='available_specialists'),
    path('meet_patient/', e_Doctor.views.meet_patient, name='meet_patient'),
    path('patients_prev_rec/', e_Doctor.views.patients_prev_rec, name='patients_prev_rec'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('doctors_info/', doctor_views.doctor, name='doctors_info'),
    path('patients_info/', patient_views.patient, name='patients_info'),
    path('prescription/', prescription_views.prescription, name='prescription'),


]
