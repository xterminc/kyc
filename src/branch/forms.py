from django import forms
from .models import BranchInfo

class BranchInfoForm(forms.ModelForm):

    class Meta:
        model = BranchInfo
        exclude = ('created_at', 'updated_at')
