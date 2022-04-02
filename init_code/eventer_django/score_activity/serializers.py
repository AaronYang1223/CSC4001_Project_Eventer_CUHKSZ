from rest_framework import serializers
from .models import Participant_Activity, Score

class Participant_Activity_serializer(serializers.ModelSerializer):
    class Meta:
        model = Participant_Activity
        fields = ['id', 'user_id__first_name', 'user_id__last_name', 'user_id__email']

class Score_activity_serializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['id', 'user_id', 'activity_id', 'score']