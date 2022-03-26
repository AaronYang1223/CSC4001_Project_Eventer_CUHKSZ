from django.db import models

# Create your models here.
class Private_calendar(models.Model):
    
    activity_id = models.ForeignKey('activity.Activity', on_delete = models.CASCADE)
    user_id = models.ForeignKey('user.User', on_delete = models.CASCADE)
    activity_date = models.DateField(auto_now = True)
    is_detele = models.BooleanField(default = False)