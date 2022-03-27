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
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)

@csrf_exempt
def activity_tag(request, tag):
    
    try:
        activities = Activity.objects.filter(tag__icontains = tag)
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_serializer(activities, many = True)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)
    
@csrf_exempt
def activity_title(request, title):
    
    try:
        activities = Activity.objects.filter(title__icontains = title)
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_serializer(activities, many = True)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)
    
@csrf_exempt
def activity_order_part_max(request, num):
    
    if (num <= 0):
        return HttpResponse(status = 404)
    
    try:
        activities = Activity.objects.order_by('-part_max_num')[:num]
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_serializer(activities, many = True)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)
    
@csrf_exempt
def activity_order_score(request, num):
    
    if (num <= 0):
        return HttpResponse(status = 404)
    
    try:
        activities = Activity.objects.filter(is_outdate = True).order_by('-score_avg')[:num]
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_serializer(activities, many = True)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)
    
@csrf_exempt
def activity_order_start_date(request, num):
    
    if (num <= 0):
        return HttpResponse(status = 404)
    
    try:
        activities = Activity.objects.order_by('-start_time')[:num]
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_serializer(activities, many = True)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)
    
    
@csrf_exempt
def activity_order_create_date(request, num):
    
    if (num <= 0):
        return HttpResponse(status = 404)
    
    try:
        activities = Activity.objects.order_by('-create_time')[:num]
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_serializer(activities, many = True)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)