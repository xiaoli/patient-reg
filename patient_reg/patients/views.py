from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

from datetime import datetime
import dateutil.parser

from .models import Patient, Appointment, Person

import csv

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

    # saving Patient object
    p = Person(name=name, gender=gender, id_card_number=id_card_number, 
              phone_number=phone, business_address=business_address,
              is_local_people=is_local_people, local_address=local_address,
              anti_virus=anti_virus
              )
    if request.FILES:
        file1 = request.FILES['file1']
        file2 = request.FILES['file2']
        p.health_photo = file1
        p.travel_photo = file2
    p.save()

    return JsonResponse(response)
    
def download(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['姓名', '性别', '身份证号码', '地址', '联系电话', '是否常住人口', '居住地址', '是否接种疫苗', '健康码', '行程码'])
    
    p_list = Person.objects.all()
    for p in p_list:  
        writer.writerow([p.name, p.gender, p.id_card_number, p.business_address, p.phone_number,
                         p.is_local_people, p.local_address, p.anti_virus, p.health_photo.url if p.health_photo else  "", p.travel_photo.url if p.travel_photo else ""])

    return response
