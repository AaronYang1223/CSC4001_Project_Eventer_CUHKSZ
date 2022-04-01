from django.urls import path
from . import views


urlpatterns = [
    path('activity/', views.activity_list),
    path('activity/create/', views.create_activity),
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
    path('activity/order/comment_number/<int:numn>', views.activity_order_comment_number),
]
