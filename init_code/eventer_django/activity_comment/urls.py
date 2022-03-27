from django.urls import path
from . import views
import user

urlpatterns = [
    path('activity/comment/<int:activity_id>', views.activity_comment),
    path('activity/comment/like/<int:activity_id>', views.activity_comment_like),
    path('activity/comment/user/<int:pk>', user.views.profile),
]
