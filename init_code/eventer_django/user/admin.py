from django.contrib import admin
from user.models import User, Email_check_new

# Register your models here.
admin.site.register(User)
admin.site.register(Email_check_new)