from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Patient, Appointment

from datetime import datetime
import dateutil.parser

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

    try:
        valid_birth_date = datetime.strptime(request.POST['date_of_birth'], '%Y-%m-%d')
        valid_due_time = dateutil.parser.parse(request.POST['dueTime'])
    except ValueError:
        # handle this
        pass

    p = Patient(first_name=first_name, last_name=last_name, birth_date=valid_birth_date)
    p.phone_number = phone
    p.email = email
    p.address = address
    p.due_date = valid_due_time
    id_photo = photoFile
    p.save()

    return JsonResponse(response)

