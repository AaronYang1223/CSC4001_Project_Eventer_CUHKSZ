from django.urls import path
from . import views

urlpatterns = [
    path('activity/<int:activity_id>/participant', views.participant_activity),
    path('activity/participant/add', views.participant_activity_add),
    path('activity/score/add', views.score_add),
    path('activity/score/<int:pk>', views.score_list)
]
