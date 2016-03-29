from django.contrib import admin
from .models import PersonalInfo, Education, Training, Passport, DrivingLicense,\
MarriageCertificate, ElectricityBill

admin.site.register(PersonalInfo)
admin.site.register(Education)
admin.site.register(Training)
admin.site.register(Passport)
admin.site.register(DrivingLicense)
admin.site.register(ElectricityBill)
admin.site.register(MarriageCertificate)
