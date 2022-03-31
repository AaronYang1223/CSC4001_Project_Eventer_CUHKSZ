from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import Post_comment_serializer
from rest_framework.response import Response
from rest_framework import status
from .models import Post_comment, Like_post_comment

@csrf_exempt
def create_activity_comment(request):
    if(request.method=='POST'):
        serializer=Post_comment_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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