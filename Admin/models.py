from django.db import models
from django.contrib.auth.models import User

class package(models.Model):
    pname=models.CharField(max_length=20,primary_key=True)
    pcity=models.CharField(max_length=20)
    pdur=models.CharField(max_length=10)
    pdec=models.CharField(max_length=150)
    pprize=models.DecimalField(max_digits=1000, decimal_places=2)
    pimage=models.ImageField(upload_to='pimages/')
    def __str__(self):
        return self.pname + ": " + str(self.pimage)


class hotel(models.Model):
    hname=models.CharField(max_length=20,primary_key=True)
    hcity=models.CharField(max_length=20)
    hdec=models.CharField(max_length=150)
    hprize=models.DecimalField(max_digits=1000, decimal_places=2)
    himage=models.ImageField(upload_to='himages/')
    def __str__(self):
        return self.hname + ": " + str(self.himage)