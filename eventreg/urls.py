from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.EventListView.as_view(), name='eventList'),
    path('eventDetails/<int:pk>', views.EventDetailView.as_view(), name='eventDetails'),
]
