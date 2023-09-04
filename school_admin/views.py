from django.shortcuts import render
from .models import Teachers,Login,AddStaff,OfficeStaff,Principal,Salary,Classroom,Classdivision,Subjects,Fees
from Teacher.models import Studentfees
from django.http import JsonResponse

# Create your views here.

def admin_home_page(request):

    # up=Login.objects.create(username='admin',password='1234',usertype='admin')
    # up=Studentfees.objects.all()
   
    # # # # print(up)
    # # # # for i in up:
    # # # #     staffsalary=Salary.objects.create(
    # # # #                 Staff_salary=0,
    # # # #                 staff_id=i.id
    # up.delete()

    #             )
    return render(request,'school_admin/admin_home.html') 

def add_staff_page(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mob']
        dob=request.POST['dob']
        address=request.POST['address']
        qualification=request.POST['qualification']
        experience=request.POST['experience']
        type=request.POST['type']
        gender=request.POST['gender']
        subject=request.POST['subject']
        designation=request.POST['designation']

        if type=='teacher':



            log=Login.objects.create(
                username=email,
                password=mobile,
                usertype=type,
            )

            staff=AddStaff.objects.create(
                Staffname=name,
                Staff_email=email,
                Staff_dob=dob,
                Staff_mobile=mobile,
                Staff_qualification=qualification,
                Staff_address=address,
                Staff_experience=experience,
                Staff_type='teacher',
                Staff_gender=gender,
            )

            stafff=AddStaff.objects.get(Staff_mobile=mobile,Staff_email=email)

            Teacher=Teachers.objects.create(
                 Subject=subject,
                 authorize=log,
                 staff_id=stafff.id
            )
            staffsalary=Salary.objects.create(
                    Staff_salary=0,
                    staff_id=stafff.id

                )

        if type=='office':

            log=Login.objects.create(
                username=email,
                password=mobile,
                usertype=type,
            )

            staff=AddStaff.objects.create(
                Staffname=name,
                Staff_email=email,
                Staff_dob=dob,
                Staff_mobile=mobile,
                Staff_qualification=qualification,
                Staff_address=address,
                Staff_experience=experience,
                Staff_type=designation,
                Staff_gender=gender,
            )

            office=AddStaff.objects.get(Staff_mobile=mobile,Staff_email=email)

            if designation=='officestaff':
                officestaffs=OfficeStaff.objects.create(
                    authorize=log,
                    staff_id=office.id
                )
                staffsalary=Salary.objects.create(
                    Staff_salary=0,
                    staff_id=office.id

                )

            if designation=='principal':
                princi=Principal.objects.create(
                    authorize=log,
                    staff_id=office.id
                )
                staffsalary=Salary.objects.create(
                    Staff_salary=0,
                    staff_id=office.id

                )       



    return render(request,'school_admin/add_staff.html') 


    
def add_class_page(request):
    if request.method=='POST':
        classname=request.POST['grade']
        classrm=Classroom.objects.create(
         name=classname    
        )

    return render(request,'school_admin/add_class.html') 

def adddvision(request):
    cls=Classroom.objects.all()
    teacher=Teachers.objects.all()
    if request.method=='POST':
        classroom=request.POST['classroom']
        classname=request.POST['classname']
        section=request.POST['section']
        capacity=request.POST['Capacity']
        classteacher=request.POST['teacher']

        teachr=Teachers.objects.get(id=int(classteacher))
        clsroom=Classroom.objects.get(id=int(classroom))

        clsdiv=Classdivision.objects.create(
            name=classname,
            Section=section,
            max_capacity=capacity,
            classroom_id=clsroom.id,
            teacher_id=teachr.id
        )



    return render(request,'school_admin/adddivision.html',{'data':cls,'dat':teacher})     

def view_staff_page(request):
    staff= AddStaff.objects.all()
    return render(request,'school_admin/view_staff.html',{'data':staff}) 

def newcheck(request):
    staff= AddStaff.objects.all()
    return render(request,'school_admin/newpage.html',{'data':staff}) 

def getdet(request):
    stafftype=request.POST['staff']
    staffs = AddStaff.objects.filter(Staff_type=stafftype)
    data = [{'id': staff.id, 'name': staff.Staffname} for staff in staffs]
    return JsonResponse({'data':data})

def getstaffinfo(request,sid):
    sal=Salary.objects.get(staff_id=sid)
    data=[{'salary':sal.Staff_salary}]
    return JsonResponse({'dat':data})

def addfees(request):
    cls= Classroom.objects.all()
    if request.method=='POST':
        feesname=request.POST['feesname']
        amount=request.POST['amount']
        classname=request.POST['classn']
        classname=int(classname)

        clsrm=Classroom.objects.get(id=classname)

        Feess=Fees.objects.create(
            Feesname=feesname,
            Amount=amount,
            classname_id=clsrm.id,
        )


    return render(request,'school_admin/addfees.html',{'data':cls})     

def view_student_page(request):
    return render(request,'school_admin/view_student.html') 

def salary_page(request):
    staff=AddStaff.objects.all()
    if request.method=='POST':
        teacher=request.POST['teacher']
        officestaff=request.POST['officestaff']
        principal=request.POST['principal']
        salary=request.POST['salary']
        type=request.POST['type']

        if type=='teacher':
            Salarydet=Salary.objects.get(staff_id=int(teacher))
            Salarydet.Staff_salary=salary
            Salarydet.save()
            return render(request,'school_admin/assign_salary.html',{'data':staff}) 

        if type=='officestaff':
            Salarydet=Salary.objects.get(staff_id=int(officestaff))
            Salarydet.Staff_salary=salary
            Salarydet.save()
            return render(request,'school_admin/assign_salary.html',{'data':staff})  

        if type=='principal':
            print('dddd')
            Salarydet=Salary.objects.get(staff_id=int(principal))
            Salarydet.Staff_salary=salary
            Salarydet.save()
            return render(request,'school_admin/assign_salary.html',{'data':staff})    






        

    return render(request,'school_admin/assign_salary.html',{'data':staff}) 


def addsubjdect(request):
    classs=Classroom.objects.all()
    if request.method=='POST':
        classname=request.POST['classn']
        classrm=Classroom.objects.get(id=int(classname))
        classno=request.POST['nosub']
        clss=int(classno)
        for i in range(clss):
            # print(f"sub_{i}")
        
            sub=request.POST[f'sub_{i+1}']
            subject=Subjects.objects.create(
                Subjectname=sub,
                classname_id=classrm.id,
            )
    return render(request,'school_admin/addsubject.html',{'data':classs})  
