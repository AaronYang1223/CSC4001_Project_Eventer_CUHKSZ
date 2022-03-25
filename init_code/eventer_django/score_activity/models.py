from django.db import models
from activity.models import Activity
from user.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Score(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    activity_id = models.ForeignKey(Activity, on_delete = models.CASCADE)
    score = models.IntegerField(
        default = 1,
        validators = [
            MaxValueValidator(10),
            MinValueValidator(1)
        ])

class Participant_Activity(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    activity_id = models.ForeignKey(Activity, on_delete = models.CASCADE)