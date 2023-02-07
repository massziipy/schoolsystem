from django.shortcuts import render

# Create your views here.

def admin_home_page(request):
    return render(request,'school_admin/admin_home.html') 

def add_staff_page(request):
    return render(request,'school_admin/add_staff.html') 


    
def add_class_page(request):
    return render(request,'school_admin/add_class.html') 

def view_staff_page(request):
    return render(request,'school_admin/view_staff.html') 

def view_student_page(request):
    return render(request,'school_admin/view_student.html') 

def salary_page(request):
    return render(request,'school_admin/assign_salary.html') 