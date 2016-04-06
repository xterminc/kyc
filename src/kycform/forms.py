from django.forms import ModelForm
from .models import PersonalInfo

class PersonlInfoForm(ModelForm):

    class Meta:
        model = PersonalInfo
        exclude = ('created_at', 'updated_at')
