from django.urls import path
from . import views
urlpatterns = [
    path('', views.essentials),
    path('askbot', views.askbot, name="askbot"),
]
