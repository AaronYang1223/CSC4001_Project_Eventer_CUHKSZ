from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from  user.models import User
import uuid


# Create your models here.
class Post(models.Model):
    user_id = models.ForeignKey(User,related_name="post", on_delete=models.CASCADE)
    post_tag = models.CharField(max_length = 32)
    post_title = models.CharField(max_length = 256)
    post_content = RichTextField()
    comment_number = models.IntegerField(default = 0)
    #cover_page = ProcessedImageField(upload_to = cover_dictory, default = 'media/activicity/default.png', processors = [ResizeToFill(1920, 960)])
    create_time = models.DateTimeField(auto_now = True)
    is_delete = models.BooleanField(default=False)