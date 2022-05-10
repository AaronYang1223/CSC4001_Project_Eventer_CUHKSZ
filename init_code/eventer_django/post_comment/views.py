from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import Post_comment_serializer, Like_post_comment_serializer
from rest_framework.response import Response
from rest_framework import status
from .models import Post_comment, Like_post_comment
from post.models import Post

@csrf_exempt
def post_comment_create(request):
    if (request.method=='POST'):
        data = JSONParser().parse(request)
        serializer = Post_comment_serializer(data = data)
        print(data)
        if serializer.is_valid():
            serializer.save()
            print("success")
            # update post comment num
            post = Post.objects.get(id = serializer.data['post_id'])
            post.comment_number += 1
            post.save()
            
            return JsonResponse(serializer.data, json_dumps_params = {'ensure_ascii': False}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def post_comment(request, post_id):
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
        serializers = Like_post_comment_serializer(data = data)
        
        if (serializers.is_valid()):
            if (Like_post_comment.objects.filter(comment_id = data['comment_id'], user_id = data['user_id']).values()):
                return HttpResponse(status = 404)
            serializers.save()
            
            post_comment = Post_comment.objects.get(id = data['comment_id'])
            if (serializers.data['is_like'] == '1'):
                post_comment.like_num += 1
            elif (serializers.data['is_like'] == '0'):
                post_comment.dislike_num += 1
            
            post_comment.save()
            
            return JsonResponse(serializers.data, status = 201, safe = False)
        return JsonResponse(serializers.errors, status = 400)
    elif (request.method == 'PUT'):
        data = JSONParser().parse(request)
        
        try:
            print(Like_post_comment.objects.all().values())
            like_post = Like_post_comment.objects.get(comment_id = data['comment_id'], user_id = data['user_id'])
        except:
            return HttpResponse(status = 404)
        
        # update like number and dislike number
        post_comment = Post_comment.objects.get(id = data['comment_id'])
        if (data['is_like'] == '1' and like_post.is_like == '2'):
            post_comment.like_num += 1
        elif (data['is_like'] == '1' and like_post.is_like == '0'):
            post_comment.like_num += 1
            post_comment.dislike_num -= 1
        elif (data['is_like'] == '0' and like_post.is_like == '2'):
            post_comment.dislike_num += 1
        elif (data['is_like'] == '0' and like_post.is_like == '1'):
            post_comment.like_num -= 1
            post_comment.dislike_num += 1
        elif (data['is_like'] == '2' and like_post.is_like == '0'):
            post_comment.dislike_num -= 1
        elif (data['is_like'] == '2' and like_post.is_like == '1'):
            post_comment.like_num -= 1
        
        like_post.is_like = data['is_like']
        like_post.save()
        post_comment.save()
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