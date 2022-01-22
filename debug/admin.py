from django.contrib import admin

from debug.models import Log

class LogAdmin(admin.ModelAdmin):
    list_display = ('timestamp','level', 'view', 'exceptionclass',
                    'message')
    list_filter = ('level', 'view', 'timestamp')
    search_fields = ['message', 'exceptionclass', 'view']

    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

 
admin.site.register(Log, LogAdmin)

