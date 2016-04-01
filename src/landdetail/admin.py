from django.contrib import admin

from .models import LandDetail, Crop, LandMeasurement

admin.site.register(LandDetail)
admin.site.register(Crop)
admin.site.register(LandMeasurement)
