from __future__ import unicode_literals
from django.db import models
from core.models import TimeStampedModel, CitizenshipInfo, Passport, DrivingLicense
from address.models import PermanentAddress, TemporaryAddress, MaitiAddress
from core.constants import DISTRICTS, FAMILY_TYPE, GENDER, EDUCATION
from .constants import RELATION,MARTIAL_STATUS,RELIGION,ETHINIC_GROUP,\
CASTE,NATIONALITY,FININCIAL_INSTITUTIONS
from branch.models import BranchInfo
from familydescription.models import SpouseOccoupation, SpousePassportInfo, SpousePassportInfo,\
SpouseDrivingLicense, SpouseCitizenshipInfo, FamilyMemberInfo

from landdetails.models import LandDetails


class CitizenshipInfo(TimeStampedModel, CitizenshipInfo):
    """Citizenship Information """

    citizenship_photo = models.ImageField(upload_to='kycform/citizenship_info/citizenship_photo')

    def __str__(self):
        return self.citizenship_no


class Education(TimeStampedModel):
    '''models for the education '''

    TECHINICAL = (
        ('engineering', 'ME/MSC/'),
    )
    general = models.CharField(max_length=15, choices=EDUCATION, default='slc' )
    technical = models.CharField(max_length=15, choices=TECHINICAL, default='engineering')

    def __str__(self):
        return self.general


class Training(TimeStampedModel):
    '''Person training info model'''

    institue_name = models.CharField(max_length=100)
    training_name = models.CharField(max_length=255)
    duration = models.IntegerField(default=30)
    certificate = models.ImageField(upload_to='kycform/training/certificate')

    def __str__(self):
        return self.training_name

class Passport(TimeStampedModel, Passport):
    '''person passport model info'''

    passport_photo = models.ImageField(upload_to='kycform/passport/passport_photo')

    def __str__(self):
        return self.passport_no

class DrivingLicense(TimeStampedModel, DrivingLicense):
    '''Person driving info model'''

    license_photo = models.ImageField(upload_to='kycform/drivinglicense/license_photo/')

    def __str__(self):
        return self.license_no

class MarriageCertificate(TimeStampedModel):
    '''Person marriage certificate info'''

    registration_no = models.CharField(max_length=30)
    issued_from = models.CharField(max_length=30, choices=DISTRICTS, default='gulmi')
    issued_date = models.DateField()
    marriage_certificate_photo = models.ImageField(upload_to='kycform/marriage_certificate/marriage_certificate_photo')

    def __str__(self):
        return self.registration_no


class ElectricityBill(TimeStampedModel):
    '''Person electricitybill info'''

    bill_no = models.CharField(max_length=50)
    issued_from = models.CharField(max_length=50, choices=DISTRICTS, default='gulmi')
    issued_date = models.DateField()
    bill_photo = models.ImageField(upload_to='kycform/electricitybill/bill_photo')

    def __str__(self):
        return self.bill_no



class PersonalInfo(TimeStampedModel):
    '''Customer Personal Information'''

    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    husband_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    father_in_law_name = models.CharField(max_length=100, blank=True)
    grand_father_in_law_name = models.CharField(max_length=100)
    nominee_name = models.CharField(max_length=100)
    nominee_relation = models.CharField(max_length=7, choices=RELATION, default='husband')
    dob = models.DateField(auto_now=True, auto_now_add=False)
    age = models.IntegerField()
    gender = models.CharField(max_length=6, choices=GENDER, default='female')
    marital_status = models.CharField(max_length=9, choices=MARTIAL_STATUS, default='married')
    religion = models.CharField(max_length=10, choices=RELIGION, default='hindu')
    ethnic_group = models.CharField(max_length=20, choices=ETHINIC_GROUP, default='Brahmin')
    caste = models.CharField(max_length=20, choices=CASTE, default='brahmin')
    nationality = models.CharField(max_length=20, choices=NATIONALITY, default='nepali')
    email = models.EmailField(blank=True)
    finger_print = models.ImageField(upload_to='kycform/personal_info/finger_print')
    signature = models.ImageField(upload_to='kycform/personal_info/signature')
    medication = models.BooleanField()
    childrens = models.IntegerField(default=0)
    boys = models.IntegerField(default=0)
    girls = models.IntegerField(default=0)
    other_banks = models.CharField(max_length=50, choices=FININCIAL_INSTITUTIONS, default='bank')
    family_type = models.CharField(max_length=7, choices=FAMILY_TYPE, default='joint')
    branch = models.ForeignKey(BranchInfo, on_delete=models.CASCADE)
    citizenship_no = models.ForeignKey(CitizenshipInfo, on_delete=models.CASCADE)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    passport = models.ForeignKey(Passport, on_delete=models.CASCADE)
    driving_license = models.ForeignKey(DrivingLicense, on_delete=models.CASCADE)
    marriage_certificate = models.ForeignKey(MarriageCertificate, on_delete=models.CASCADE)
    electricity_bill = models.ForeignKey(ElectricityBill, on_delete=models.CASCADE,related_name='kycform_personalinfos')
    permanent_address = models.ForeignKey(PermanentAddress, on_delete=models.CASCADE)
    temporary_address = models.ForeignKey(TemporaryAddress, on_delete=models.CASCADE)
    maiti_address = models.ForeignKey(MaitiAddress, on_delete=models.CASCADE)
    spouse_citizenship_info = models.ForeignKey(SpouseCitizenshipInfo, on_delete=models.CASCADE)
    spouse_driving_license = models.ForeignKey(SpouseDrivingLicense, on_delete=models.CASCADE)
    spouse_passport_info = models.ForeignKey(SpousePassportInfo, on_delete=models.CASCADE)
    spouse_occupation = models.ForeignKey(SpouseOccoupation, on_delete=models.CASCADE)
    family_member_info = models.ForeignKey(FamilyMemberInfo, on_delete=models.CASCADE)
    land_details = models.ForeignKey(LandDetails, on_delete=models.CASCADE)



    class Meta:
        ordering = ('first_name', )

    def __str__(self):
        return self.first_name + self.last_name
