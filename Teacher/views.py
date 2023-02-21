from django.shortcuts import render,redirect
from school_admin.models import Teachers, AddStaff,Classdivision,Subjects
from Teacher.models import Students,Marks
from common.models import Login
from principal.models import Exams

# Create your views here.


def add_student_page(request):
    classname=Classdivision.objects.all()
    if request.method=='POST':
        studentname=request.POST['name']
        studentemail=request.POST['mail']
        studentmobile=request.POST['mob']
        studentdob=request.POST['dob']
        studentaddress=request.POST['address']
        studentguardian=request.POST['guardian']
        studentphoto=request.FILES['student']
        studentclass=request.POST['grade']
        studentgender=request.POST['gender']

        classdiv=Classdivision.objects.get(id=int(studentclass))


        log=Login.objects.create(
            username=studentemail,
            password=studentmobile,
            usertype='student',
        )

        student=Students.objects.create(
            Studentname=studentname,
            Studentemail=studentemail,
            Studentdob=studentdob,
            Studentmob=studentmobile,
            Studentadress=studentaddress,
            Studentguardian=studentguardian,
            Studentclass_id=classdiv.id,
            Studentimage=studentphoto,
            Student_gender=studentgender,
            authorize=log,
        )







        
    return render(request,'Teacher/add_student.html',{'data':classname}) 

def view_student_page(request):
    return render(request,'Teacher/view_student.html') 

def add_mark_page(request):
    classs=Classdivision.objects.all()
    if request.method=='POST':
        classname=request.POST['classroom']
        classname=int(classname)
        return redirect('Teacher:assignmarks',classname)
    return render(request,'Teacher/add_mark.html',{'data':classs}) 

def progress_card(request):
    return render(request,'Teacher/create_progress_card.html') 

    
def teacher_home_page(request):
    Teacher=Teachers.objects.get(id=request.session['teacherid'])
    return render(request,'Teacher/teacher_home.html',{'data':Teacher}) 


def assignmarks(request,clsid):
    Student=Students.objects.filter(Studentclass_id=clsid)
    Cls=Classdivision.objects.get(id=clsid)
    Exam=Exams.objects.filter(grade_id=Cls.classroom_id)
    Sub=Subjects.objects.filter(classname_id=Cls.classroom_id)
    print(Exam)
    print(Sub)
   
    if request.method=='POST':
        studentss=request.POST['students']
        subject=request.POST['subject']
        exm=request.POST['exam']
        mark=request.POST['marks']

        studentss=int(studentss)
        subject=int(subject)
        exm=int(exm)

        studentdet=Students.objects.get(id=studentss)
        subjectdet=Subjects.objects.get(id=subject)
        examdet=Exams.objects.get(id=exm)

        marks=Marks.objects.create(
            subject_id=subjectdet.id,
            student_id=studentdet.id,
            exam_id=examdet.id,
            Mark=mark,
        )



    return render(request,'Teacher/assignmarks.html',{'data':Student,'subj':Sub,'exm':Exam})     