from django.contrib import admin
from .models import Event
from django.contrib.admin.models import LogEntry

class EventAdmin(admin.ModelAdmin):
    list_display = ("session_id", "category", "name", "timestamp", "data")
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    search_fields = [
       "session_id", "category", "name","timestamp"
    ]

admin.site.register(Event, EventAdmin)
