from django.contrib import admin

from .models import *

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email')
    ordering = ['-created_at', '-updated_at']

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('due_date',) 

admin.site.register(Patient, PatientAdmin)
admin.site.register(Appointment, AppointmentAdmin)