from django.shortcuts import render

# Create your views here.

def modify_teacher_page(request):
    return render(request,'principal/modify_teacher.html') 

def view_teacher_page(request):
    return render(request,'principal/view_teacher.html') 

def view_student_page(request):
    return render(request,'principal/view_student.html')

def principal_home_page(request):
    return render(request,'principal/principal_home.html')

def edit_details_page(request):
    return render(request,'principal/edit_details.html')

def class_teacher_page(request):
    return render(request,'principal/assign_class_teacher.html')