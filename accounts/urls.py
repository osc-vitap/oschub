from django.urls import path, include
from .views import Profile, SignUp, Login

app_name = "accounts"

urlpatterns = [
    path('profile/', Profile.as_view(), name='profile'),
    path('login/', Login.as_view(), name='login'),
    path('signup/', SignUp.as_view(), name='signup')
]