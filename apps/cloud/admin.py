from django.contrib import admin
from apps.cloud.models import ItemSize, ItemName, Item, Instance

admin.site.register(ItemName)
admin.site.register(ItemSize)
admin.site.register(Item)
admin.site.register(Instance)

# class ItemSizeInline(admin.StackedInline):
#     model = ItemSize
#     fields = ['size', 'size_type', 'storage_type', 'price']
#     extra = 1  # Only 1 inline form to show

#     # Make sure size and price fields are required
#     def get_formset(self, request, obj=None, **kwargs):
#         formset = super().get_formset(request, obj, **kwargs)
#         for form in formset.forms:
#             form.fields['size'].required = True
#             form.fields['price'].required = True
#         return formset
    

# @admin.register(ItemName)
# class ItemNameAdmin(admin.ModelAdmin):
#     list_display = ['name']


# @admin.register(Item)
# class ItemAdmin(admin.ModelAdmin):
#     inlines = [ItemSizeInline]
#     list_display = ['get_item_name']

#     # Custom display function for ItemName's name field
#     def get_item_name(self, obj):
#         return obj.item.name
#     get_item_name.short_description = 'Item Name'  # Display name in the admin header
