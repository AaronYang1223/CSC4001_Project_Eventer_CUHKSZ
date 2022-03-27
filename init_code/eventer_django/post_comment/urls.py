from django.urls import path
from . import views
import user

urlpatterns = [
    path('post/comment/<int:post_id>', views.post_comment),
    path('post/comment/like/<int:post_id>', views.post_comment_like),
    path('post/comment/user/<int:pk>', user.views.profile),
]
