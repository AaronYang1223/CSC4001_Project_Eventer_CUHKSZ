from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import Activity_serializer
from .models import Activity
import datetime

@api_view(['GET'])
def activity_list(request):
    if request.method == 'GET':
        activities = Activity.objects.all()
        serializer = Activity_serializer(activities, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def create_activity(request):
    if request.method == 'POST':
        serializer = Activity_serializer(data==request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def activity_pk(request, pk):
    
    try:
        activity = Activity.objects.get(pk = pk, is_delete = False)
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_serializer(activity)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)

@csrf_exempt
def activity_tag(request, tag):
    
    try:
        activities = Activity.objects.filter(tag__icontains = tag, is_delete = False)
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_serializer(activities, many = True)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)
    
@csrf_exempt
def activity_title(request, title):
    
    try:
        activities = Activity.objects.filter(title__icontains = title, is_delete = False)
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
        activities = Activity.objects.filter(is_delete = False).order_by('-part_max_num')[:num]
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
        activities = Activity.objects.filter(is_outdate = True, is_delete = False).order_by('-score_avg')[:num]
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
        activities = Activity.objects.filter(is_delete = False).order_by('-start_time')[:num]
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
        activities = Activity.objects.filter(is_delete = False).order_by('-create_time')[:num]
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_serializer(activities, many = True)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)
    
    
@csrf_exempt
def activity_order_comment_number(request, num):
    
    if (num <= 0):
        return HttpResponse(status = 404)
    
    try:
        activities = Activity.objects.filter(is_delete = False).order_by('-comment_number')[:num]
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_serializer(activities, many = True)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)