"""eventer_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# for picture
from django.urls import re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    path('captcha/', include('captcha.urls')),
    
    path('api/', include('user.urls')),
    path('api/', include('private_calendar.urls')),
    path('api/', include('public_calendar.urls')),
    path('api/', include('activity.urls')),
    path('api/', include('activity_comment.urls')),
    path('api/', include('score_activity.urls')),
    path('api/', include('post.urls')),
    path('api/', include('post_comment.urls')),
]
