from django.contrib import admin
from .models import MailList


class MailListAdmin(admin.ModelAdmin):
    search_fields = ["email"]
    list_display = ["email"]


admin.site.register(MailList, MailListAdmin)
