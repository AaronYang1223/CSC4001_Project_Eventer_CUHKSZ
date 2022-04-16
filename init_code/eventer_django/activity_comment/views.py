from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import Activity_comment_serializer, Like_activity_comment_serializer
from .models import Activity_comment, Like_activity_comment
from rest_framework import status
from activity.models import Activity

@csrf_exempt
def activity_comment_create(request):
    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = Activity_comment_serializer(data = data)
        
        if serializer.is_valid():
            serializer.save()
            
            # update activity comment num
            activity = Activity.objects.get(id = serializer.data['activity_id'])
            activity.comment_number += 1
            activity.save()
            
            return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, status = status.HTTP_201_CREATED)
        return JsonResponse({'status':'failed'})


@csrf_exempt
def activity_comment(request, activity_id):
    try:
        comment = Activity_comment.objects.filter(activity_id = activity_id, is_delete = False).order_by('-create_time')
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_comment_serializer(comment, many = True)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)
    
    
@csrf_exempt
def activity_comment_like(request, activity_id):
    
    try:
        comment = Activity_comment.objects.filter(activity_id = activity_id, is_delete = False).order_by('-like_num')
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_comment_serializer(comment, many = True)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)
    
@csrf_exempt
def activity_comment_like_add(request):
    
    if (request.method == 'POST'):
        data = JSONParser().parse(request)
        serializers = Like_activity_comment_serializer(data = data)
        
        if (serializers.is_valid()):
            serializers.save()
            if (Activity_comment.objects.filter(comment_id = data['comment_id'], user_id = data['user_id']).values()):
                return HttpResponse(status = 404)
            activity_comment = Activity_comment.objects.get(id = data['comment_id'])
            if (serializers.data['is_like'] == '1'):
                activity_comment.like_num += 1
            elif (serializers.data['is_like'] == '0'):
                activity_comment.dislike_num += 1
            
            activity_comment.save()
            
            return JsonResponse(serializers.data, status = 201, safe = False)
        return JsonResponse(serializers.errors, status = 400)
    elif (request.method == 'PUT'):
        data = JSONParser().parse(request)
        try:
            like_activity = Like_activity_comment.objects.get(comment_id = data['comment_id'], user_id = data['user_id'])
        except:
            return HttpResponse(status = 404)
        
        # update like number and dislike number
        activity_comment = Activity_comment.objects.get(id = data['comment_id'])
        if (data['is_like'] == '1' and like_activity.is_like == '2'):
            activity_comment.like_num += 1
        elif (data['is_like'] == '1' and like_activity.is_like == '0'):
            activity_comment.like_num += 1
            activity_comment.dislike_num -= 1
        elif (data['is_like'] == '0' and like_activity.is_like == '2'):
            activity_comment.dislike_num += 1
        elif (data['is_like'] == '0' and like_activity.is_like == '1'):
            activity_comment.like_num -= 1
            activity_comment.dislike_num += 1
        elif (data['is_like'] == '2' and like_activity.is_like == '0'):
            activity_comment.dislike_num -= 1
        elif (data['is_like'] == '2' and like_activity.is_like == '1'):
            activity_comment.like_num -= 1
        
        like_activity.is_like = data['is_like']
        like_activity.save()
        
        activity_comment.save()

        return JsonResponse('Change like status to {}.'.format(like_activity.is_like), status = 201, safe = False)
    
# if do not exit, add a default
@csrf_exempt
def activity_comment_like_get(request, comment, user):
    
    try:
        like_activity = Like_activity_comment.objects.get(comment_id = comment, user_id = user)
    except:
        data = {
            'comment_id': comment,
            'user_id': user,
            'is_like': "2"
        }
        serializers = Like_activity_comment_serializer(data = data)
    
        if (serializers.is_valid()):
            serializers.save()
            
            return JsonResponse(serializers.data, status = 201, safe = False)
        return JsonResponse(serializers.errors, status = 400)
    
    if (request.method == 'GET'):
        serializer = Like_activity_comment_serializer(like_activity)
        return JsonResponse(serializer.data, safe = False)