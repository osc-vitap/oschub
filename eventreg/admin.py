from django.contrib import admin
from .models import EventData


class EventAdmin(admin.ModelAdmin):
    search_fields = ['eventName']
    list_display = ['eventName', 'eventDate', 'eventTime', 'eventSpeaker']


admin.site.register(EventData, EventAdmin)
