from django.urls import path
from . import views


urlpatterns = [
    path('activity/list', views.activity_list),
    path('activity/create', views.activity_create),
    path('activity/<int:pk>', views.activity_pk),
    path('activity/change/<int:pk>', views.activity_change_pk),
    path('activity/upload/<int:pk>', views.activity_upload_cover),
    path('activity/tag/<str:tag>', views.activity_tag),
    path('activity/title/<str:title>', views.activity_title),
    path('activity/order/part_max/<int:num>', views.activity_order_part_max),
    path('activity/order/score/<int:num>', views.activity_order_score),
    
    # which should be xxxx-xx-xx
    path('activity/order/start_date/<int:num>', views.activity_order_start_date),
    path('activity/order/create_date/<int:num>', views.activity_order_create_date),
    path('activity/order/comment_number/<int:num>', views.activity_order_comment_number),
    path('activity/order/create_date/all', views.activity_order_create_date_all),
    path('activity/order/comment_number/all', views.activity_order_comment_number_all),
    path('activity/user/<int:user_id>', views.activity_user),
    path('activity/user/order/comment_number/<int:user_id>', views.activity_user_order_comment_num),
    path('activity/user/order/create_date/<int:user_id>', views.activity_user_order_create_time),
    path('activity/<int:activity_id>/comment', views.activity_comment),
]
