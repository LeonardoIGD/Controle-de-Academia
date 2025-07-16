from django.contrib import admin

from gym.models import Plan


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'modality', 'duration_months', 'price', 'instructor', 'active']
    list_filter = ['modality', 'duration_months', 'active']
    search_fields = ['name', 'description', 'modality']
    readonly_fields = ['created_at', 'updated_at', 'created_by']
    list_editable = ['active']
    ordering = ['-created_at']

    def has_delete_permission(self, request, obj=None):
        return False
