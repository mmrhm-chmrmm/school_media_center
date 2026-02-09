from django.contrib import admin
from .models import Post, Photo, GalleryFolder, Video


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'updated_at')
    search_fields = ('title', 'text', 'author__username')
    list_filter = ('updated_at',)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'folder', 'file')
    list_filter = ('folder',)


@admin.register(GalleryFolder)
class GalleryFolderAdmin(admin.ModelAdmin):
    list_display = ('id', 'folder_name')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'video_name', 'video_url')
