from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Usermodel(models.Model):
    user_name = models.CharField(unique=True,max_length=50)
    password = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)
    pri = models.CharField(max_length=100, default = None,blank= True)
    
class Privillages(models.Model):
    privillages_name = models.CharField(max_length = 50)