from django.db import models

# Create your models here.
from common.models import Login
from school_admin.models import Classdivision,Fees,Subjects

# Create your models here.
class Students(models.Model):
    Studentname=models.CharField(max_length=20)
    Studentemail=models.CharField(max_length=20,unique=True)
    Studentdob=models.CharField(max_length=20)
    Studentmob=models.BigIntegerField(unique=True)
    Studentguardian=models.CharField(max_length=20)
    Studentadress=models.CharField(max_length=50)
    Studentclass=models.ForeignKey(Classdivision, on_delete=models.CASCADE,default='')
    authorize=models.OneToOneField(Login,on_delete=models.CASCADE)
    Studentimage=models.ImageField(upload_to = 'student/', default = 'static/images/student.png')
    Student_gender=models.CharField(max_length=10) 


class Studentfees(models.Model):
    student=models.ForeignKey(Students, on_delete=models.CASCADE)
    fees=models.ForeignKey(Fees,on_delete=models.CASCADE)
    status=models.CharField(max_length=20,default='not_paid')


class Marks(models.Model):
    student=models.ForeignKey(Students, on_delete=models.CASCADE)
    subject=models.ForeignKey(Subjects,on_delete=models.CASCADE)
    Mark=models.BigIntegerField(default=0)    
