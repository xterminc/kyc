from django.shortcuts import render

#importing forms from branch app
from branch.forms import BranchInfoForm

#importing form from livestock app
from livestock.forms import LiveStockDetailForm

def form(request):
    """kyc form view"""
    #branch_info_from
    branch_info_form = BranchInfoForm()
    #livestockform
    livestock_form = LiveStockDetailForm()

    if request.method == 'POST':
        pass
    else:
        return render(request,'kycform/form.html', {'branch_info_form':article_form})
