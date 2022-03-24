from email.policy import default
from pyexpat import model
from django.db import models
from ckeditor.fields import RichTextField


class Comment(models.Model):
    
    user_id = models.ForeignKey('user.User', on_delete = models.CASCADE)
    content = RichTextField()
    like_num = models.IntegerField(default = 0)
    dislike_num = models.IntegerField(default = 0)
    create_time = models.DateTimeField(auto_now_add = True)
    is_delete = models.BooleanField(default = False)
    

class Like_comment(models.Model):
    
    LIKE = '1'
    DISLIKE = '0'
    CANCEL = '2'
    
    LIKE_STATE = [
        (LIKE, 'like comment'),
        (DISLIKE, 'dislike comment'),
        (CANCEL, 'cancel like or dislike'),
    ]
    
    comment_id = models.ForeignKey(Comment, on_delete = models.CASCADE)
    user_id = models.ForeignKey('user.User', on_delete = models.CASCADE)
    is_like = models.CharField(max_length = 1, choices = LIKE_STATE, default = CANCEL)
    is_delete = models.BooleanField(default = False)

class Comment_activity(models.Model):
    
    activity_id = models.ForeignKey('activity.Activity', on_delete = models.CASCADE)
    comment_id = models.ForeignKey(Comment, on_delete = models.CASCADE)
    is_delete = models.BooleanField(default = False)

