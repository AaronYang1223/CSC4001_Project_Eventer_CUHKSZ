from django.contrib import admin
from activity_comment.models import Like_activity_comment, Activity_comment

# Register your models here.
admin.site.register(Activity_comment)
admin.site.register(Like_activity_comment)

