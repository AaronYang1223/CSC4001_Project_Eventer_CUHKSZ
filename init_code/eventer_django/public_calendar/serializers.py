from rest_framework import routers, serializers, viewsets
from .models import Public_calendar

class Public_calendar_serializer(serializers.ModelSerializer):
    class Meta:
        model = Public_calendar
        fields = '__all__'