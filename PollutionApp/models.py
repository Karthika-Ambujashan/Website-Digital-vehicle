from django.db import models

# Create your models here.
class Pollutiondb(models.Model):
    registration_no = models.CharField(max_length=100,default=0)
    vehicle_make= models.CharField(max_length=20,default=0)
    vehicle_model = models.CharField(max_length=20,default=0)
    yearof_manufacture= models.CharField(max_length=10,default=0)
    typeof_vehicle= models.CharField(max_length=50,default=0)
    typeof_engine = models.CharField(max_length=20,default=0)
    id_number = models.CharField(max_length=20,default=0)
    engine_no = models.CharField(max_length=20,default=0)
    speedo_meter = models.CharField(max_length=10,default=0)
    date = models.DateField()
    fuel = models.CharField(max_length=20,default=0)

class PollutionRegisterdb(models.Model):
    password = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)