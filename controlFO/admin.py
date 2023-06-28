from django.contrib import admin
from .models import Fields

# Register your models here.

class getFields(admin.ModelAdmin):
    list_display = ('factory_order', 'factory_order_date', 'article_number', 'datasheet', 'datasheet_date', 'etools', 'sticker', 'sticker_date', 'description', 'client')
    search_fields = ('factory_order', 'factory_order_date', 'article_number', 'datasheet', 'datasheet_date', 'etools', 'sticker', 'sticker_date', 'description', 'client')
    list_filter = ('factory_order', 'factory_order_date', 'article_number', 'datasheet', 'datasheet_date', 'etools', 'sticker', 'sticker_date', 'description', 'client',)
    ordering = ['factory_order']

admin.site.register(Fields, getFields)