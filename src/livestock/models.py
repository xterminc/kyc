from django.db import models
from core.models import TimeStampedModel
from core.constants import LIVESTOCKS_NAME

class LiveStockDetails(TimeStampedModel):
    livestock_name = models.CharField(max_length=100, choices=LIVESTOCKS_NAME, default='buffaloes')
    livestock_number = models.IntegerField(default=1)
    total_value = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    class Meta:
        verbose_name_plural = "Livestock Details"
    def __str__(self):
        return self.livestock_name
