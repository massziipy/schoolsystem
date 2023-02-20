from django.shortcuts import render
from school_admin.models import Teachers, AddStaff,Classdivision
from Teacher.models import Students
from common.models import Login

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
    return render(request,'Teacher/add_mark.html') 

def progress_card(request):
    return render(request,'Teacher/create_progress_card.html') 

    
def teacher_home_page(request):
    Teacher=Teachers.objects.get(id=request.session['teacherid'])
    return render(request,'Teacher/teacher_home.html',{'data':Teacher}) 