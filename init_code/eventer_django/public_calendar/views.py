from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from .serializers import Public_calendar_serializer
from .models import Public_calendar
import datetime


@csrf_exempt
def create_calendar_event(request):
    if(request.method=='POST'):
        serializer=Public_calendar_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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