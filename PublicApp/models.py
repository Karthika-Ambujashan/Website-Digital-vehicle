from django.db import models
from AdminApp.models import *
# Create your models here.
class Regisdb(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=25)
    phonenumber=models.IntegerField()
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=15)
    username=models.CharField(max_length=15,default='')
class Rc_Dashboard(models.Model):
    rid = models.ForeignKey(RcDetailsdb,on_delete=models.CASCADE)
    userdid = models.ForeignKey(Regisdb,on_delete=models.CASCADE)
    engine_no = models.CharField(max_length=20)
    chassis_no =models.CharField(max_length=20)
class Dl_Dashboard(models.Model):
    dlid = models.ForeignKey(Licensedb,on_delete=models.CASCADE)
    userdid = models.ForeignKey(Regisdb,on_delete=models.CASCADE)
    dob = models.CharField(max_length=20)
class Complaintdb(models.Model):
    date_reported=models.DateField()
    color=models.CharField(max_length=10)
    Body_style=models.CharField(max_length=10)
    marker_platenumber=models.CharField(max_length=10)
    vehicle_registered=models.BooleanField()
    vehicle_register_state=models.CharField(max_length=10)
    door_locked=models.BooleanField()
    keys_invehicle=models.BooleanField()
    nameof_owner=models.CharField(max_length=10)
    address=models.CharField(max_length=30)
    court_available=models.BooleanField()
    date_vehicle_stolen=models.DateField()
    vehicle_identification_number=models.IntegerField()
    nameof_insurance_company=models.CharField(max_length=10)
    phone_number=models.IntegerField()
    dayof_week=models.CharField(max_length=10)
    time=models.TimeField()
    location_from=models.CharField(max_length=10)



    


