from django.contrib import admin
from .models import MailList


# Register your models here.

class MailListAdmin(admin.ModelAdmin):
    search_fields = ['email']
    list_display = ['email']


admin.site.register(MailList, MailListAdmin)
