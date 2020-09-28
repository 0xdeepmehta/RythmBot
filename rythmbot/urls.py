'''
Divcorn : Day3 | Practical guide 
ulrs.py
'''
from django.contrib import admin
from django.urls import path
from bot.views import (
    yt_video_search_play,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', yt_video_search_play),
]







