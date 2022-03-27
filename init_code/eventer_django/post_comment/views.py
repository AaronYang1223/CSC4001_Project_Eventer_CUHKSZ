from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import Post_comment_serializer
from .models import Post_comment, Like_post_comment

@csrf_exempt
def post_comment(request, post_id):
    
    # may return [], do not change for now
    try:
        comment = Post_comment.objects.filter(post_id = post_id, is_delete = False).order_by('-create_time')
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Post_comment_serializer(comment, many = True)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)
    
    
@csrf_exempt
def post_comment_like(request, post_id):
    
    try:
        comment = Post_comment.objects.filter(post_id = post_id, is_delete = False).order_by('-like_num')
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Post_comment_serializer(comment, many = True)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)