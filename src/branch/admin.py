from django.contrib import admin

from .models import BranchInfo

@admin.register(BranchInfo)
class BranchInfoAdmin(admin.ModelAdmin):
    """Register the branch info to admin panel"""
    list_display = ['center_name', 'branch', 'center_code', 'group_code']
    list_filter = ['center_name', 'branch', 'center_code', 'group_code']
