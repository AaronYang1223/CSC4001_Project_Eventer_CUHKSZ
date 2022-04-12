from django.urls import path
from . import views



urlpatterns = [
    path('post/<int:pk>', views.post_pk),
    path('post/create/', views.post_create),
    path('post/tag/<str:tag>', views.post_tag),
    path('post/title/<str:title>', views.post_title),
    
    # which should be xxxx-xx-xx
    path('post/order/create_date/<int:num>', views.post_order_create_date),
    path('post/order/create_date/all', views.post_order_create_date_all),
    path('post/order/comment_number/<int:num>', views.post_order_comment_number),
    path('post/order/comment_number/all', views.post_order_comment_number_all),
    path('post/user/<int:user_id>', views.post_user),
]