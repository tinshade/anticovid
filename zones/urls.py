from django.urls import path
from . import views
urlpatterns = [
    path('', views.zones),
    path('askbot', views.askbot, name="askbot"),
]