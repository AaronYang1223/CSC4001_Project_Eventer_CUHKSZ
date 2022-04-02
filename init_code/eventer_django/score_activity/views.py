from selectors import EpollSelector
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import Participant_Activity_serializer, Score_activity_serializer
from .models import Participant_Activity, Score
from activity.models import Activity
from private_calendar.views import calendar_add


@csrf_exempt
def participant_activity(request, activity_id):
    
    if (request.method == 'GET'):
        try:
            participant_activity_list1 = Participant_Activity.objects.filter(activity_id = activity_id).select_related()
            print(participant_activity_list1.values())
            participant_activity_list2 = [{'id': participant_activity.id, 'user_id': participant_activity.user_id.id, 
                                            'activity_id': participant_activity.activity_id.id, 'first_name': participant_activity.user_id.first_name,
                                            'last_name': participant_activity.user_id.last_name, 'email': participant_activity.user_id.email} 
                                            for participant_activity in participant_activity_list1]
            return JsonResponse(participant_activity_list2, json_dumps_params = {'ensure_ascii': False}, safe = False)
        except:
            return HttpResponse(status = 404)

@csrf_exempt
def participant_activity_add(request):
    
    if (request.method == 'POST'):
        data = JSONParser().parse(request)
        serializers = Participant_Activity_serializer(data = data)
        if (serializers.is_valid()):
            participant_activity = Participant_Activity.objects.filter(user_id = data['user_id'], activity_id = data['activity_id'])
            activity = Activity.objects.get(id = data['activity_id'])

            if (len(participant_activity) != 0):
                return JsonResponse('User {} already participant activity {}'.format(data['user_id'], data['activity_id']), status = 404, safe = False)
            
            if (activity.participant_num >= activity.max_participant_num):
                return JsonResponse('The number of participant is already full for activity: {}.'.format(data['activity_id']), status = 404, safe = False)
            else:
                activity.participant_num += 1
                activity.part_max_num = activity.participant_num / activity.max_participant_num
                activity.save()
                
            serializers.save()
            
            # update calendar
            res = calendar_add(data['activity_id'], data['user_id'])
            
            # can not add to private calendar
            if (not res):
                return JsonResponse('Can not add to private calendar, activity_id: {}, user_id: {}'.format(data['activity_id'], data['user_id']), status = 400)
            
            return JsonResponse(serializers.data, status = 201)
        return JsonResponse(serializers.errors, status = 400)
    
@csrf_exempt
def score_add(request):
    if (request.method == 'POST'):
        data = JSONParser().parse(request)
        serializers = Score_activity_serializer(data = data)
        if (serializers.is_valid()):
            
            # check if score exists
            scores = Score.objects.filter(user_id = data['user_id'], activity_id = data['activity_id'])
            if (scores.values()):
                return JsonResponse('score already exist: user_id: {}, activity_id: {}, score: {}'.format(data['user_id'], data['activity_id'], data['score']), status = 400, safe = False)
        
            # update activity score
            activity = Activity.objects.get(id = data['activity_id'])
            
            # check if activity is finished
            if (not activity.is_outdate):
                return JsonResponse('activity {} is not finished'.format(data['activity_id']), status = 400, safe = False)
            
            # update activity score
            activity.score_avg = (activity.score_avg * activity.score_num + data['score']) / (activity.score_num + 1)
            activity.score_num += 1
            activity.save()
            serializers.save()
            
            return JsonResponse(serializers.data, status = 201)
        return JsonResponse(serializers.errors, status = 400)