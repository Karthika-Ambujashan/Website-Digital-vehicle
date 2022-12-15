from django.db import models
from AdminApp.models import *
from PublicApp.models import*
# Create your models here.
class Policedb(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class DisciplinaryActiondb(models.Model):
    reason = models.TextField(max_length=200)
    amount = models.IntegerField(default=0)
    dlid = models.ForeignKey(Licensedb,on_delete=models.CASCADE)
    status = models.IntegerField(default=0)