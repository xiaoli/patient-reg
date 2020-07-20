from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Patient, Appointment

from datetime import datetime

@csrf_exempt
def register(request):
    response = {'status':'ok'}
    
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    date_of_birth = request.POST.get('date_of_birth')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    dueTime = request.POST.get('dueTime')
    photoFile = request.FILES['file']

    print(first_name, last_name, photoFile, date_of_birth, dueTime)

    try:
        valid_birth_date = datetime.strptime(request.POST['date_of_birth'], '%Y-%m-%d')
        #valid_due_time = datetime.strptime(request.POST['dueTime'], '%Y-%m-%dT%H%M')
        #print(valid_birth_date, valid_due_time)
    except ValueError:
        # handle this
        print("======")
    
    print("======999======")
    print(valid_birth_date)
    p = Patient(first_name=first_name, last_name=last_name, birth_date=valid_birth_date)
    p.phone_number = phone
    p.email = email
    p.address = address
    id_photo = photoFile
    print(p.birth_date)
    p.save()

    return JsonResponse(response)

