from django.shortcuts import render

# Create your views here.


def add_student_page(request):
    return render(request,'Teacher/add_student.html') 

def view_student_page(request):
    return render(request,'Teacher/view_student.html') 

def add_mark_page(request):
    return render(request,'Teacher/add_mark.html') 

def progress_card(request):
    return render(request,'Teacher/create_progress_card.html') 

    
def teacher_home_page(request):
    return render(request,'Teacher/teacher_home.html') 