from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home),
    path('home', views.home, name="homepage"),
    path('facts', views.facts, name="facts"),
    path('news', views.news, name="news"),
    path('feedbacks', views.feedbacks, name="feedbacks"),
    path('askbot', views.askbot, name="askbot"),
    #path('askbot', include('talker.urls'), name="askbot"),
]
