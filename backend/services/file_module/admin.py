from django.contrib import admin
from services.file_module.models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'object_id', 'content_type']
    search_fields = ['id', 'object_id', 'content_type']
