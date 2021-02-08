from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('eventreg/', include('eventreg.urls')),
    path('admin/updateSheet', views.updateSheets, name='updateSheets'),
]
