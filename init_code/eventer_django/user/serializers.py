from rest_framework import routers, serializers, viewsets
from .models import User

class User_profile_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'nick_name', 'is_organization', 'create_time', 'picture')