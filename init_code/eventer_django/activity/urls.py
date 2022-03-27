from django.urls import path
from . import views


urlpatterns = [
    path('activity/<int:pk>', views.activity_pk),
    path('activity/tag/<str:tag>', views.activity_tag),
]
