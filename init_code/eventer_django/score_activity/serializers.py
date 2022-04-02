from rest_framework import serializers
from .models import Participant_Activity, Score

class Participant_Activity_serializer(serializers.ModelSerializer):
    class Meta:
        model = Participant_Activity
        fields = ['id', 'activity_id', 'user_id']

class Score_activity_serializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['id', 'user_id', 'activity_id', 'score']