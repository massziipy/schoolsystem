from django.shortcuts import render
from school_admin.models import Principal,Teachers,Classdivision

# Create your views here.

def modify_teacher_page(request):
    return render(request,'principal/modify_teacher.html') 

def view_teacher_page(request):
    teacher= Teachers.objects.all()
    classs=Classdivision.objects.all()

    return render(request,'principal/view_teacher.html',{'data':teacher,'class':classs}) 

def view_student_page(request):
    return render(request,'principal/view_student.html')

def principal_home_page(request):
    princi=Principal.objects.get(id=request.session['principalid'])
    return render(request,'principal/principal_home.html',{'data':princi})

def edit_details_page(request):
    return render(request,'principal/edit_details.html')

def class_teacher_page(request):
    tchr=Teachers.objects.all()
    cls=Classdivision.objects.all()
    if request.method=='POST':
        print('hkhi')
        classname=request.POST['class']
        teachr=request.POST['teacher']
        classs=Classdivision.objects.get(id=int(classname))
        teach=Teachers.objects.get(id=int(teachr))
        classs.teacher_id=teach.id
        classs.save()
    return render(request,'principal/assign_class_teacher.html',{'class':cls,'teacher':tchr})