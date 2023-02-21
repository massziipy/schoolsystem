from django.shortcuts import render
from school_admin.models import Classroom,Classdivision
from Teacher.models import Marks,Students,Studentfees
from principal.models import Exams

# Create your views here.


def student_home_page(request):
    return render(request,'student/student_home.html') 

def pay_fee_page(request):
    Studfees=Studentfees.objects.filter(student_id=request.session['studentid'])

    return render(request,'student/pay_fees.html',{'data':Studfees}) 

def changefeesstatus(request,feeid):
    Studfees=Studentfees.objects.filter(student_id=request.session['studentid'])
    stud=Studentfees.objects.get(id=feeid)
    stud.status='paid'
    stud.save()
    return render(request,'student/pay_fees.html',{'data':Studfees}) 


def selectexam(request):
    stud=Students.objects.get(id=request.session['studentid'])
    classs=Classdivision.objects.get(id=stud.Studentclass_id)
    grade=Classroom.objects.get(id=classs.id)
    exam=Exams.objects.filter(grade_id=grade.id)
    return render(request,'student/selectexam.html',{'data':exam})     

def view_report_card_page(request,eid):
    no=0
    totalmarks=0
    status=''
    grade=''
    
    student=Students.objects.get(id=request.session['studentid'])
    mark=Marks.objects.filter(student_id=request.session['studentid'],exam_id=eid)
    for marks in mark:
        if marks.Mark<50:
            status='Fail'
            break
        else:
            status='Pass'

    for marks in mark:
        no=no+1
        totalmarks=totalmarks+marks.Mark
    
    try:
        avg=int(totalmarks/no)
        print(avg)
    except:avg=0       

    if avg >= 90:
        grade='A'
    elif avg>80 and avg<=89:
        grade='B'    
    elif avg>70 and avg<=79:
        grade='C'    
    elif avg>60 and avg<=69:
        grade='D' 
    elif avg>50 and avg<=59:
        grade='E' 
    else:
        grade='F'        




                
            

    return render(request,'student/view_report_card.html',{'score':mark,'stat':status,'total':totalmarks,'grad':grade,'student':student}) 

