import email
import profile
from time import time
from django.db import models
import datetime
# Create your models here.

class mr_user(models.Model):
    
    user_name = models.CharField(max_length=255 , default="" ,unique=True)
    
    password = models.CharField(max_length=500, default="")
    
    profile_pic = models.ImageField(upload_to="profiles" , null=True,  blank=True)
    
    first_name = models.CharField(max_length=255, default="")
    
    last_name = models.CharField(max_length=255, default="")
    
    mobile = models.BigIntegerField()
    
    latitude = models.FloatField(default=0)
    
    longitude = models.FloatField(default=0)
    
    # dob= models.DateField(("Date"), default=2000-01-01)
    
    
class dr_user(models.Model):
    
    first_name = models.CharField(max_length=255, default="")
    
    last_name = models.CharField(max_length=255, default="")
    
    hospital_name = models.CharField(max_length=255, default="")
    
    mobile = models.BigIntegerField()
    
    email = models.CharField(max_length=255 , default="" ,unique=True)

    category = models.CharField(max_length=255, default="")
 
    latitude = models.FloatField(default=0)
    
    longitude = models.FloatField(default=0)
    
    profile_pic = models.ImageField(upload_to="profiles" , null=True,  blank=True)
    
    city = models.CharField(max_length=255)
    
    

class visits(models.Model):

    hospital_name = models.CharField(max_length=255)
    doctor_name = models.CharField(max_length=255)

    latitude = models.FloatField(default=0)
    
    longitude = models.FloatField(default=0)
    
    mr_username = models.CharField(max_length=255)
    
    # date = models.DateField(_(""), auto_now=False, auto_now_add=False)
    # time = models.TimeField(_(""), auto_now=False, auto_now_add=False)
    # timestamp = models.DateField(_(""),)
    ppt_path = models.CharField(max_length=50)
    
    
    
    
    
    
    
    
    
    
    
    
