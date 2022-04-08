from asyncio.windows_events import NULL
import code
from http.client import HTTPResponse
import imp
import re
import json
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import User_profile_serializer
from .models import Email_check_new, User

from .forms import RegisterForm
from django.contrib.auth.hashers import make_password
from utils.email_util import send_email, send_check_organization_email

@csrf_exempt
def profile(request, pk):
    
    try:
        user = User.objects.get(pk = pk)
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = User_profile_serializer(user)
        return JsonResponse(serializer.data, safe = False)

# for put method, need to include all fields without default values
@csrf_exempt
def profile_change(request, pk):
    
    try:
        user = User.objects.get(pk = pk)
    except:
        return HttpResponse(status = 404)
    
    # do not limit is_organization
    if (request.method == 'PUT'):
        json_data = request.body.decode("utf-8")
        data = json.loads(json_data)
        
        email = data.get('email')
        code = data.get('code')
        email_code = Email_check_new.objects.filter(email = email, email_type = 'retrieve').first()
        if(email_code.__getattribute__('code') == code):
            user_data = JSONParser().parse(request)
            serializers = User_profile_serializer(user, data = user_data)
            if (serializers.is_valid()):
                serializers.save()
                return JsonResponse(serializers.data, status = 201)
        return JsonResponse(serializers.errors, status = 400)

@csrf_exempt
def profile_add(request):
    if (request.method == 'POST'):
        #data = JSONParser().parse(request)
        json_data = request.body.decode("utf-8")
        data = json.loads(json_data)
        #if (data['is_orginazation'] == True):
        #    check_organization(data)
        email = data.get('email')
        code = data.get('code')
        email_code = Email_check_new.objects.filter(email = email, email_type = 'register').order_by('-send_time')[:1]
        if email_code != []:
            print('exist')
        if(email_code.values()[0]['code']):
            user_data = JSONParser().parse(request)
            if(user_data==NULL):
                print("null")
            else:
                print(user_data)
            serializers = User_profile_serializer(data = user_data)
            if (serializers.is_valid()):
                serializers.save()
                return JsonResponse({
                    'code' : '002',
                    'message':'create userprofile success'
                    })
        return JsonResponse({
            'code' : '102',
            'message':'create userprofile failed'
        })

def check_organization(email):
    send_check_organization_email(email)
    
@csrf_exempt
def email_verification(request):
    json_data = request.body.decode("utf-8")
    #print(json_data)
    data = json.loads(json_data)
    #print(data)
    if request.method == "POST":
        email =  data.get('email')
        email_type = data.get('email_type')
        user_obj = User.objects.filter(email=email).first()
        if user_obj:
            if email_type == 'register':
                return JsonResponse({
                    'email': str(email),
                    'code':'101', # 101 === email exist
                    'message': 'error: This email is already registered' 
                })
            if email_type == 'retrieve':
                email_status = send_email(email, email_type = 'retrieve')
                return JsonResponse({
                    'email': str(email),
                    'code':'003', # 003 === email exist
                    'message': 'email eixst' 
                })
        else:
            if email_type == 'register':
                email_status = send_email(email, send_type = 'register')
                if(data.get('is_organization') == "true"):
                    check_organization(email)
                return JsonResponse({
                    'email': str(email),
                    'code':'001', # 001 === email valid for registration
                    'message': 'email valid for registration' 
                })
            if email_type == 'retrieve':
                return JsonResponse({
                    'email': str(email),
                    'code':'103', #103 == email doesn't get registered
                    'message': 'user doesn\'t exist' 
                })
    #code = data['code']
    #email = data['email']
    #type = data['email_type']
    #user_obj = Email_check_new.objects.filter(email=email, code = code).first()
    #if user_obj:    
    #    if request.method=="POST":
    #        #新建用户
    #        pass
    #    if request.method=="PUT":
    #        #更改密码
    #        user_old = User.objects.filter(email=email).first()
    #else:
    #    return HttpResponse(status=404)  # return need modification
        
