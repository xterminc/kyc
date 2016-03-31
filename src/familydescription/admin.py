from django.contrib import admin

from .models import SpouseCitizenshipInfo, SpousePassportInfo, SpouseDrivingLicense,\
SpouseOccoupation, FamilyMemberInfo

admin.site.register(SpouseCitizenshipInfo)
admin.site.register(SpousePassportInfo)
admin.site.register(SpouseDrivingLicense)
admin.site.register(SpouseOccoupation)
admin.site.register(FamilyMemberInfo)
