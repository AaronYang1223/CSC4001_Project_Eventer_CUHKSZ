from email.policy import default
from django.db import models

# Create your models here.
class Private_calendar(models.Model):
    
    activity_id = models.ForeignKey('activity.Activity', on_delete = models.CASCADE)
    user_id = models.ForeignKey('user.User', on_delete = models.CASCADE, related_name = 'owner')
    # organizer_id = models.ForeignKey('user.User', on_delete = models.CASCADE, related_name = 'organizer_id')
    
    # show calendar
    activity_title = models.CharField(max_length = 256, default = 'None')
    activity_start_date = models.DateTimeField(editable = True)
    activity_end_date = models.DateTimeField(editable = True)
    is_delete = models.BooleanField(default = False)