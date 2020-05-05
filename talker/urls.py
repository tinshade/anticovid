from django.urls import path
from . import views
urlpatterns = [
    path('', views.talker),
    path('bot', views.bot),
]
