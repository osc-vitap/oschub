from django.urls import path, re_path, include
from . import views

app_name = "eventreg"


urlpatterns = [
    path('eventList/', views.EventListView.as_view(), name='eventList'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='eventDetails'),
]
