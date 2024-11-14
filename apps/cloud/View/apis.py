from rest_framework import generics
from apps.cloud.models import ServiceName, AvailabilityZone
from apps.cloud.serializer.instance import ServiceNameSerializer, AvailabilityZoneSerializer



class ServiceNameListView(generics.ListAPIView):
    queryset = ServiceName.objects.all()
    serializer_class = ServiceNameSerializer

class AvailabilityZoneListAPIView(generics.ListAPIView):
    queryset = AvailabilityZone.objects.all()
    serializer_class = AvailabilityZoneSerializer
