from django.contrib import admin

from .models import LandDetails, Crops, LandMeasurement

admin.site.register(LandDetails)
admin.site.register(Crops)
admin.site.register(LandMeasurement)
