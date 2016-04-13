from django.shortcuts import render
from django.utils import timezone

#importing forms from branch app
from branch.forms import BranchInfoForm

#importing forms from kycform app, it contains personal info form
from .forms import PersonalInfoForm, CitizenshipInfoForm, EducationForm

#importing form from livestock app
from livestock.forms import LiveStockDetailForm

#family description form app
from familydescription.forms import SpouseCitizenshipInfoForm, SpousePassportInfoForm,\
SpouseDrivingLicenseForm, SpouseOccoupationForm,  FamilyMemberInfoForm

def form(request):
    """kyc form view"""
    #forms dict that hold collection of forms to the view
    forms = {}
    #branch_info_from
    forms['branch_info_form'] = BranchInfoForm(prefix='branch_info_form')

    #livestockform
    forms['livestock_form'] = LiveStockDetailForm(prefix='livestock_form')

    #family description
    forms['spouse_citizenship_info_form'] = SpouseCitizenshipInfoForm(prefix='spouse_citizenship_info_form')
    forms['spouse_passport_info_form'] = SpousePassportInfoForm(prefix='spouse_passport_info_form')
    forms['spouse_driving_license_form'] = SpouseDrivingLicenseForm(prefix='spouse_driving_license_form')
    forms['spouse_occupation_form'] = SpouseOccoupationForm(prefix='spouse_occupation_form')
    forms['family_member_info_form'] = FamilyMemberInfoForm(prefix='family_member_info_form')

    #personal info form,
    forms['citizenship_info_form'] = CitizenshipInfoForm(prefix='citizenship_info_form')
    forms['education_form'] = EducationForm(prefix='education_form')
    forms['personal_info_form'] = PersonalInfoForm(prefix='personal_info_form')


    if request.method == 'POST':
        #branch info app form
        branch_info_form = BranchInfoForm(request.POST,prefix='branchinfo')

        #live stock app form
        livestock_form = LiveStockDetailForm(request.POST,prefix='livestock')

        #family description app form
        spouse_citizenship_info_form = SpouseCitizenshipInfoForm(request.POST, prefix='spousecitizen')
        spouse_passport_info_form = SpousePassportInfoForm(request.POST, prefix='spousepassport')
        spouse_driving_license_form = SpouseDrivingLicenseForm(request.POST, prefix='spousedrivinglicense')
        spouse_occupation_form = SpouseOccoupationForm(request.POST, prefix='spouseoccupation')
        family_member_info_form = FamilyMemberInfoForm(request.POST, prefix='familymember')

        #personal info form
        citizenship_info_form = CitizenshipInfoForm(request.POST, prefix='citizenshipinfo')
        education_form = EducationForm(request.POST,prefix='education_form')
        personal_info_form = PersonalInfoForm(request.POST, prefix='perosnalinfo')


        if branch_info_form.is_valid() and personal_info_form.is_valid():
            #Save branch_info form  to the database
            branch_info = branch_info_form.save(commit=False)
            branch_info.updated_at = timezone.now()
            branch_info = branch_info.save()


        else:
            #resend branch_info_form
            forms['branch_info_form'] = branch_info_form
            #resend personal info form
            forms['citizenship_info_form'] = spouse_citizenship_info_form
            forms['education_form'] = education_form
            forms['personal_info_form'] = personal_info_form
            #resend livestock form
            forms['livestock_form'] = livestock_form

            return render(request,'kycform/form.html', forms)

    else:
        return render(request,'kycform/form.html', forms)
