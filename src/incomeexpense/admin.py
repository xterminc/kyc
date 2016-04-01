from django.contrib import admin

from .models import Business, Ornament, OtherAsset, Electronic, Furniture, \
LoanDetail, AssetOnCollateral

admin.site.register(Business)
admin.site.register(Ornament)
admin.site.register(OtherAsset)
admin.site.register(Electronic)
admin.site.register(LoanDetail)
admin.site.register(AssetOnCollateral)
admin.site.register(Furniture)
