from email.policy import default
from django.db import models

class Familia(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    edad= models.IntegerField()
    fechanac=models.DateField(null=True)

