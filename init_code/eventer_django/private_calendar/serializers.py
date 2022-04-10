from rest_framework import routers, serializers, viewsets
from .models import Private_calendar

class Private_calendar_serializer(serializers.ModelSerializer):
    class Meta:
        model = Private_calendar
        fields = '__all__'