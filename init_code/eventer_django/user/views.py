from http.client import HTTPResponse
import json
import re
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from activity import serializers
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
    
@csrf_exempt
def profile_upload_picture(request, pk):
    try:
        user = User.objects.get(pk = pk)
    except:
        return JsonResponse(status = 404)
    
    print(request.FILES)
    if (request.method == 'POST' and request.FILES):
        user.picture.save(request.FILES['picture'].name, request.FILES['picture'])
        user.picture.close()
        
        serializers = User_profile_serializer(user)
        return JsonResponse(serializers.data, status = 200)
    else:
        return JsonResponse(status = 404)

# for put method, need to include all fields without default values
@csrf_exempt
def profile_change(request):
    
    # do not limit is_organization
    if (request.method == 'PUT'):
        json_data = request.body.decode("utf-8")
        data = json.loads(json_data)
        
        email = data.get('email')
        oldpassword = data.get('oldpassword')
        newpassword = data.get('newpassword')
        try:
            User.objects.filter(email=email,password=oldpassword).update(password=newpassword)
            return JsonResponse({
                'code' : '005',
                'message':'update password success'
            })
        except:
            return JsonResponse({
                'code' : '105',
                'message':'update password failed'
            })


@csrf_exempt
def profile_retrieve(request):
    if (request.method == 'PUT'):
        json_data = request.body.decode("utf-8")
        data = json.loads(json_data)
        email = data.get('email')
        code = data.get('code')
        newpassword = data.get('newpassword')
        email_code = Email_check_new.objects.filter(email = email, email_type = 'retrieve').order_by('-send_time')[:1]

        if(email_code.values()[0]['code']==code):
            User.objects.filter(email = email).update(password = newpassword)
            return JsonResponse({
                'code' : '004',
                'message':'password updated'
            })
        return JsonResponse({
            'code' : '104',
            'message':'update password failed'
        })

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
        password = data.get('password')
        email_code = Email_check_new.objects.filter(email = email, email_type = 'register').order_by('-send_time')[:1]
        if email_code != []:
            print('exist')
        if(email_code.values()[0]['code']==code):
            if(data.get('is_organization') == "true"):
                    check_organization(email)
            user_data = JSONParser().parse(request)

            serializers = User_profile_serializer(data = user_data)
            if (serializers.is_valid()):
                serializers.save()
                User.objects.filter(email=email).update(password=password)
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
                email_status = send_email(email, send_type = 'retrieve')
                return JsonResponse({
                    'email': str(email),
                    'code':'003', # 003 === email exist
                    'message': 'email eixst' 
                })
        else:
            if email_type == 'register':
                email_status = send_email(email, send_type = 'register')
                
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
@csrf_exempt
def verify_password(request):
    if(request.method == "GET"):
        email = request.GET.get("email")
        password = request.GET.get("password")
        user = User.objects.filter(email=email,password=password)
        if(user.exists()):
            user_data = User.objects.get(email=email,password=password)
            serializer = User_profile_serializer(user_data)
            return JsonResponse(serializer.data)
        print("wrong")
        return JsonResponse({
            'status':'error',
            'message':'login success',
            'id':''
        })

        
