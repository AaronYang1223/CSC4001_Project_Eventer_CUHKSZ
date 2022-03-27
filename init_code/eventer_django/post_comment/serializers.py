from rest_framework import serializers
from .models import Post_comment, Like_post_comment


class Post_comment_serializer(serializers.ModelSerializer):
    class Meta:
        model = Post_comment
        fields = '__all__'