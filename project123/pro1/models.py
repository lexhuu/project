from django.db import models

# Create your models here.
class Emp(models.Model):
    Name=models.CharField(max_length=25)
    email=models.EmailField()
    phone=models.IntegerField()
    place=models.CharField(max_length=25)
       
