from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User, StudentProfile, InstructorProfile


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'is_student', 'is_instructor', 'is_staff')
    list_filter = ('is_student', 'is_instructor', 'is_staff')
    search_fields = ('username', 'email')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Informações Pessoais', {'fields': ('phone',)}),
        ('Permissões', {'fields': ('is_student', 'is_instructor', 'is_active', 'is_staff', 'is_superuser')}),
        ('Datas Importantes', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )

    readonly_fields = ('created_at', 'updated_at')

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'height', 'weight')
    search_fields = ('user__username', 'user__email')

@admin.register(InstructorProfile)
class InstructorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'experience_years', 'is_available')
    search_fields = ('user__username', 'specialization')

admin.site.register(User, CustomUserAdmin)