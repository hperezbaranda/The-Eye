from re import M
from django.contrib import admin
from .models import Event, DataEvent


class EventAdmin(admin.ModelAdmin):
    list_display = ("session", "category", "name", "timestamp",)


admin.site.register(Event, EventAdmin)
admin.site.register(DataEvent)
