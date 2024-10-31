from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

from apps.core.models import TimestampedModel

# Create your models here.
class ServiceName(TimestampedModel):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class ServiceDetails(TimestampedModel):
    class sizeType(models.TextChoices):
        MB = 'Mb', 'mb'
        GB = 'Gb', 'gb'
        TB = 'Tb', 'tb'
    
    class storageType(models.TextChoices):
        SSD  = 'SSD',  'ssd'
        HDD  = 'HDD',  'hdd'
        NVME = 'NVME', 'nvme'

    service = models.ForeignKey(ServiceName, on_delete=models.CASCADE)

    description = models.CharField(max_length=225, null=True, blank=True)
    size = models.FloatField(null=True, blank=True)
    size_type = models.CharField(
                    verbose_name="Size Type", 
                    max_length=10, 
                    choices=sizeType.choices, 
                    null=True, blank=True
                )
    storage_type = models.CharField(
                    verbose_name="Storage Type", 
                    max_length=10, 
                    choices=storageType.choices, 
                    null=True, blank=True
                )
    price = models.FloatField()

    def __str__(self):
        return self.service.name


class AvailabilityZone(TimestampedModel):
    name = models.CharField(max_length=225)
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return self.name

    
class Instance(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=225)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    zone = models.ForeignKey(AvailabilityZone, on_delete=models.CASCADE)
    service = models.ForeignKey(ServiceName, on_delete=models.CASCADE)
    service_details = models.ForeignKey(ServiceDetails, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name if self.user.name else ''} : {self.service.service.name}"

    


