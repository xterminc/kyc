# core/models.py
from django.db import models
from datetime import datetime
class TimeStampedModel(models.Model):
    """
    Abstract class to implement created_at and updated_at attributes
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
