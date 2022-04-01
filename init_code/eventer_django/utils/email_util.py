from django.core.mail import send_mail
from user.models import Email_check_new
import random
import datetime
from eventer_django import settings
from datetime import timedelta

def random_codechr(length=16):
    # 随机大小写组合的验证码
    chars = 'quFDGDbtwehykjahuhufHFCUHNCWEHAFDONCJUHU'
    codechr = ''
    for x in range(length):
        # 随机取出一个字符
        codechr += random.choice(chars)
    return codechr

def send_email(to_email, send_type='app'):
    """
    :param to_email: 收件人的邮箱
    :param send_type: 邮件类型
    :return: 邮件发送结果
    """
    email = Email_check_new()
    # 获取验证码
    email.code = random_codechr()
    # 收件人
    email.email = to_email
    # 过期时间
    email.exprie_time = datetime.datetime.now() + datetime.timedelta(days=7)
    # 邮件类型
    email.send_type = send_type
    # 发送邮件
    try:
        res = send_mail('论坛激活邮件', '', settings.EMAIL_HOST_USER, [to_email], html_message='欢迎注册论坛, 点击链接激活你的账户:<a href="127.0.0.1:8000/active/{}">127.0.0.1:8000/active/{}</a>'.format(email.code, email.code))
        if res == 1:
            # 保存邮件记录
            email.save()
            return True
        else:
            return False
    #except Email_check_new as e:
    #    print(e)
    #    return False'''
    except:
        pass