from distutils.command.upload import upload
from statistics import mode
from time import timezone
from xml.sax import default_parser_list
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import uuid

def user_dictory(instance, filename):
    filename  = 'media/user/' + '{}.png'.format(uuid.uuid4())
    print(filename)
    return filename

# Create your models here.
class User(models.Model):
    
    # django default 
    # id = models.AutoField(primary_key = True)
    email = models.EmailField()
    first_name = models.CharField(max_length = 256)
    last_name = models.CharField(max_length = 256)
    nick_name = models.CharField(max_length = 256)
    is_orginazation = models.BooleanField(default = False)
    
    # default UTC time in settings.py
    create_time = models.DateTimeField(auto_now_add = True)
    picture = ProcessedImageField(upload_to = user_dictory, default = 'media/user/default.png', processors = [ResizeToFill(100, 100)])