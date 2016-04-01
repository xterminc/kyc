from django.db import models
from core.models import TimeStampedModel
from core.constants import ZONES, DISTRICTS


class Address(TimeStampedModel):
    zone = models.CharField(max_length=100, choices=ZONES, default="Lumbini")
    district = models.CharField(max_length=100, choices=DISTRICTS, default="gulmi")
    vdc = models.CharField(max_length=100)
    ward_no = models.IntegerField(default=1)
    house_no = models.IntegerField(default=0)
    street = models.CharField(max_length=100)
    tel_no = models.IntegerField()
    pobox_no = models.IntegerField()

    class Meta:
        abstract = True


class PermanentAddress(Address):

    def __str__(self):
        return self.ZONES

class TemporaryAddress(Address):

    def __str__(self):
        return self.zone

class MaitiAddress(Address):

    def __str__(self):
        return self.zone
