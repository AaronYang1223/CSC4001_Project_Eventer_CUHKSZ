from django.db import models
from pyexpat import model
from ckeditor.fields import RichTextField
from user.models import User
from post.models import Post
# Create your models here.

class Post_comment(models.Model):
    
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    #post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = RichTextField()
    like_num = models.IntegerField(default = 0)
    dislike_num = models.IntegerField(default = 0)
    create_time = models.DateTimeField(auto_now_add = True)
    is_delete = models.BooleanField(default = False)

class Comment_post_list(models.Model):
    post_id = models.ForeignKey(Post, on_delete = models.CASCADE)
    comment_id = models.ForeignKey(Post_comment, on_delete = models.CASCADE)
    is_delete = models.BooleanField(default = False)

class Like_post_comment(models.Model):
    LIKE = '1'
    DISLIKE = '0'
    CANCEL = '2'
    
    LIKE_STATE = [
        (LIKE, 'like comment'),
        (DISLIKE, 'dislike comment'),
        (CANCEL, 'cancel like or dislike'),
    ]
    
    comment_id = models.ForeignKey(Post_comment, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    is_like = models.CharField(max_length = 1, choices = LIKE_STATE, default = CANCEL)
    is_delete = models.BooleanField(default = False)