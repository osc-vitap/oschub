from django.urls import path, include
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("speakers/", views.SpeakerView.as_view(), name="speakers"),
    path("about/", views.AboutView.as_view(), name="about"),
]
