from django.contrib import admin
from .models import Speaker


# Register your models here.


class SpeakerAdmin(admin.ModelAdmin):
    search_fields = ["speakerName"]
    list_display = ["speakerName", "speakerProfession"]


admin.site.register(Speaker, SpeakerAdmin)
