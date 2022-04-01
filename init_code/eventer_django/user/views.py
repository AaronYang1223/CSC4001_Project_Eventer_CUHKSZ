import imp
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import User_profile_serializer
from .models import User

from .forms import RegisterForm
from django.contrib.auth.hashers import make_password
from utils.email_util import send_email

@csrf_exempt
def profile(request, pk):
    
    try:
        user = User.objects.get(pk = pk)
    except:
        return HttpResponse(status = 404)
    
    if (request.method == 'GET'):
        serializer = User_profile_serializer(user)
        return JsonResponse(serializer.data, safe = False)

# for put method, need to include all fields without default values
@csrf_exempt
def profile_change(request, pk):
    
    try:
        user = User.objects.get(pk = pk)
    except:
        return HttpResponse(status = 404)
    
    # do not limit is_organization
    if (request.method == 'PUT'):
        data = JSONParser().parse(request)
        
        # may need change status code
        if ('is_orginazation' in data and data['is_orginazation'] != user.is_orginazation):
            return HttpResponse(status = 400)

        if ('email' in data and data['email'] != user.email):
            return HttpResponse(status = 400)
        
            
        serializers = User_profile_serializer(user, data = data)
        if (serializers.is_valid()):
            serializers.save()
            return JsonResponse(serializers.data, status = 201)
        return JsonResponse(serializers.errors, status = 400)

@csrf_exempt
def profile_add(request):

    if (request.method == 'POST'):
        data = JSONParser().parse(request)
        if (data['is_orginazation'] == True):
            check_organization(data)
        serializers = User_profile_serializer(data = data)
        if (serializers.is_valid()):
            serializers.save()
            return JsonResponse(serializers.data, status = 201)
        return JsonResponse(serializers.errors, status = 400)

def check_organization(request):
    pass


#send emial
def index(request):
    if request.method == 'GET':
        # 构建form对象, 为了显示验证码
        form = RegisterForm()
        return render(request, 'login.html', {'form': form})
    elif request.method == 'POST':
        # 验证form提交的数据
        form = RegisterForm(request.POST)
        # 判断是否合法
        if form.is_valid():
            # 判断密码是否一致
            email = form.cleaned_data['email']
            pwd = form.cleaned_data['password']
            rePwd = form.cleaned_data['rePassword']
            # 两次密码不一致
            if pwd != rePwd:
                # 返回注册页面和错误信息
                return render(request, 'login.html', {'form': form, 'error': '两次密码不一致!'})
            # 判断用户是否存在
            # 根据email查找用户, 如果用户存在, 返回错误信息
            if User.objects.filter(email=email):
                # 用户已存在
                return render(request, 'login.html', {'form': form, 'errMsg': '该用户已存在!'})
            # 创建用户
            user = User(email=email, password=make_password(pwd))
            # 对用户传递过来的密码进行加密, 将加密之后的数据进行保存
            # 账户状态 未激活
            user.is_active = 0
            # 保存为邮箱地址, 可以使用邮箱登录后台
            user.username = email
            # 保存用户
            user.save()
            # 发送注册邮件
            if send_email(email, send_type='app'):
                # 注册邮件发送成功
                return HttpResponse('恭喜您注册成功, 激活邮件已发送至您的邮箱, 请登录后进行激活操作')
            else:
                return HttpResponse('恭喜您注册成功, 激活邮件发送')
        else:
            # 返回form表单
            # 返回注册页面, 信息回填, 显示错误信息
            return render(request, 'login.html', {'form': form})