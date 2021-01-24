from django.contrib import admin
from .models import EventData, EventUserData


class EventAdmin(admin.ModelAdmin):
    search_fields = ['eventName']
    list_display = ['eventName', 'eventDate', 'eventStartTime', 'eventEndTime', 'eventSpeaker']


class EventDataAdmin(admin.ModelAdmin):
    search_fields = ['eventName', 'studentName', 'studentReg', 'studentEmail']
    list_display = ['eventName', 'studentReg', 'studentName']


admin.site.register(EventData, EventAdmin)
admin.site.register(EventUserData, EventDataAdmin)
