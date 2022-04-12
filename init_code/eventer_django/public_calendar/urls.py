from django.urls import path

from . import views

# date should be xxxx-xx-xx
urlpatterns = [
    path('public_calendar/<str:start_date>/<str:end_date>', views.calendar),
    # path('public_calendar/create', views.create_calendar_event)
    path('public_calendar/all', views.calendar_public_all),
]
