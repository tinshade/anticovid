from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('home', views.home, name="homepage"),
    path('facts', views.facts, name="facts"),
    path('news', views.home, name="news"),
]
