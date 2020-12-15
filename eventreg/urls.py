from django.urls import path, include
from . import views

urlpatterns = [
    path('eventsList/', views.eventsList, name='eventsList'),
    path('eventDetails/', views.eventDetails, name='eventDetails')
]