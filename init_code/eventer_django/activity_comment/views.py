from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import Activity_comment_serializer, Comment_activity_list_serializer
from .models import Activity_comment, Like_activity_comment, Comment_activity_list, Comment_activity_list

@csrf_exempt
def activity_comment(request, activity_id):
    
    try:
        activity = Activity_comment.objects.get(activity_id = activity_id)
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_comment_serializer(activity)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)