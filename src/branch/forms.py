from django import forms
from .models import BranchInfo

class BranchInfoForm(forms.ModelForm):

    class Meta:
        model = BranchInfo
        fields = ['branch', 'center_code', 'center_name', 'group_code', 'member_code']
