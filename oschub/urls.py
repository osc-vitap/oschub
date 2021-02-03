from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('accounts.urls')),
        path('accounts/', include('allauth.urls')),
        path('dashboard/', include('dashboard.urls')),
        path('eventreg/', include('eventreg.urls')),
        path('livestream/', include('livestreams.urls')),
        path('admin/updateSheet', views.updateSheets, name='updateSheets'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
