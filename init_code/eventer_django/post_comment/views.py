from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import Post_comment_serializer, Like_post_comment_serializer
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

@csrf_exempt
def post_comment_like_add(request):
    
    if (request.method == 'POST'):
        data = JSONParser().parse(request)
        print(data)
        serializers = Like_post_comment_serializer(data = data)
        
        if (serializers.is_valid()):
            serializers.save()
            
            return JsonResponse(serializers.data, status = 201, safe = False)
        return JsonResponse(serializers.errors, status = 400)
    elif (request.method == 'PUT'):
        data = JSONParser().parse(request)
        try:
            like_post = Like_post_comment.objects.get(comment_id = data['comment_id'], user_id = data['user_id'])
        except:
            return HttpResponse(status = 404)
        
        like_post.is_like = data['is_like']
        like_post.save()
        return JsonResponse('Change like status to {}.'.format(like_post.is_like), status = 201, safe = False)
    
    
# if do not exit, add a default
@csrf_exempt
def post_comment_like_get(request, comment, user):
    
    try:
        like_post = Like_post_comment.objects.get(comment_id = comment, user_id = user)
    except:
        data = {
            'comment_id': comment,
            'user_id': user,
            'is_like': "2"
        }
        serializers = Like_post_comment_serializer(data = data)
    
        if (serializers.is_valid()):
            serializers.save()
            
            return JsonResponse(serializers.data, status = 201, safe = False)
        return JsonResponse(serializers.errors, status = 400)
    
    if (request.method == 'GET'):
        serializer = Like_post_comment_serializer(like_post)
        return JsonResponse(serializer.data, safe = False)