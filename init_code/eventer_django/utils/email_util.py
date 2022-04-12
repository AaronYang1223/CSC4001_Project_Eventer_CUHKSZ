from atexit import register
from django.core.mail import send_mail
from user.models import Email_check_new
import random
import datetime
from eventer_django import settings
from datetime import timedelta

def random_codechr(length=6):
    # 随机大小写组合的验证码
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    codechr = ''
    for x in range(length):
        # 随机取出一个字符
        codechr += random.choice(chars)
    return codechr

def send_email(to_email, send_type='register'):
    """
    :param to_email: 收件人的邮箱
    :param send_type: 邮件类型
    :return: 邮件发送结果
    """
    code = random_codechr()
    #if(send_type == "register"):
    email = Email_check_new()
    #elif(send_type == "retrieve"):
    #    email = Email_check_old()
    # 获取验证码
    email.code = code
    # 收件人
    email.email = to_email
    #发送时间
    email.send_time = datetime.datetime.now()
    # 过期时间
    email.exprie_time = datetime.datetime.now() + datetime.timedelta(days=7)
    # 邮件类型
    email.email_type = send_type

    email.save()
    # 发送邮件
    email_title = ""
    email_body = ""
    if(send_type == "register"):
        email_title = "注册激活"
        email_body = "您的邮箱注册验证码为：{0}, 该验证码有效时间为7天，请及时进行验证。".format(code)
        send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [to_email])
        if(not send_status):
            return False
    if send_type == "retrieve":
        email_title = "找回密码"
        email_body = "您的邮箱验证码为：{0}, 该验证码有效时间为7天，请及时进行验证。".format(code)
        # 发送邮件
        send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [to_email])
        if not send_status:
            return False
    return True

def send_check_organization_email(to_email):
    email_title = "组织者账号验证"
    email_body = "请回复此封邮件以请求认证成为组织者账号，内容包括你的邮箱与组织名称。"
    send_status = send_email(email_title, email_body, settings.EMAIL_FROM,[to_email])
    if(not send_status):
        return False
    return True