from django.db import models
from common.models import Login

# Create your models here.
class AddStaff(models.Model):
    Staffname=models.CharField(max_length=20)
    Staff_email=models.CharField(max_length=20,unique=True)
    Staff_dob=models.CharField(max_length=20)
    Staff_mobile=models.BigIntegerField(unique=True)
    Staff_qualification=models.CharField(max_length=20)
    Staff_address=models.CharField(max_length=50)
    Staff_experience=models.CharField(max_length=20)
    Staff_type=models.CharField(max_length=20)
    Staff_gender=models.CharField(max_length=10)


class Teachers(models.Model):
    Subject=models.CharField(max_length=20)
    staff=models.ForeignKey(AddStaff, on_delete=models.CASCADE)
    authorize=models.OneToOneField(Login,on_delete=models.CASCADE)

class Principal(models.Model):
    staff=models.ForeignKey(AddStaff, on_delete=models.CASCADE)
    authorize=models.OneToOneField(Login,on_delete=models.CASCADE)  

class OfficeStaff(models.Model):
    staff=models.ForeignKey(AddStaff, on_delete=models.CASCADE)
    authorize=models.OneToOneField(Login,on_delete=models.CASCADE)

class Salary(models.Model):
    staff=models.OneToOneField(AddStaff, on_delete=models.CASCADE,unique=True)
    Staff_salary=models.CharField(max_length=20)


class Classroom(models.Model):
    name=models.CharField(max_length=20,unique=True)
   

class Classdivision(models.Model):
    name=models.CharField(max_length=20) 
    classroom=models.ForeignKey(Classroom,on_delete=models.CASCADE)
    max_capacity=models.PositiveBigIntegerField()  
    teacher=models.ForeignKey(Teachers,on_delete=models.CASCADE,default='')
    Section=models.CharField(max_length=3)


class Fees(models.Model):
    Feesname=models.CharField(max_length=20) 
    Amount=models.BigIntegerField(default=0)
    classname=models.ForeignKey(Classroom,on_delete=models.CASCADE)
   

class Subjects(models.Model):
    Subjectname=models.CharField(max_length=20) 
    classname=models.ForeignKey(Classroom,on_delete=models.CASCADE)

    
               


    





   



    


