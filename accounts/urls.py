from django.urls import path, include
from .views import Profile, Login

app_name = "accounts"

urlpatterns = [
    path("profile/", Profile.as_view(), name="profile"),
    path("", Login.as_view(), name="login"),
]
