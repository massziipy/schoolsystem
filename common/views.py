from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request,'common/home.html') 

def about_page(request):
    return render(request,'common/about.html') 

def contact_page(request):
    return render(request,'common/contact.html') 


def admission_page(request):
    return render(request,'common/admission.html') 

def registration_form(request):
    return render(request,'common/registration.html') 

def login_page(request):
    return render(request,'common/login.html') 

def signup_page(request):
    return render(request,'common/signup.html') 