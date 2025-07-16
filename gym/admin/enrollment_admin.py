from django.contrib import admin

from gym.models import Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'plan', 'start_date', 'end_date', 'status', 'assigned_by', 'active']
    list_filter = ['status', 'start_date', 'end_date', 'active']
    search_fields = ['student__user__username', 'plan__name', 'assigned_by__user__username']
    readonly_fields = ['created_at', 'updated_at', 'created_by']
    list_editable = ['status', 'active']
    ordering = ['-start_date']

    def has_delete_permission(self, request, obj=None):
        return False
