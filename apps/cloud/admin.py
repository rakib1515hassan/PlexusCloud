from django.contrib import admin
from apps.cloud.models import ServiceDetails, ServiceName, Instance, AvailabilityZone

# Inline for showing related Instances within ServiceDetailsAdmin
class InstanceInline(admin.TabularInline):
    model = Instance
    extra = 1  # Number of empty forms to display

@admin.register(ServiceName)
class ServiceNameAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(ServiceDetails)
class ServiceDetailsAdmin(admin.ModelAdmin):
    fields = ['service', 'storage_type', 'description', 'size', 'size_type', 'price']
    list_display = ['service', 'storage_type', 'description', 'size', 'size_type', 'price']
    # inlines = [InstanceInline]  # Display related Instances inline in ServiceDetails

@admin.register(Instance)
class InstanceAdmin(admin.ModelAdmin):
    fields = ['user', 'project_name', 'name']
    list_display = ['user', 'project_name']




admin.site.register(AvailabilityZone)
