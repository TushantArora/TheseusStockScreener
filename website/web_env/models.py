from django.db import models

# Create your models here.

class TRADER(models.Model):
    uname= models.CharField(max_length=50,default="abc")
    uemail=models.CharField(max_length=50,default="abc@xyz.com")
    upassword = models.CharField(max_length=50,default="123")

class stock:
    sname:str
    srecc:str
    sbuy:int
    ssell:int
    sneut:int
    
