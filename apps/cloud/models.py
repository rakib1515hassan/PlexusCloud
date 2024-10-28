from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

from apps.core.models import TimestampedModel

# Create your models here.
class ItemName(TimestampedModel):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class ItemSize(TimestampedModel):
    class sizeType(models.TextChoices):
        MB = 'Mb', 'mb'
        GB = 'Gb', 'gb'
        TB = 'Tb', 'tb'
    
    class storageType(models.TextChoices):
        SSD  = 'SSD',  'ssd'
        HDD  = 'HDD',  'hdd'
        NVME = 'NVME', 'nvme'

    size = models.FloatField()
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


class Item(TimestampedModel):
    item = models.ForeignKey(ItemName, on_delete=models.CASCADE)
    details = models.OneToOneField(ItemSize, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.name if self.item.name else ''


class Instance(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ManyToManyField(Item)
    
    def __str__(self):
        return self.user.name if self.user.name else ''

# class Configaration(TimestampedModel):
#     instance = models.ForeignKey(Instance, on_delete=models.CASCADE)
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)