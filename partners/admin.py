from django.contrib import admin
from .models import ServiceProvider


@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):

    list_display = ['full_name', 'service', 'phone', 'email', 'status', 'is_active', 'created_at']
    list_filter = ['status', 'service', 'is_active', 'created_at']
    search_fields = ['full_name', 'email', 'phone', 'service']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = [
        ('Personal Information', {
            'fields': ('full_name', 'phone', 'email', 'service', 'experience', 'address')
        }),
        ('Documents', {
            'fields': ('profile_picture', 'id_proof')
        }),
        ('Approval Status', {
            'fields': ('status', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    ]
    
    actions = ['approve_providers', 'reject_providers']

    def approve_providers(self, request, queryset):
        queryset.update(status='approved', is_active=True)
        self.message_user(request, "Selected providers have been approved.")
    approve_providers.short_description = "Approve selected providers"

    def reject_providers(self, request, queryset):
        queryset.update(status='rejected', is_active=False)
        self.message_user(request, "Selected providers have been rejected.")
    reject_providers.short_description = "Reject selected providers"