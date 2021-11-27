from django.db import models

class curso(models.Model):
    code=models.CharField( primary_key=True, max_length=10)
    name=models.CharField( max_length=200,blank=False,null=False)
    credits=models.CharField( max_length=10,blank=False,null=False)
    carrera=models.CharField(max_length=100,blank=False,null=False)
    grupo=models.CharField(max_length=1,blank=True,null=True)
    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'
        ordering=['name']
    def __str__(self):
        return self.code
class CursosHorarios(models.Model):
    id=models.AutoField(primary_key=True)
    tipo=models.CharField( max_length=10,blank=False,null=False)
    ht=models.CharField( max_length=2,blank=False,null=False)
    hp=models.CharField( max_length=2,blank=False,null=False)
    day=models.CharField( max_length=15,blank=False,null=False)
    hr_i=models.CharField( max_length=2,blank=False,null=False)
    hr_f=models.CharField( max_length=2,blank=False,null=False)
    matriculados=models.CharField( max_length=2,blank=False,null=False)
    semestre=models.CharField( max_length=7,blank=False,null=False)
    id_curso=models.ForeignKey(curso,on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'CursosHorarios'
        verbose_name_plural = 'CursosHorarios'
        ordering=['day']

# Create your models here.
