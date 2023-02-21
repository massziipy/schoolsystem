from django.db import models
from school_admin.models import Classroom

# Create your models here.
class Exams(models.Model):
    Examname=models.CharField(max_length=50)
    grade=models.ForeignKey(Classroom,on_delete=models.CASCADE)  
