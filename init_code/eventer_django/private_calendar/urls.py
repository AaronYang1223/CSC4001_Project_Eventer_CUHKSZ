from django.urls import path
from . import views

# date should be xxxx-xx-xx
urlpatterns = [
    path('private_calendar/<int:user>/<str:start_date>/<str:end_date>', views.calendar)
]
