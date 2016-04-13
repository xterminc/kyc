from django.forms import ModelForm
from django import forms
from .models import PersonalInfo, CitizenshipInfo, Education


class PersonalInfoForm(ModelForm):

    class Meta:
        model = PersonalInfo
        exclude = ('created_at', 'updated_at',)
        widgets = {
            'dob' : forms.DateInput(attrs={'type':'date'})
        }


class CitizenshipInfoForm(ModelForm):
    class Meta:
        model = CitizenshipInfo
        exclude = ('created_at', 'updated_at',)
        widgets = {
        'issued_date' : forms.DateInput(attrs={'type':'date'})
        }

class EducationForm(ModelForm):
    class Meta:
        model = Education
        exclude = ('created_at', 'updated_at',)
