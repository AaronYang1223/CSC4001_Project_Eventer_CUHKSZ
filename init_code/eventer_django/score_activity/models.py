from django.db import models
from activity.models import Activity
from user.models import User

class Score(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    activity_id=models.ForeignKey(Activity, on_delete=models.CASCADE)
    score = models.IntegerField()

class Participant_Activity(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    activity_id=models.ForeignKey(Activity, on_delete=models.CASCADE)