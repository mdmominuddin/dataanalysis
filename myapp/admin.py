# admin.py

from django.contrib import admin
from .models import Dataset, Visualization, DataPoint

@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'upload_date')
    list_filter = ('user', 'upload_date')
    search_fields = ('name', 'user__username')  # Search by dataset name and user username

@admin.register(Visualization)
class VisualizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('name', 'user__username')  # Search by visualization name and user username

@admin.register(DataPoint)
class DataPointAdmin(admin.ModelAdmin):
    list_display = ('get_data_display', 'visualization')
    list_filter = ('visualization__name',)  # Filter by visualization name
    search_fields = ('data', 'visualization__name')  # Search by data and visualization name

    def get_data_display(self, obj):
        return str(obj.data)
    get_data_display.short_description = 'Data'
