from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

from apps.core.models import TimestampedModel

# Create your models here.
class ItemName(TimestampedModel):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class ItemDetails(TimestampedModel):
    class sizeType(models.TextChoices):
        MB = 'Mb', 'mb'
        GB = 'Gb', 'gb'
        TB = 'Tb', 'tb'
    
    class storageType(models.TextChoices):
        SSD  = 'SSD',  'ssd'
        HDD  = 'HDD',  'hdd'
        NVME = 'NVME', 'nvme'

    item = models.ForeignKey(ItemName, on_delete=models.CASCADE)

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




class Instance(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(ItemDetails, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.name if self.user.name else ''} : {self.item.item.name}"


