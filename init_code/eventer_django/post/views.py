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
def post_pk(request,pk):
    #id = request.GET.get("id")
    try:
        post = Post.objects.get(pk = pk, is_delete = False)
    except:
        return JsonResponse({'code' : '404'})
    
    if (request.method == 'GET'):
        serializer = Post_serializer(post)
        temp_data = post_add_comment_info(serializer)
        return JsonResponse(temp_data, json_dumps_params = {'ensure_ascii': False}, safe = False)

def post_add_comment_info(serializer):
    temp_data = serializer.data
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
        like_str = [str(i.user_id.id) for i in like]
        dislike_str = [str(i.user_id.id) for i in dislike]
        temp_data['comments'][i]['like_user'] = ' '.join(like_str)
        temp_data['comments'][i]['dislike_user'] = ' '.join(dislike_str)
    return temp_data

# def post_add_comment_info(serializer):
#     temp_data = serializer.data
#     #print(temp_data)
#     all_comments = Post_comment.objects.filter(post_id = temp_data['id'])
#     all_comments_serializer = Post_comment_serializer(all_comments, many=True)
#     #print(all_comment_serializer)
    
#     temp_data['comment'] = [{"user": {
#                 "user_id": '',
#                 "nick_name": "",
#                 "avatar": ""
#             },
#             "content": "",
#             "likeNum": '',
#             "likeId": "",
#             "dislikeId": ""}]*len(all_comments_serializer.data)
    
#     for i in range(len(all_comments_serializer.data)):
#         print(i)
#         #print(all_comments_serializer.data[i]['user_id'])
#         user_info = User.objects.get(id = all_comments_serializer.data[i]['user_id'])
        
#         user_info_serializer = User_profile_serializer(user_info)
#         comment_like_info = Like_post_comment.objects.filter(comment_id=all_comments_serializer.data[i]['id'], is_like='1')
#         comment_dislike_info = Like_post_comment.objects.filter(comment_id=all_comments_serializer.data[i]['id'], is_like='0')
#         likeId = ""
#         dislikeId = ""
#         for item in comment_like_info:
#             likeId = likeId + str(item.user_id.id) + " "
#         for item in comment_dislike_info:
#             dislikeId = dislikeId + str(item.user_id.id) + " "
#         temp_data['comment'][i]['user'] = {
#                                             "user_id": all_comments_serializer.data[i]['user_id'],
#                                             "nick_name" : user_info_serializer.data['nick_name'],
#                                             "avatar": "http://127.0.0.1:8000"+user_info_serializer.data['picture'],
#                                             #"likeNum": all_comments[i].like_num,
#                                             #"dislikeNum": all_comments[i].dislike_num,
#                                             #"likeId": likeId,
#                                             #"dislikeId": dislikeId
#                                         }
#         temp_data['comment'][i]['content'] = all_comments[i].content
#         #print(temp_data['comment'][i]['content'],i)
#         temp_data['comment'][i]['likeNum'] = all_comments[i].like_num
#         temp_data['comment'][i]['likeId'] = likeId
#         temp_data['comment'][i]['dislikeId'] = dislikeId
#         print(temp_data['comment'][0])
        
#     print (temp_data['comment'])
#     return temp_data
    
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