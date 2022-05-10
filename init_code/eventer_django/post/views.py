import imp
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import Post_serializer
from .models import Post
from post_comment.models import Post_comment, Like_post_comment
from post_comment.serializers import Post_comment_serializer,Like_post_comment_serializer
from user.models import User
from user.serializers import User_profile_serializer
import datetime

# create post
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

# change post info
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

# return all post information, including post information, comments, commenters, likers, dislikers
@csrf_exempt
def post_pk(request, pk):
    try:
        post = Post.objects.get(pk = pk, is_delete = False)
    except:
        return JsonResponse({'code' : '404'})
    
    if (request.method == 'GET'):
        serializer = Post_serializer(post)
        temp_data = post_add_comment_info(serializer)
        return JsonResponse(temp_data, json_dumps_params = {'ensure_ascii': False}, safe = False)

# add comment information to post
def post_add_comment_info(serializer):
    temp_data = serializer.data

    post_user = User.objects.get(pk=temp_data['user_id'])
    post_user_serializer = User_profile_serializer(post_user)
    temp_data['user_nickname'] = post_user_serializer.data['nick_name']
    temp_data['user_avatar'] = post_user_serializer.data['picture']
    temp_data['user_is_organization'] = post_user_serializer.data['is_organization']

    comments = Post_comment.objects.filter(post_id = temp_data['id'], is_delete = False)
    comment_serializer = Post_comment_serializer(comments, many = True)
    temp_data['comments_list'] = [int(i['id']) for i in comment_serializer.data]
    temp_data['comments'] = comment_serializer.data

    for i in range(len(temp_data['comments'])):
        user = User.objects.get(pk = temp_data['comments'][i]['user_id'])
        user_serializer = User_profile_serializer(user)
        temp_data['comments'][i]['avatar'] = user_serializer.data['picture']
        temp_data['comments'][i]['user_nickname'] = user_serializer.data['nick_name']
        like = Like_post_comment.objects.filter(comment_id = temp_data['comments'][i]['id'], is_like = '1')
        dislike = Like_post_comment.objects.filter(comment_id = temp_data['comments'][i]['id'], is_like = '0')
        not_like_dislike = Like_post_comment.objects.filter(comment_id = temp_data['comments'][i]['id'], is_like = '2')
        like_str = [str(i.user_id.id) for i in like]
        dislike_str = [str(i.user_id.id) for i in dislike]
        not_like_dislike_str = [str(i.user_id.id) for i in not_like_dislike]
        temp_data['comments'][i]['like_user'] = ' '.join(like_str)
        temp_data['comments'][i]['dislike_user'] = ' '.join(dislike_str)
        temp_data['comments'][i]['had_commented'] = ' '.join(not_like_dislike_str)
    return temp_data

# return all posts which tags contain the keyword
@csrf_exempt
def post_tag(request, tag):
    try:
        posts = Post.objects.filter(post_tag__icontains = tag, is_delete = False)
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Post_serializer(posts, many = True)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)
    

# reutrn all posts which title contains the keyword
@csrf_exempt
def post_title(request, title):
    try:
        posts = Post.objects.filter(post_title__icontains = title, is_delete = False)
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = Post_serializer(posts, many = True)
        return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, safe = False)

# return the fixed number of posts, which are sorted by create time
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

# return all posts which are sorted by create time
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
    

# return the fixed number of posts which are sorted by comment number
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

# return all posts which are sorted by comment number
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

# return specific usre's posts which are sorted by create time
@csrf_exempt
def post_user_order_comment_num(request, user_id):

    try:
        posts = Post.objects.filter(user_id = user_id, is_delete = False).order_by('-create_time')
    except:
        return HttpResponse(status = 404)

    if (request.method == 'GET'):
        serializer = Post_serializer(posts, many = True)
        temp_data = post_add_user_info(serializer)
        return JsonResponse(temp_data, json_dumps_params = {'ensure_ascii': False}, safe = False)

# return specific usre's posts which are sorted by comment number
@csrf_exempt
def post_user_order_create_date(request, user_id):

    try:
        posts = Post.objects.filter(user_id = user_id, is_delete = False).order_by('-comment_number')
    except:
        return HttpResponse(status = 404)

    if (request.method == 'GET'):
        serializer = Post_serializer(posts, many = True)
        temp_data = post_add_user_info(serializer)
        return JsonResponse(temp_data, json_dumps_params = {'ensure_ascii': False}, safe = False)

# add user info to the post
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

# return specific usre's posts which are sorted by create time, deprecated
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