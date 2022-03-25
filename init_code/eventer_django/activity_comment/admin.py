from django.contrib import admin
from activity_comment.models import Like_activity_comment, Comment_activity_list, Activity_comment

# Register your models here.
admin.site.register(Activity_comment)
admin.site.register(Like_activity_comment)
admin.site.register(Comment_activity_list)

