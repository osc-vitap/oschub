from django.urls import path, include
from . import views

urlpatterns = [
    path('eventsList/', views.EventListView.as_view(), name='eventsList'),
    path('eventDetails/<int:pk>', views.EventDetailView.as_view(), name='eventDetails'),
]
