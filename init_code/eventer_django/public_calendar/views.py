from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from .serializers import Public_calendar_serializer
from .models import Public_calendar
import datetime
from activity.models import Activity
from user.models import User
from user.serializers import User_profile_serializer
from activity.serializers import Activity_serializer

def calendar(request, start_date, end_date):
    
    _start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    _end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    try:
        activities = Public_calendar.objects.filter(activity_start_date__gte = _start_date, activity_end_date__lte = _end_date)
        # activities = Public_calendar.objects.all()
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Public_calendar_serializer(activities, many = True)
        return JsonResponse(serializer.data, safe = False)
    
    
def calendar_add(activity_id, user_id) -> bool:
    
    activity = Activity.objects.get(id = activity_id)
    data = {
        'activity_id': activity_id,
        'user_id': user_id,
        'activity_title': activity.title,
        'activity_start_date': activity.start_time,
        'activity_end_date': activity.end_time
    }
    
    serializer = Public_calendar_serializer(data = data)
    if (serializer.is_valid()):
        serializer.save()
        return True
    return False

@csrf_exempt
def calendar_public_all(request):
    
    try:
        calendars = Public_calendar.objects.filter(is_delete = False)
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Public_calendar_serializer(calendars, many = True)
        temp_data = calendar_public_add_info(serializer)
        return JsonResponse(temp_data, safe = False)
    
def calendar_public_add_info(calendars):
    temp_data = calendars.data
    for i in range(len(temp_data)):
        activity = Activity.objects.get(id = temp_data[i]['activity_id'])
        temp_activity_serializer = Activity_serializer(activity)
        user = User.objects.get(id = temp_activity_serializer.data['organizer_id'])
        temp_user_serializer = User_profile_serializer(user)
        temp_data[i]['is_organization'] = temp_user_serializer.data['is_organization']
        temp_data[i]['nick_name'] = temp_user_serializer.data['nick_name']
        temp_data[i]['picture'] = temp_user_serializer.data['picture']
        temp_data[i]['is_public'] = temp_activity_serializer.data['is_public']
    return temp_data