from django.shortcuts import render,redirect
from common.models import Registration, Login
from school_admin.models import AddStaff, Teachers,Principal,OfficeStaff

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

    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['mail']
        mobile=request.POST['phone']
        dob=request.POST['dob']
        address=request.POST['address']
        preschool=request.POST['prevschool']
        grade=request.POST['grade']
        gender=request.POST['gender']

        reg1=Registration(
            name=name,
            email=email,
            mobile=mobile,
            dob=dob,
            address=address,
            prevschool=preschool,
            grade=grade,
            gender=gender
        )
        reg1.save()





    return render(request,'common/registration.html') 

def login_page(request,user):
    if user=='teacher' or user=='student' or user=='office':
         if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            if user=='teacher':
                try:
                    Auth= Login.objects.get(username=username,password=password)
                    Teacher=Teachers.objects.get(authorize_id=Auth.id)
                    request.session['teacherid']=Teacher.id
                    return redirect("Teacher:tchr")
                except:
                    return render(request,'common/login.html')

            if user=='office':
                try:
                    Auth= Login.objects.get(username=username,password=password)
                    try:
                        Princi=Principal.objects.get(authorize_id=Auth.id)
                        request.session['principalid']=Princi.id
                        return redirect("principal:princi_home")
                    except:
                        officstaff=OfficeStaff.objects.get(authorize_id=Auth.id)
                        request.session['officestaffid']=officstaff.id
                        return redirect("office_staff:staffhome")   
                except:
                    return render(request,'common/login.html')        
                    
                        

    else:
        return redirect('common:usertype')   
    return render(request,'common/login.html') 

def signup_page(request):
    return render(request,'common/signup.html') 

def usertype(request):
    a=['principal','teacher','office']
    print(a[0])
    
    
    return render(request,'common/user_type.html',{'princi':a[0],'teacher':a[1],'office':a[2]})    

def logout(request,user):
    if user=='teacher':
        usertype='teacher'
        del request.session['teacherid']
        request.session.flush()
        return redirect('common:login',usertype)

    if user=='principal':
        usertype='office'
        del request.session['principalid']
        request.session.flush()
        return redirect('common:login',usertype) 

    if user=='officestaff':
        usertype='office'
        del request.session['officestaffid']
        request.session.flush()
        return redirect('common:login',usertype)

                