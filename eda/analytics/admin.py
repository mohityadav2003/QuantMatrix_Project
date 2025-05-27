from django.contrib import admin
from .models import RetailData

@admin.register(RetailData)
class RetailDataAdmin(admin.ModelAdmin):
    list_display = ('Brand', 'Year', 'Month', 'SalesValue', 'Volume', 'Channel', 'Region')
    search_fields = ('Brand', 'PPG', 'Channel', 'Region')
    list_filter = ('Year', 'Brand', 'Channel', 'PackType')
