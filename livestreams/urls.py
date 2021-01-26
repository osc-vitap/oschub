from django.urls import re_path, include
from . import views

app_name = "livestreams"

urlpatterns = [
    re_path(r"^(?P<pk>\d+)/$", views.LiveStreamView.as_view(), name='liveEvents')
]