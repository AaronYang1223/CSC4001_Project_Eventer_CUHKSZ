from django.contrib import admin
from comment_activity.models import Like_comment, Comment_activity, Comment

# Register your models here.
admin.site.register(Comment)
admin.site.register(Like_comment)
admin.site.register(Comment_activity)

