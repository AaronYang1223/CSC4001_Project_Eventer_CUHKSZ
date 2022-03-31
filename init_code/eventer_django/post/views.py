from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import Post_serializer
from .models import Post
import datetime

@csrf_exempt
def create_activity_comment(request):
    if(request.method=='POST'):
        serializer=Post_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def post_pk(request, pk):
    try:
        post = Post.objects.get(pk = pk, is_delete = False)
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Post_serializer(post)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)
    
    
@csrf_exempt
def post_tag(request, tag):
    try:
        posts = Post.objects.filter(post_tag__icontains = tag, is_delete = False)
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Post_serializer(posts, many = True)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)
    

@csrf_exempt
def post_title(request, title):
    try:
        posts = Post.objects.filter(post_title__icontains = title, is_delete = False)
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Post_serializer(posts, many = True)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)
    
@csrf_exempt
def post_order_create_date(request, num):
    
    if (num <= 0):
        return HttpResponse(status = 404)
    
    try:
        posts = Post.objects.filter(is_delete = False).order_by('-create_time')[:num]
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Post_serializer(posts, many = True)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)
    

@csrf_exempt
def post_order_comment_number(request, num):
    
    if (num <= 0):
        return HttpResponse(status = 404)

    try:
        posts = Post.objects.filter(is_delete = False).order_by('-comment_number')[:num]
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Post_serializer(posts, many = True)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)