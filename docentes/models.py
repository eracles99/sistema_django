from django.db import models

# Create your models here.
class Docente(models.Model):
    code=models.CharField(primary_key=True,max_length=100)
    name=models.CharField(max_length=100,blank=False,null=False)
    grado=models.CharField(max_length=100,blank=False,null=False)
    categoria=models.CharField(max_length=100,blank=False,null=False)
    correo=models.CharField(max_length=100,blank=False,null=False)
    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
        ordering=['name']
    def __str__(self):
        return self.name


