from rest_framework import serializers
from apps.cloud.models import ServiceName, ServiceDetails, AvailabilityZone

class ServiceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDetails
        fields = ['description', 'size', 'size_type', 'storage_type', 'price']

class ServiceNameSerializer(serializers.ModelSerializer):
    details = ServiceDetailsSerializer(source='servicedetails_set', many=True, read_only=True)

    class Meta:
        model = ServiceName
        fields = ['name', 'details']


class AvailabilityZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailabilityZone
        fields = '__all__'