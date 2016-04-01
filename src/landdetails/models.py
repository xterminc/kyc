#landdetails/models.py

from django.db import models
from core.models import TimeStampedModel
from core.constants import LAND_CATEGORY, LAND_MEASUREMENT, CROPS, LAND_TYPE


class Crops(TimeStampedModel):
    crop_name = models.CharField(max_length=100, choices=CROPS, default='wheat')
    production_volume = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    average_income = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    class Meta:
        verbose_name_plural = "Crops"

    def __str__(self):
        return self.crop_name

class LandMeasurement(TimeStampedModel):
    value = models.DecimalField(default=0.0, decimal_places=2, max_digits=12)
    measured_in = models.CharField(max_length=20, choices=LAND_MEASUREMENT, default='ropani')

    def __str__(self):
        return self.quantity

class LandDetails(TimeStampedModel):

    land_category = models.CharField(max_length=255, choices=LAND_CATEGORY, default='farming land')
    land_type = models.CharField(max_length=100, choices=LAND_TYPE, default='others')
    total_value = models.DecimalField(default=0.0, decimal_places=2, max_digits=15)
    land_measurement = models.ForeignKey(LandMeasurement, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Land Details"

    def __str__(self):
        return self.land_category
