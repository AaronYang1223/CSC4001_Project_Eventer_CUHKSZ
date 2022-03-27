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
    
