from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=30, null=True, db_index=True)
    email = models.EmailField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    id_photo = models.ImageField(null=True, blank=True)
    due_date = models.DateTimeField(null=True)
    
    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)
    # A timestamp reprensenting when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return ('%s - %s %s' % self.pk, self.first_name, self.last_name)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    
class Person(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    id_card_number = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30, null=True, db_index=True)
    business_address = models.CharField(max_length=200, null=True)
    is_local_people = models.CharField(max_length=20, null=True)
    local_address = models.CharField(max_length=200, null=True)
    anti_virus = models.CharField(max_length=20, null=True)
    health_photo = models.ImageField(null=True, blank=True)
    travel_photo = models.ImageField(null=True, blank=True)
    
    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)
    # A timestamp reprensenting when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return ('%s - %s %s' % self.pk, self.name, self.id_card_number)