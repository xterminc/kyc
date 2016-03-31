from django.contrib import admin

from .models import PermanentAddress, TemporaryAddress, MaitiAddress

admin.site.register(PermanentAddress)
admin.site.register(TemporaryAddress)
admin.site.register(MaitiAddress)
