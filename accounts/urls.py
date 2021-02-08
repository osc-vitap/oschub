from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
]