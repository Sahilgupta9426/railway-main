from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Travel_Schedule(models.Model):
    
    train_no=models.IntegerField(primary_key=True)
    train_name=models.CharField(max_length=100)
    source=models.CharField(max_length=30)
    destination=models.CharField(max_length=30)
    arrival_time=models.CharField(max_length=30)
    fare=models.IntegerField()
class Train(models.Model):
    id=models.IntegerField(primary_key=True)
    seat1=models.IntegerField()
    seat2=models.IntegerField()
    seat3=models.IntegerField()
    seat4=models.IntegerField()
    seat5=models.IntegerField()
    seat6=models.IntegerField()
    seat7=models.IntegerField()
    seat8=models.IntegerField()
    seat9=models.IntegerField()
    seat10=models.IntegerField()
    sid=models.ForeignKey("Travel_Schedule",on_delete=models.CASCADE)

class Customer(models.Model):
    op=[('0', 'Male'),
    ('1', 'Female'),
    ('2', 'Transgender')]
    cid=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=100)
    gender=models.CharField(max_length=1,choices=op)
    number=models.CharField(max_length=10)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
