from django.contrib import admin
from apps.cloud.models import ItemDetails, ItemName, Instance


@admin.register(ItemName)
class ItemNameAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(ItemDetails)
class ItemDetailsAdmin(admin.ModelAdmin):
    fields = ['item', 'storage_type', 'description', 'size', 'size_type', 'price']
    list_display = ['item', 'storage_type', 'description', 'size', 'size_type', 'price']

@admin.register(Instance)
class InstanceAdmin(admin.ModelAdmin):
    fields = ['user', 'item']
    list_display = ['user', 'get_item_name']

    def get_item_name(self, obj):
        return obj.item.item.name if obj.item.item else 'N/A'
    get_item_name.short_description = 'Item Name'




