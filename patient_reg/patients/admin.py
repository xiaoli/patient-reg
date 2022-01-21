from django.contrib import admin

from .models import *

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email')
    ordering = ['-created_at', '-updated_at']

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('get_patient_name', 'due_date',) 

    def get_patient_name(self, obj):
        return ('%s %s' % (obj.patient.first_name, obj.patient.last_name))

    get_patient_name.admin_order_field  = 'patient'  #Allows column order sorting
    get_patient_name.short_description = 'Patient Name'  #Renames column head
    
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_card_number', 'phone_number', 'business_address')
    ordering = ['-created_at', '-updated_at']

admin.site.register(Patient, PatientAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Appointment, AppointmentAdmin)