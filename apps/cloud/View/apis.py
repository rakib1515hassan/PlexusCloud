from rest_framework import generics
from apps.cloud.models import ServiceName
from apps.cloud.serializer.instance import ServiceNameSerializer



class ServiceNameListView(generics.ListAPIView):
    queryset = ServiceName.objects.all()
    serializer_class = ServiceNameSerializer
