from django.http import HttpResponse
from django.shortcuts import render
from post.models import Post
# Create your views here.
def post_list(request):
    return HttpResponse("this is post-list:")