from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ("session", "category", "name", "timestamp", "data")


admin.site.register(Event, EventAdmin)
