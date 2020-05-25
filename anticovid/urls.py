from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'), name="homepage"),
    path('main/', include('main.urls'), name="homepage"),
    path('main/home', include('main.urls'), name="homepage"),
    path('main/news', include('main.urls'), name="news"),
    path('main/getnews', include('main.urls'), name="getnews"),
    path('main/facts', include('main.urls'), name="facts"),
    path('social/', include('social.urls'), name="social"),
    path('essentials/', include('essentials.urls'), name="essentials"),
    path('quiz/', include('quiz.urls'), name="quiz"),
    path('talker/', include('talker.urls'), name="talker"),
    path('zones/', include('zones.urls'), name="zones"),
]