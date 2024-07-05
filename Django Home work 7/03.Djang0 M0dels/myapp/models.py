from django.db import models
from datetime import datetime
# Create your models here.
 
class CustomUser(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    age=models.IntegerField()
    adress=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone_number=models.CharField(max_length=50)



    def __str__(self):
        return self.fname + " " + self.lname



class Tasks(models.Model):
    title=models.CharField(max_length=250)
    due_date=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now=True,blank=True)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    