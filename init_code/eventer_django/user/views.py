from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import User_profile_serializer
from .models import User

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
        data = JSONParser().parse(request)
        
        # may need change status code
        if ('is_orginazation' in data and data['is_orginazation'] != user.is_orginazation):
            return HttpResponse(status = 400)

        if ('email' in data and data['email'] != user.email):
            return HttpResponse(status = 400)
        
            
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
        serializers = User_profile_serializer(data = data)
        if (serializers.is_valid()):
            serializers.save()
            return JsonResponse(serializers.data, status = 201)
        return JsonResponse(serializers.errors, status = 400)

def check_organization(request):
    pass