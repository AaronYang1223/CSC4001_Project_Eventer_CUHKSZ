from rest_framework import serializers
from .models import Activity_comment, Like_activity_comment


class Activity_comment_serializer(serializers.ModelSerializer):
    class Meta:
        model = Activity_comment
        fields = '__all__'
        
class Like_activity_comment_serializer(serializers.ModelSerializer):
    class Meta:
        model = Like_activity_comment
        fields = '__all__'