from django.urls import path
from . import views


urlpatterns = [
    path('activity/<int:pk>', views.activity_pk),
    path('activity/tag/<str:tag>', views.activity_tag),
    path('activity/title/<str:title>', views.activity_title),
    path('activity/order/part_max/<int:num>', views.activity_order_part_max),
    path('activity/order/score/<int:num>', views.activity_order_score),
    
    # which should be xxxx-xx-xx
    path('activity/order/start_date/<int:num>', views.activity_order_start_date),
    path('activity/order/create_date/<int:num>', views.activity_order_create_date),
]
