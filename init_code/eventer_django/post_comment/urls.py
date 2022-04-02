from django.urls import path
from . import views
import user

urlpatterns = [
    path('post/comment/<int:post_id>', views.post_comment),
    path('post/comment/like/<int:post_id>', views.post_comment_like),
    path('post/comment/user/<int:pk>', user.views.profile),
    path('post/comment/like/add_change', views.post_comment_like_add),
    path('post/comment/like/<int:comment>/<int:user>', views.post_comment_like_get),
    path('post/comment/create', views.post_comment_create),
]
