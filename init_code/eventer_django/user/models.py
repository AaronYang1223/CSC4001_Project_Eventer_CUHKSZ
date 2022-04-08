from distutils.command.upload import upload
from statistics import mode
from time import timezone
from xml.sax import default_parser_list
from datetime import datetime
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import uuid

def user_dictory(instance, filename):
    filename  = 'user/' + '{}.png'.format(uuid.uuid4())
    return filename

# Create your models here.
class User(models.Model):
    
    # django default 
    # id = models.AutoField(primary_key = True)
    email = models.EmailField()
    password = models.CharField(max_length = 1024, default = '123456')
    first_name = models.CharField(max_length = 256)
    last_name = models.CharField(max_length = 256)
    nick_name = models.CharField(max_length = 256)
    is_orginazation = models.BooleanField(default = False)
    
    # default UTC time in settings.py
    create_time = models.DateTimeField(auto_now_add = True)
    picture = ProcessedImageField(upload_to = user_dictory, default = 'user/default.png', processors = [ResizeToFill(100, 100)])

class Email_check_new(models.Model):
    code = models.CharField(max_length=20, verbose_name='Verification Code')
    email = models.EmailField(max_length=50, verbose_name='User Email')
    send_time = models.DateTimeField(default=datetime.now, verbose_name='Send Time', null=True, blank=True)
    exprie_time = models.DateTimeField(null=True)
    email_type = models.CharField(choices=(('register', 'Registration'), ('forget', 'Retrieve Password')), max_length=10)

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)

# class Email_check_old(models.Model):
#     code = models.CharField(max_length=20, verbose_name='Verification Code')
#     email = models.EmailField(max_length=50, verbose_name='User Email')
#     send_time = models.DateTimeField(default=datetime.now, verbose_name='Send Time', null=True, blank=True)
#     exprie_time = models.DateTimeField(null=True)
#     email_type = models.CharField(choices=(('register', 'Registration'), ('forget', 'Retrieve Password')), max_length=10)

#     def __unicode__(self):
#         return '{0}({1})'.format(self.code, self.email)