from rest_framework import routers, serializers, viewsets
from .models import Private_calendar

class Private_calendar_serializer(serializers.ModelSerializer):
    class Meta:
        model = Private_calendar
        fields = ('activity_id', 'user_id', 'activity_title', 'activity_start_date', 'activity_end_date', 'is_detele')