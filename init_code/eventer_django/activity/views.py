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
import user
from .serializers import Activity_serializer
from .models import Activity
import datetime

from activity import serializers
from user.models import User
from user.serializers import User_profile_serializer
from activity_comment.models import Activity_comment, Like_activity_comment
from activity_comment.serializers import Activity_comment_serializer
from score_activity.models import Score, Participant_Activity
from score_activity.serializers import Score_activity_serializer


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
        print(serializer)
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
            
            return JsonResponse(serializer.data, status=201)
        return JsonResponse({'code':'101'})

@csrf_exempt
def activity_update_coverpage(request, pk):
    try:
        activity = Activity.objects.get(pk = pk)
    except:
        return JsonResponse(status = 404)
    
    print(request.FILES)
    if (request.method == 'PUT' and request.FILES):
        activity.cover_page.save(request.FILES['cover_page'].name, request.FILES['cover_page'])
        activity.cover_page.close()
        
        serializers = Activity_serializer(activity)
        return JsonResponse(serializers.data, status = 200)
    else:
        return JsonResponse(status = 404)

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
        activities = Activity.objects.filter(is_delete = False, is_private = False, is_outdate = False).order_by('-create_time')[:num]
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_serializer(activities, many = True)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)
    
@csrf_exempt
def activity_order_create_date_all(request):
    
    try:
        activities = Activity.objects.filter(is_delete = False, is_private = False, is_outdate = False).order_by('-create_time')
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_serializer(activities, many = True)
        temp_data = activity_add_user_info(serializer)
        return JsonResponse(temp_data, json_dumps_params = {'ensure_ascii': False}, safe = False)
    
    
@csrf_exempt
def activity_order_comment_number(request, num):
    
    if (num <= 0):
        return HttpResponse(status = 404)
    
    try:
        activities = Activity.objects.filter(is_delete = False, is_private = False, is_outdate = False).order_by('-comment_number')[:num]
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_serializer(activities, many = True)
        temp_data = activity_add_user_info(serializer)
        return JsonResponse(temp_data, json_dumps_params = {'ensure_ascii': False}, safe = False)
    
@csrf_exempt
def activity_order_comment_number_all(request):
    
    try:
        activities = Activity.objects.filter(is_delete = False, is_private = False, is_outdate = False).order_by('-comment_number')
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_serializer(activities, many = True)
        temp_data = activity_add_user_info(serializer)
        return JsonResponse(temp_data, json_dumps_params = {'ensure_ascii': False}, safe = False)
    
def activity_add_user_info(serializer):
    temp_data = serializer.data
    for i in range(len(temp_data)):
        user = User.objects.get(pk = temp_data[i]['organizer_id'])
        temp_user_serializer = User_profile_serializer(user)
        # is_organization, nick_name, picture
        temp_data[i]['is_organization'] = temp_user_serializer.data['is_organization']
        temp_data[i]['nick_name'] = temp_user_serializer.data['nick_name']
        temp_data[i]['picture'] = temp_user_serializer.data['picture']
        if ((not temp_data[i]['is_outdate']) and (datetime.datetime.strptime(temp_data[i]['end_time'], "%Y-%m-%dT%H:%M:%S") < datetime.datetime.now())):
            temp_data[i]['is_outdate'] = True
            activity = Activity.objects.get(pk = temp_data[i]['id'])
            activity.is_outdate = True
            activity.save()
    return temp_data

@csrf_exempt
def activity_user_order_comment_num(request, user_id):
    
    try:
        activities = Activity.objects.filter(organizer_id = user_id, is_delete = False).order_by('-comment_number')
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_serializer(activities, many = True)
        temp_data = activity_add_user_info(serializer)
        return JsonResponse(temp_data, json_dumps_params = {'ensure_ascii': False}, safe = False)

@csrf_exempt
def activity_user_order_create_time(request, user_id):
    
    try:
        activities = Activity.objects.filter(organizer_id = user_id, is_delete = False).order_by('-create_time')
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_serializer(activities, many = True)
        temp_data = activity_add_user_info(serializer)
        return JsonResponse(temp_data, json_dumps_params = {'ensure_ascii': False}, safe = False)

@csrf_exempt
def activity_user(request, user_id):
    
    try:
        activities = Activity.objects.filter(organizer_id = user_id, is_delete = False)
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Activity_serializer(activities, many = True)
        temp_data = activity_add_user_info(serializer)
        return JsonResponse(temp_data, json_dumps_params = {'ensure_ascii': False}, safe = False)


@csrf_exempt
def activity_comment(request, activity_id):
    
    try:
        activity = Activity.objects.get(pk = activity_id)
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        activity_serializer = Activity_serializer(activity)
        temp_data = activity_add_comment_info(activity_serializer)
        return JsonResponse(temp_data, json_dumps_params = {'ensure_ascii': False}, safe = False)

    
    # if (request.method == 'POST'):
    #     data = JSONParser().parse(request)
    #     serializer = Comment_serializer(data = data)
    #     if (serializer.is_valid()):
    #         serializer.save()
    #         return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, status = 201)
    #     return JsonResponse(serializer.errors, status = 400)
    
@csrf_exempt
def activity_add_comment_info(serializer):
    temp_data = serializer.data
    comments = Activity_comment.objects.filter(activity_id = temp_data['id'], is_delete = False)
    comment_serializer = Activity_comment_serializer(comments, many = True)
    temp_data['comments_list'] = [int(i['id']) for i in comment_serializer.data]
    temp_data['comments'] = comment_serializer.data
    for i in range(len(temp_data['comments'])):
        user = User.objects.get(pk = temp_data['comments'][i]['user_id'])
        user_serializer = User_profile_serializer(user)
        temp_data['comments'][i]['avatar'] = user_serializer.data['picture']
        temp_data['comments'][i]['user_nickname'] = user_serializer.data['nick_name']
        like = Like_activity_comment.objects.filter(comment_id = temp_data['comments'][i]['id'], is_like = '1')
        dislike = Like_activity_comment.objects.filter(comment_id = temp_data['comments'][i]['id'], is_like = '0')
        like_str = [str(i.user_id.id) for i in like]
        dislike_str = [str(i.user_id.id) for i in dislike]
        temp_data['comments'][i]['like_user'] = ' '.join(like_str)
        temp_data['comments'][i]['dislike_user'] = ' '.join(dislike_str)

    if ((not temp_data['is_outdate']) and (datetime.datetime.strptime(temp_data['end_time'], "%Y-%m-%dT%H:%M:%S") < datetime.datetime.now())):
        temp_data['is_outdate'] = True
        activity = Activity.objects.get(pk = temp_data['id'])
        activity.is_outdate = True
        activity.save()

    score = Score.objects.filter(activity_id = temp_data['id'],)
    temp_data['score_list'] = [i.user_id.id for i in score]
    part = Participant_Activity.objects.filter(activity_id = temp_data['id'],)
    temp_data['participants_list'] = [i.user_id.id for i in part]
    
    
    return temp_data