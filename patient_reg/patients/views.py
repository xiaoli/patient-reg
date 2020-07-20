from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

from datetime import datetime
import dateutil.parser

from .models import Patient, Appointment

@csrf_exempt
def register(request):
    response = {'status':'ok'}
    
    # recieving form data
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    date_of_birth = request.POST.get('date_of_birth')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    dueTime = request.POST.get('dueTime')
    photoFile = request.FILES['file']

    # handing date & time data
    try:
        valid_birth_date = datetime.strptime(request.POST['date_of_birth'], '%Y-%m-%d')
        valid_due_time = dateutil.parser.parse(request.POST['dueTime'])
    except ValueError:
        # handle this
        pass

    # handing photo ID
    photo_file = photoFile
    #fs = FileSystemStorage()
    #filename = fs.save(id_photo.name, photo_id_file)
    #uploaded_file_url = fs.url(filename)

    # saving Patient object
    p = Patient(first_name=first_name, last_name=last_name, birth_date=valid_birth_date)
    p.phone_number = phone
    p.email = email
    p.address = address
    p.due_date = valid_due_time
    p.id_photo = photo_file
    p.save()

    return JsonResponse(response)