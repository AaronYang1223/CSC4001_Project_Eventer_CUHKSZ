from distutils.command.upload import upload
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

import public_calendar
import private_calendar
from .serializers import Activity_serializer
from .models import Activity
import datetime
from django.core.files.storage import FileSystemStorage

from activity import serializers

# TODO: Change post function for uploading a cover page when create an activity

@csrf_exempt
def activity_list(request):
    if request.method == 'GET':
        activities = Activity.objects.filter(is_delete = False, is_outdate = False, is_private = False)
        serializer = Activity_serializer(activities, many=True)
        return JsonResponse(serializer.data, safe = False)

@csrf_exempt
def activity_create(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Activity_serializer(data = data)
        if serializer.is_valid():
            serializer.save()
            
            # add public calendar
            if (serializer.data['is_public']):
                res = public_calendar.views.calendar_add(serializer.data['id'], serializer.data['organizer_id'])
                if (not res):
                    return JsonResponse('Can not add to public calendar, activity_id: {}, organizer_id: {}'.format(serializer.data['id'], serializer.data['organizer_id']), status = 400)
            elif (serializer.data['is_private']):
                # the organizer is the owner of this activity
                res = private_calendar.views.calendar_add(serializer.data['id'], serializer.data['organizer_id'])
                if (not res):
                    return JsonResponse('Can not delete from public calendar, activity_id: {}, organizer_id: {}'.format(serializer.data['id'], serializer.data['organizer_id']), status = 400)
            
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def activity_pk(request, pk):
    
    try:
        activity = Activity.objects.get(pk = pk, is_delete = False)
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_serializer(activity)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)

# for put method, need to include all fields without default values
@csrf_exempt
def activity_change_pk(request, pk):
    try:
        activity = Activity.objects.get(pk = pk)
    except:
        return HttpResponse(status = 404)
    
    # do not limit is_organization
    if (request.method == 'PUT'):
        data = JSONParser().parse(request)
        
        serializers = Activity_serializer(activity, data = data)
        if (serializers.is_valid()):
            serializers.save()
            return JsonResponse(serializers.data, status = 201)
        return JsonResponse(serializers.errors, status = 400)

# TODO: complete this function
@csrf_exempt
def activity_upload_cover(request, pk):
    try:
        activity = Activity.objects.get(pk = pk)
    except:
        return JsonResponse(status = 404)
    
    if (request.method == 'POST' and request.FILES):
        activity.cover_page.save(request.FILES['cover_page'].name, request.FILES['cover_page'])
        activity.cover_page.close()
        
        serializers = Activity_serializer(activity)
        return JsonResponse(serializers.data, status = 200)
    else:
        return JsonResponse(status = 404)

@csrf_exempt
def activity_tag(request, tag):
    
    try:
        activities = Activity.objects.filter(tag__icontains = tag, is_delete = False, is_private = False)
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_serializer(activities, many = True)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)
    
@csrf_exempt
def activity_title(request, title):
    
    try:
        activities = Activity.objects.filter(title__icontains = title, is_delete = False, is_private = False)
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
        activities = Activity.objects.filter(is_delete = False, is_private = False).order_by('-part_max_num')[:num]
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
        activities = Activity.objects.filter(is_outdate = True, is_delete = False, is_private = False).order_by('-score_avg')[:num]
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
        activities = Activity.objects.filter(is_delete = False, is_private = False).order_by('-start_time')[:num]
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
        activities = Activity.objects.filter(is_delete = False, is_private = False).order_by('-create_time')[:num]
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
        activities = Activity.objects.filter(is_delete = False, is_private = False).order_by('-comment_number')[:num]
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_serializer(activities, many = True)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)