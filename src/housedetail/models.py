from django.db import models
from core.models import TimeStampedModel
from core.constants import HOUSE_TYPE, MATERIAL_TYPE, ROOF_TYPE

class HouseDetail(TimeStampedModel):
    """House detail"""

    house_type = models.CharField(max_length=20, choices=HOUSE_TYPE, default='kachi')
    no_of_houses = models.IntegerField(default=0)
    house_covered_area = models.DecimalField('Covered Area in km', max_digits=10, decimal_places=2 )
    roof_of_house = models.CharField('Roof type', choices=ROOF_TYPE, default='tile', max_length=20)
    no_of_rooms = models.IntegerField()
    material_used = models.CharField(max_length=20, choices=MATERIAL_TYPE, default='brick')
    total_value = models.DecimalField(max_digits=10, decimal_places=2)


    class Meta:
        verbose_name_plural = 'House Details'

    def __str__(self):
        return self.house_type
