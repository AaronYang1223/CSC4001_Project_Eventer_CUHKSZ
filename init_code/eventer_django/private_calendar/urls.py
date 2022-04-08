from django.urls import path
from . import views

# date should be xxxx-xx-xx
urlpatterns = [
    path('private_calendar/<int:user>/<str:start_date>/<str:end_date>', views.calendar),
    path('private_calendar/<int:user>', views.calendar_get_user),
    # path('private_calendar/create', views.create_calendar_event)
]
