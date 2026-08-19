from django.contrib import admin
from .models import Project, Skill, ContactMessage, SiteInfo


@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ["location", "currently_learning"]

    def has_add_permission(self, request):
        # Only one row should ever exist
        return not SiteInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "featured", "order", "created_at"]
    list_editable = ["featured", "order"]
    list_filter = ["featured"]
    search_fields = ["name", "description", "tags"]
    ordering = ["order"]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "level", "percent", "order"]
    list_editable = ["level", "percent", "order"]
    list_filter = ["level"]
    search_fields = ["name"]
    ordering = ["order"]


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "created_at", "is_read"]
    list_editable = ["is_read"]
    list_filter = ["is_read", "created_at"]
    search_fields = ["name", "email", "message"]
    readonly_fields = ["name", "email", "message", "created_at"]
    actions = ["mark_as_read", "mark_as_unread"]

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected as read"

    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "Mark selected as unread"
