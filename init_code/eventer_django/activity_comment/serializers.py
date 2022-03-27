from rest_framework import serializers
from .models import Activity_comment, Like_activity_comment, Comment_activity_list


class Activity_comment_serializer(serializers.ModelSerializer):
    class Meta:
        model = Activity_comment
        fields = '__all__'
        
class Comment_activity_list_serializer(serializers.ModelSerializer):
    class Meta:
        model = Comment_activity_list
        fields = '__all__'