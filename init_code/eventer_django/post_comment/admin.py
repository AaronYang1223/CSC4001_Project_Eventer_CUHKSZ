from django.contrib import admin
from .models import Post_comment, Like_post_comment

admin.site.register(Post_comment)
# admin.site.register(Comment_post_list)
admin.site.register(Like_post_comment)
