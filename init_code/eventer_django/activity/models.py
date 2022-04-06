from pyexpat import model
from wsgiref.validate import validator
from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator

def cover_dictory(instance, filename):
    filename  = 'activity/' + '{}.png'.format(uuid.uuid4())
    return filename


class Activity(models.Model):
        
    tag = models.CharField(max_length = 32)
    organizer_id = models.ForeignKey('user.User', on_delete = models.CASCADE, related_name = 'originizer_id', default = 1)
    # start_time = models.DateTimeField(auto_now = True, editable = True)
    start_time = models.DateTimeField(editable = True)
    end_time = models.DateTimeField(editable = True)
    title = models.CharField(max_length = 256)
    content = RichTextField()
    comment_number = models.IntegerField(default = 0)
    cover_page = ProcessedImageField(upload_to = cover_dictory, default = 'activicity/default.png', processors = [ResizeToFill(1920, 1080)])
    participant_num = models.IntegerField(default = 0)
    max_participant_num = models.IntegerField(default = 1, 
                                                validators = [
                                                    MinValueValidator(1),
                                                ])
    part_max_num = models.FloatField(default = 0.0, 
                                        validators = [
                                            MaxValueValidator(1.0),
                                        ])
    create_time = models.DateTimeField(auto_now_add = True)
    score_avg = models.FloatField(default = 0.0,
                                    validators = [
                                        MinValueValidator(0.0),
                                        MaxValueValidator(10.0),
                                    ])
    score_num = models.IntegerField(default = 0)
    is_public = models.BooleanField(default = False)
    is_delete = models.BooleanField(default = False)
    is_outdate = models.BooleanField(default = False)
    is_private = models.BooleanField(default = False)