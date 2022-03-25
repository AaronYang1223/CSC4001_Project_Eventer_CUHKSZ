from django.contrib import admin
from .models import PostComment, PostComment_Post, Like_PostComment

admin.site.register(PostComment)
admin.site.register(PostComment_Post)
admin.site.register(Like_PostComment)
# Register your models here.
