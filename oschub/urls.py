from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [path('admin/', admin.site.urls), path('', include('accounts.urls')),
               path('accounts/', include('allauth.urls')), path('dashboard/', include('dashboard.urls')),
               path('eventreg/', include('eventreg.urls')), path('livestream/', include('livestreams.urls')),
               path('admin', views.updateSheets, name='updateSheets')]
