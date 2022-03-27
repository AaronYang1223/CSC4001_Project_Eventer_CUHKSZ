from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import Activity_serializer
from .models import Activity
import datetime

@csrf_exempt
def activity_pk(request, pk):
    
    try:
        activity = Activity.objects.get(pk = pk)
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_serializer(activity)
        return JsonResponse(serializer.data, safe = False)

@csrf_exempt
def activity_tag(request, tag):
    
    try:
        activities = Activity.objects.filter(tag = tag)
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_serializer(activities, many = True)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)