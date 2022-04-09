from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:pk>', views.profile),
    path('profile/add', views.profile_add),
    path('profile/change', views.profile_change),
    path('profile/retrieve', views.profile_retrieve),
    path('profile/send_email', views.email_verification),
    path('profile/upload/<int:pk>', views.profile_upload_picture),
]
