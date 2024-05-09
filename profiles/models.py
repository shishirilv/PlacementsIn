from django.db import models


# Create your models here.
class Profiles(models.Model):
    name=models.CharField(max_length=120,default='Some name')
    branch=models.CharField(max_length=120,default='Some branch')
    jobtitle=models.CharField(max_length=120)
    cgpa=models.DecimalField(decimal_places=2,max_digits=1000)
    major=models.CharField(max_length=120)
    mini=models.CharField(max_length=120)
    minor=models.CharField(max_length=120)
    internships=models.TextField(null=True,blank=True)
    special_courses=models.TextField(null=True,blank=True)
    email=models.EmailField(max_length=250)
    LinkedIn=models.CharField(max_length=200)
    org=models.CharField(max_length=120,default='some company')
    package_LPA=models.DecimalField(decimal_places=1,max_digits=1000,default=5)

