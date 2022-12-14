"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from downloader.views.views import videos_list, about_view
from downloader.views.download import download_video, download_audio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', videos_list, name='videos'),
    path('download_video/<str:video_id>/<str:resolution>', download_video, name='download_video'),
    path('download_audio/<str:video_id>/', download_audio, name="download_audio"),
    path('about/', about_view, name='about')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
