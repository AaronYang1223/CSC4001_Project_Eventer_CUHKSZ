from rest_framework import routers, serializers, viewsets
from .models import Activity

class Activity_serializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'