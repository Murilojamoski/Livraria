from django.contrib import admin
from uploader.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['attachment_key', 'criado_em']
    search_fields = ['attachment_key']
    readonly_fields = ['criado_em']
