from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import Post_serializer
from .models import Post
from user.models import User
from user.serializers import User_profile_serializer
import datetime

@csrf_exempt
def post_create(request):
    if (request.method == 'POST'):
        post_data = JSONParser().parse(request)
        serializer = Post_serializer(data=post_data)
        print(serializer)
        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse({
            "code":"101",
            "message":"post failed"
        })
# user_id = models.ForeignKey(User, related_name = "post", on_delete = models.CASCADE)
# post_tag = models.CharField(max_length = 32)
# post_title = models.CharField(max_length = 256)
# post_content = RichTextField()
# comment_number = models.IntegerField(default = 0)
    
@csrf_exempt
def post_change(request, pk):
    try:
        post = Post.objects.get(pk = pk)
    except:
        return HttpResponse(status = 404)
    if (request.method == 'PUT'):
        data = JSONParser().parse(request)
        serializer = Post_serializer(post, data = data)
        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)


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
def post_order_create_date_all(request):
    
    try:
        posts = Post.objects.filter(is_delete = False).order_by('-create_time')
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Post_serializer(posts, many = True)
        temp_data = post_add_user_info(serializer)
        return JsonResponse(temp_data, json_dumps_params = {'ensure_ascii': False}, safe = False)
    

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
        temp_data = post_add_user_info(serializer)
        return JsonResponse(temp_data, json_dumps_params = {'ensure_ascii': False}, safe = False)
    
@csrf_exempt
def post_order_comment_number_all(request):
    
    try:
        posts = Post.objects.filter(is_delete = False).order_by('-comment_number')
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Post_serializer(posts, many = True)
        temp_data = post_add_user_info(serializer)
        return JsonResponse(temp_data, json_dumps_params = {'ensure_ascii': False}, safe = False)
    
def post_add_user_info(serializer):
    temp_data = serializer.data
    for i in range(len(temp_data)):
        user = User.objects.get(pk = temp_data[i]['user_id'])
        temp_user_serializer = User_profile_serializer(user)
        # is_organization, nick_name, picture
        temp_data[i]['is_organization'] = temp_user_serializer.data['is_organization']
        temp_data[i]['nick_name'] = temp_user_serializer.data['nick_name']
        temp_data[i]['picture'] = temp_user_serializer.data['picture']
    return temp_data


@csrf_exempt
def post_user(request, user_id):
    try:
        posts = Post.objects.filter(user_id = user_id, is_delete = False).order_by('-create_time')
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Post_serializer(posts, many = True)
        temp_data = post_add_user_info(serializer)
        return JsonResponse(temp_data, json_dumps_params = {'ensure_ascii': False}, safe = False)