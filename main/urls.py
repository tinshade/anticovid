from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('home', views.home, name="homepage"),
    path('facts', views.facts, name="facts"),
    path('news', views.news, name="news"),
    path('feedbacks', views.feedbacks, name="feedbacks"),
]
