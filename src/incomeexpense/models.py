from django.db import models
from core.models import TimeStampedModel
from core.constants import BUSINESS_CATEGORY, VEHICLE_TYPE, ELECTONICE_TYPE,\
LOAN_TYPE

class Business(TimeStampedModel):
    business_category = models.CharField(max_length=40, choices=BUSINESS_CATEGORY, default='agriculture')
    initial_capital = models.DecimalField(max_digits=15, decimal_places=2)
    average_stock = models.DecimalField(max_digits=15, decimal_places=2)
    average_turn_over = models.DecimalField('Average turn over per month', max_digits=15, decimal_places=2)
    doe = models.DateField('Date of Eastblishment')
    vat_no = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Business'

    def __str__(self):
        return self.business_category

class Ornament(TimeStampedModel):
    name = models.CharField(max_length=40)
    total_value = models.DecimalField(max_digits=12,decimal_places=2)

    def __str__(self):
        return self.name


class OtherAsset(TimeStampedModel):
    bank_balance = models.DecimalField(decimal_places=2, max_digits=15)
    ornaments = models.ForeignKey(Ornament, on_delete=models.CASCADE)

    def __str__(self):
        return self.bank_balance


class Vehicle(TimeStampedModel):
    vehicle_type = models.CharField(max_length=40, choices=VEHICLE_TYPE, default='motorcycle')
    total = models.IntegerField(default=1)
    total_value = models.DecimalField(decimal_places=2, max_digits=7)

    def __str__(self):
        return self.vehicle_type



class Electronic(TimeStampedModel):
    electronic_type = models.CharField(max_length=25, choices=ELECTONICE_TYPE, default='mobile')
    total = models.IntegerField(default=1)
    total_value = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.electronic_type


class Furniture(TimeStampedModel):
    furniture_name = models.CharField(max_length=30)
    no_of_item = models.IntegerField(default=1)
    total_value = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.furniture_name


class LoanDetail(TimeStampedModel):
    loan_type = models.CharField(max_length=20, choices=LOAN_TYPE, default='borrow')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    interest = models.DecimalField(max_digits=2, decimal_places=2)
    remaining = models.DecimalField(max_digits=12, decimal_places=2)
    name = models.CharField(max_length=10)


    def __str__(self):
        return self.loan_type


class AssetOnCollateral(TimeStampedModel):
    particular = models.CharField('Particular name', max_length=100)
    total_value = models.DecimalField(decimal_places=2, max_digits=15)

    def __str__(self):
        return self.particular
