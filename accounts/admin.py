from django.contrib import admin
from .models import ServiceProvider

@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'service', 'phone', 'email', 'status', 'created_at', 'is_active']
    list_filter = ['status', 'service', 'is_active', 'created_at']
    search_fields = ['full_name', 'email', 'phone']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = [
        ('Personal Information', {
            'fields': ('full_name', 'phone', 'email', 'service', 'experience', 'address')
        }),
        ('Documents', {
            'fields': ('profile_picture', 'id_proof')
        }),
        ('Account Status', {
            'fields': ('status', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    ]