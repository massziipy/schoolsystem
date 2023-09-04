from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)


class Members(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    mobile=models.CharField(max_length=20)
    

