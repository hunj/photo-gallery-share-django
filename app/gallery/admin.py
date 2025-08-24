from django.contrib import admin
from .models import Album, Photo


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created_at', 'is_public', 'get_photo_count']
    list_filter = ['is_public', 'created_at', 'owner']
    search_fields = ['title', 'description', 'owner__username', 'owner__email']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
    
    def get_photo_count(self, obj):
        return obj.get_photo_count()
    get_photo_count.short_description = 'Photo Count'


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'album', 'uploaded_at', 'is_public']
    list_filter = ['is_public', 'uploaded_at', 'owner', 'album']
    search_fields = ['title', 'description', 'owner__username', 'owner__email', 'album__title']
    readonly_fields = ['uploaded_at', 'updated_at']
    date_hierarchy = 'uploaded_at'
    list_select_related = ['owner', 'album']
