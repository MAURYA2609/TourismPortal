from django.db import models
from django.contrib.auth.models import User

class pBookings(models.Model):
    pname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    class Meta:
        unique_together = ('username','pname')
        
class hBookings(models.Model):
    hname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    class Meta:
        unique_together = ('username','hname')
   