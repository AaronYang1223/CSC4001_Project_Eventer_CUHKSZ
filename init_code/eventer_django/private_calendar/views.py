from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse

from .serializers import Private_calendar_serializer
from .models import Private_calendar
from activity.models import Activity
import datetime

def calendar(request, user, start_date, end_date):
    
    _start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    _end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    try:
        activities = Private_calendar.objects.filter(user_id = user, activity_start_date__gte = _start_date, activity_end_date__lte = _end_date)
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Private_calendar_serializer(activities, many = True)
        return JsonResponse(serializer.data, safe = False)

def calendar_get_user(request, user):
    
    try:
        activities = Private_calendar.objects.filter(user_id = user)
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Private_calendar_serializer(activities, many = True)
        return JsonResponse(serializer.data, safe = False)
    
def calendar_add(activity_id, user_id) -> bool:
    
    # user_id is owner of this private calendar
    activity = Activity.objects.get(id = activity_id)
    data = {
        'activity_id': activity_id,
        'user_id': user_id,
        'activity_title': activity.title,
        'activity_start_date': activity.start_time,
        'activity_end_date': activity.end_time
    }
    
    serializer = Private_calendar_serializer(data = data)
    if (serializer.is_valid()):
        serializer.save()
        return True
    return False