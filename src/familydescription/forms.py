from django.forms import ModelForm
from .models import SpouseCitizenshipInfo, SpousePassportInfo, SpouseDrivingLicense,\
SpouseOccoupation, FamilyMemberInfo

class SpouseCitizenshipInfoForm(ModelForm):
    """spouse citizenship form """

    class Meta:
        model = SpouseCitizenshipInfo
        exclude = ('created_at', 'updated_at',)


class SpousePassportInfoForm(ModelForm):


    class Meta:
        model = SpousePassportInfo
        exclude = ('created_at', 'updated_at',)


class SpouseDrivingLicenseForm(ModelForm):
    """Spouse dirving license form """

    class Meta:
        model = SpouseDrivingLicense
        exclude = ('created_at', 'updated_at',)

class SpouseOccoupationForm(ModelForm):
    """Spouse occupation form """

    class Meta:
        model = SpouseOccoupation
        exclude = ('created_at', 'updated_at',)

class FamilyMemberInfoForm(ModelForm):
    """Family member information form"""

    class Meta:
        model = FamilyMemberInfo
        exclude = ('created_at', 'updated_at',)
