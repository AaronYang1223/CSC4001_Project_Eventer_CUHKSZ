from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import uuid

def cover_dictory(instance, filename):
    filename  = 'media/activity/' + '{}.png'.format(uuid.uuid4())
    print(filename)
    return filename


class Activity(models.Model):
        
    tag = models.CharField(max_length = 32)
    start_time = models.DateTimeField(auto_now = True)
    end_time = models.DateTimeField(auto_now = True)
    title = models.CharField(max_length = 256)
    content = RichTextField()
    comment_number = models.IntegerField(default = 0)
    cover_page = ProcessedImageField(upload_to = cover_dictory, default = 'media/activicity/default.png', processors = [ResizeToFill(1920, 960)])
    participant_num = models.IntegerField(default = 0)
    max_participant_num = models.IntegerField(default = 0)
    create_time = models.DateTimeField(auto_now_add = True)
    is_public = models.BooleanField(default = False)
    is_delete = models.BooleanField(default = False)
    is_outdate = models.BooleanField(default = False)