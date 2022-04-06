import code
from http.client import HTTPResponse
import imp
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from activity import serializers
from .serializers import User_profile_serializer
from .models import Email_check_new, User

from .forms import RegisterForm
from django.contrib.auth.hashers import make_password
from utils.email_util import send_email

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
def profile_change(request, pk):
    
    try:
        user = User.objects.get(pk = pk)
    except:
        return JsonResponse(status = 404)
    
    # do not limit is_organization
    if (request.method == 'PUT'):
        data = JSONParser().parse(request)
        email = data['email']
        email_status = send_email(email)
        if email_status:
            return  JsonResponse(status=200)  # return need modification
        else:
            return  JsonResponse(status=404)  # return need modification
        # # may need change status code
        # if ('is_orginazation' in data and data['is_orginazation'] != user.is_orginazation):
        #     return HttpResponse(status = 404)

        # if ('email' in data and data['email'] != user.email):
        #     return HttpResponse(status = 404)
        
        serializers = User_profile_serializer(user, data = data)
        if (serializers.is_valid()):
            serializers.save()
            return JsonResponse(serializers.data, status = 201)
        return JsonResponse(serializers.errors, status = 400)

@csrf_exempt
def profile_add(request):

    if (request.method == 'POST'):
        data = JSONParser().parse(request)
        if (data['is_orginazation'] == True):
            check_organization(data)
        email = data['email']
        user_obj = User.objects.filter(email=email).first()
        if user_obj:    
            return HttpResponse(status=404) # return need modification
        else:
            email_status = send_email(email)
            if email_status:
                return  HttpResponse(status=200)  # return need modification
            else:
                return  HttpResponse(status=404)  # return need modification
        serializers = User_profile_serializer(data = data)
        if (serializers.is_valid()):
            serializers.save()
            return JsonResponse(serializers.data, status = 201)
        return JsonResponse(serializers.errors, status = 400)

def check_organization(request):
    pass


@csrf_exempt
def email_verification(request):
    data = JSONParser().parse(request)
    code = data['code']
    email = data['email']
    type = data['email_type']
    user_obj = Email_check_new.objects.filter(email=email, code = code).first()
    if user_obj:    
        if request.method=="POST":
            #新建用户
            pass
        if request.method=="PUT":
            #更改密码
            user_old = User.objects.filter(email=email).first()
    else:
        return HttpResponse(status=404)  # return need modification
        

