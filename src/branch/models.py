from django.db import models
from core.models import TimeStampedModel
from .constants import BRANCHES


class BranchInfo(TimeStampedModel):
    '''Branch Information model'''

    
    branch = models.CharField(max_length=50, choices=BRANCHES, default='baneshwor')
    center_code = models.IntegerField()
    center_name = models.CharField(max_length=100)
    group_code = models.IntegerField()
    member_code = models.IntegerField()


    class Meta:
        ordering = ('center_name',)
        verbose_name = 'Branche'


    def __str__(self):
        return self.center_name
