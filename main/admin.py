from django.contrib import admin
# from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

from .models import Channel

# Register your models here.

class ChannelAdmin(admin.ModelAdmin):
    list_display = ('channel_name', 'health_type', 'health_part', 'video_title', 'video_link', 'video_view_num', 'video_upload_date')


admin.site.register(Channel, ChannelAdmin)

