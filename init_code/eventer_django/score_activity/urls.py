from django.urls import path
from . import views

urlpatterns = [
    path('activity/<int:activity_id>/participant', views.participant_activity),
    path('activity/<int:activity_id>/participant/add', views.participant_activity_add),
    path('activity/score/add', views.score_add),
]
