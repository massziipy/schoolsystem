from django.shortcuts import render,redirect
from common.models import Registration
from school_admin.models import OfficeStaff,Classdivision,Classroom,Fees
from Teacher.models import Studentfees, Students


# Create your views here.
def staffhome(request):
    officest=OfficeStaff.objects.get(id=request.session['officestaffid'])
    return render(request,'officestaff/officestaffhome.html',{'data':officest}) 

def enquiries(request):
    enquiries=Registration.objects.all()
    return render(request,'officestaff/enquiries.html',{'data':enquiries})   

def sendpaymentreq(request):
    classs=Classdivision.objects.all()
    if request.method=='POST':
        classname=request.POST['classroom']
        classname=int(classname)
        return redirect('office_staff:assignfees',classname)
    return render(request,'officestaff/sendpaymentrequest.html',{'data':classs})  

def assignfees(request,clsid):
    Student=Students.objects.filter(Studentclass_id=clsid)
    Cls=Classdivision.objects.get(id=clsid)
    fees=Fees.objects.filter(classname_id=Cls.classroom_id)

    if request.method=='POST':
        feees=request.POST['fees']
        student=request.POST['students']

        feees=int(feees)
        student=int(student)

        stud=Students.objects.get(id=student)
        fee=Fees.objects.get(id=feees)

        Addfees=Studentfees.objects.create(
            student_id=stud.id,
            fees_id=fee.id,
            status='not_paid',
        )
   



    return render(request,'officestaff/feesassign.html',{'data':Student,'feesdata':fees})       