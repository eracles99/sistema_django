from django.db import models

# Create your models here.
class Docente(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    grado=models.CharField(max_length=100,blank=False,null=False)
    categoria=models.CharField(max_length=100,blank=False,null=False)
    correo=models.CharField(max_length=100,blank=False,null=False)

    def __str__(self):
        return self.name


