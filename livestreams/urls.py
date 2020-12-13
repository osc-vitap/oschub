from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.livestreams, name='Live Streaming')
]