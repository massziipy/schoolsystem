from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)
    dob = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    prevschool = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)
    gender = models.CharField(max_length=30)
   

class Login(models.Model):
    username=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=20)   
    usertype=models.CharField(max_length=10)

