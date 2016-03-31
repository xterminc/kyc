from django.db import models
from core.models import TimeStampedModel, CitizenshipInfo, Passport, DrivingLicense
from core.constants import OCCOUPATION, INDUSTRY, RELATION, GENDER, EDUCATION

class SpouseCitizenshipInfo(TimeStampedModel,CitizenshipInfo):
    """Spouce description"""

    citizenship_photo = models.ImageField(upload_to='kycform/family_description/spouce_citizenship_photo')

    def __str__(self):
        return self.citizenship_no


class SpousePassportInfo(TimeStampedModel,Passport):
    """Spouce passport information """

    passport_photo = models.ImageField(upload_to='kycform/family_description/spouce_passport_photo')

    def __str__(self):
        return self.passport_no


class SpouseDrivingLicense(TimeStampedModel,DrivingLicense):
    """Spouce Driving License information model"""

    driving_license_photo = models.ImageField(upload_to='kycform/family_description/spouce_driving_license_photo')

    def __str__(self):
        return self.license_no


class SpouseOccoupation(TimeStampedModel):
    """Spouce occoupation description"""

    name = models.CharField(max_length=100, choices=OCCOUPATION, default='agriculture')
    trading = models.DecimalField(default=0.0, decimal_places=2,max_digits=12)
    industry = models.CharField(max_length=50, choices=INDUSTRY, default='')
    services = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FamilyMemberInfo(TimeStampedModel):
    """Family member info"""

    relation = models.CharField(max_length=20, choices=RELATION, default='father')
    full_name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=6, choices=GENDER)
    main_occupation = models.CharField(max_length=50, choices=OCCOUPATION, default='agriculture')
    education = models.CharField(max_length=100, choices=EDUCATION, default='slc')
    monthly_income = models.DecimalField(default=0.0, decimal_places=2, max_digits=12)
    citizenship_no = models.CharField(max_length=10)
    mobile_no = models.CharField(max_length=10)
    member_in_past = models.CharField(max_length=3, default='no', choices=(
        ('no','No'),
        ('yes', 'Yes'),
        ))

    disease = models.CharField(max_length=3, default='no', choices=(
        ('no','No'),
        ('Yes', 'Yes'),
        ))
