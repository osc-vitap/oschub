from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(accounts.urls)),
    path('dashboard/', include(dashboard.urls)),
    path('eventreg/', include(eventreg.urls)),
    path('livestream/', include(livestreams.urls)),
]
