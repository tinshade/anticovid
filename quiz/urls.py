from django.urls import path
from . import views
urlpatterns = [
    path('', views.quiz),
    path('mq', views.mq)
]
