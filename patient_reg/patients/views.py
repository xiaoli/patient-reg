from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

from datetime import datetime
import dateutil.parser

from .models import Patient, Appointment, Person

@csrf_exempt
def register(request):
    response = {'status':'ok'}
    
    # recieving form data
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    id_card_number = request.POST.get('id_card_number')
    phone = request.POST.get('phone')
    business_address = request.POST.get('business_address')
    is_local_people = request.POST.get('is_local_people')
    local_address = request.POST.get('local_address')
    anti_virus = request.POST.get('anti_virus')
    file1 = request.FILES['file1']
    file2 = request.FILES['file2']

    # saving Patient object
    p = Person(name=name, gender=gender, id_card_number=id_card_number, 
              phone_number=phone, business_address=business_address,
              is_local_people=is_local_people, local_address=local_address,
              anti_virus=anti_virus
              )
    p.health_photo = file1
    p.travel_photo = file2
    p.save()

    return JsonResponse(response)