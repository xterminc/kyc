# core/models.py
from django.db import models
from .constants import DISTRICTS

class TimeStampedModel(models.Model):
    """
    Abstract class to implement created_at and updated_at attributes
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CitizenshipInfo(models.Model):
    """Citizenship Information """

    citizenship_no = models.CharField(max_length=10, unique=True)
    issued_from = models.CharField(max_length=20, choices=DISTRICTS, default='gulmi')
    issued_date = models.DateField()

    class Meta:
        abstract = True


class Passport(models.Model):
    '''Passport model'''

    passport_no = models.CharField(max_length=30, unique=True)
    issued_from = models.CharField(max_length=50, choices=DISTRICTS, default='gulmi')
    issued_date = models.DateField()

    class Meta:
        abstract = True


class DrivingLicense(models.Model):
    '''Person driving license general model'''

    license_no = models.CharField(max_length=20, unique=True)
    issued_from = models.CharField(max_length=30, choices=DISTRICTS, default='gulmi')
    issued_date = models.DateField()

    class Meta:
        abstract = True
