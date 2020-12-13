from django.urls import path, include
from . import views

urlpatterns = [
    path('/account', views.accounts, name='User Account'),
    path('', views.login, name='Login')
]