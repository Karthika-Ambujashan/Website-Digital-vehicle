from django.db import models

# Create your models here.
class Licensedb(models.Model):
    drivinglicenseNo=models.CharField(max_length=30)
    holder_name=models.CharField(max_length=20)
    license_authority=models.CharField(max_length=30)
    vehicle_class=models.CharField(max_length=30)
    issue_date=models.DateField(null=True,blank=False)
    license_validity=models.DateField(null=True,blank=False)
    dob=models.DateField(max_length=20,default='')
class RcDetailsdb(models.Model):
    owner_name = models.CharField(max_length=100,default=0)
    registered_rto = models.CharField(max_length=50,default=0)
    maker_model = models.CharField(max_length=13,default=0)
    vehicle_class = models.CharField(max_length=50,default=0)
    fuel_norms = models.CharField(max_length=30,default=0)
    engine_no = models.CharField(max_length=13,default=0)
    chassis_no = models.CharField(max_length=17,default=0)
    registration_date = models.DateField(default = 0)
    fitness_upto = models.DateField(default = 0)
    insurance_expiry = models.DateField(default = 0)
    insurance_expiry_in = models.DateField(default = 0)
    registration_no = models.CharField(max_length=10,default=0)
    color = models.CharField(max_length=20,default=0)
    unloaded_weight = models.IntegerField()
