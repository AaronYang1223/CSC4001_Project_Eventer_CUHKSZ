from django.db import models

# Create your models here.
class Public_calendar(models.Model):
    
    activity_id = models.ForeignKey('activity.Activity', on_delete = models.CASCADE)
    
    # show calendar
    activity_title = models.CharField(max_length = 256, default = 'None')
    activity_date = models.DateField(auto_now = True)
    is_detele = models.BooleanField(default = False)