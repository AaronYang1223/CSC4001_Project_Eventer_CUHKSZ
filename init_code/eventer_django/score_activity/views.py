from django.shortcuts import render
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import Participant_Activity_serializer
from .models import Participant_Activity

@csrf_exempt
def participant_activity(request, activity_id):
    
    if (request.method == 'GET'):
        try:
            participant_activity_list1 = Participant_Activity.objects.filter(activity_id = activity_id).select_related()
            participant_activity_list2 = [{'id': participant_activity.id, 'user_id': participant_activity.user_id.id, 
                                            'activity_id': participant_activity.activity_id.id, 'first_name': participant_activity.user_id.first_name,
                                            'last_name': participant_activity.user_id.last_name, 'email': participant_activity.user_id.email} 
                                            for participant_activity in participant_activity_list1]
            return JsonResponse(participant_activity_list2, json_dumps_params = {'ensure_ascii': False}, safe = False)
        except:
            return HttpResponse(status = 404)