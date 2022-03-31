from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:pk>', views.profile),
    path('profile/add', views.profile_add),
    path('profile/change/<int:pk>', views.profile_change),
]
