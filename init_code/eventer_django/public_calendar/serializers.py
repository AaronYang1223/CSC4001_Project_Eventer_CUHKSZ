from rest_framework import routers, serializers, viewsets
from .models import Public_calendar

class Public_calendar_serializer(serializers.ModelSerializer):
    class Meta:
        model = Public_calendar
        fields = ('id', 'activity_id', 'user_id' 'activity_title', 'activity_start_date', 'activity_end_date', 'is_detele')