from django.db import models

# Create your models here.
class Insurancedb(models.Model):
    
    owner_name = models.CharField(max_length=100,default=0)
    engine_no = models.CharField(max_length=13,default=0)
    chassis_no = models.CharField(max_length=17,default=0)
    registration_no = models.CharField(max_length=10,default=0)
    period_from = models.DateField()
    period_to = models.DateField()

class InsuranceRegisterdb(models.Model):
    password = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)