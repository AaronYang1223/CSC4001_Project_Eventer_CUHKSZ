from django.urls import path
from . import views

urlpatterns = [
    path('activity/<int:activity_id>/participant', views.participant_activity),
]
