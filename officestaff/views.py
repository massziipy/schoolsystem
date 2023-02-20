from django.shortcuts import render
from common.models import Registration
from school_admin.models import OfficeStaff

# Create your views here.
def staffhome(request):
    officest=OfficeStaff.objects.get(id=request.session['officestaffid'])
    return render(request,'officestaff/officestaffhome.html',{'data':officest}) 

def enquiries(request):
    enquiries=Registration.objects.all()
    return render(request,'officestaff/enquiries.html',{'data':enquiries})     