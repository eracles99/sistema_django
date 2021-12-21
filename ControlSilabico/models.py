from django.db import models
from django.db.models.fields import CharField

# Create your models herfrom django.db import models

# Create your models here.
class tcurso(models.Model):
    codeC=models.CharField ( primary_key=True, max_length=10)
    name=models.CharField( max_length=200,blank=False,null=False)
    credits=models.CharField( max_length=10,blank=False,null=False)
    carrera=models.CharField(max_length=100,blank=False,null=False)
    grupo=models.CharField(max_length=1,blank=True,null=True)
    class Meta:
        db_table='tcurso'
        verbose_name = 'tcurso'
        verbose_name_plural = 'tcursos'
        ordering=['name']
    def __str__(self):
        return self.codeC

class tdocente(models.Model):
    codeD=models.CharField(primary_key=True,max_length=10)
    name=models.CharField(max_length=100,blank=False,null=False)
    Categoria=models.CharField(max_length=50,blank=False,null=False)
    correo=models.EmailField(max_length=100,blank=False,null=False)
    class Meta:
        db_table='tdocente'
        verbose_name = 'tdocente'
        verbose_name_plural = 'tdocentes'
        ordering=['name']
    def __str__(self):
        return self.codeD
class tcarga_academica(models.Model): 
    id= models.AutoField(primary_key=True)  
    codeC=models.OneToOneField(tcurso,on_delete=models.CASCADE)
    codeD=models.ForeignKey(tdocente,on_delete=models.CASCADE)
    nameDocente=models.CharField(max_length=200,blank=False,null=False)
    nameCurso=models.CharField(max_length=200,blank=False,null=False)
    class Meta:
        db_table='tcarga'
        verbose_name = 'tcargaAcademica'
        verbose_name_plural = 'tcargaAcademica'
        
        ordering=['nameDocente']
    def __str__(self):
        return str(self.id)
        
class tdia(models.Model):
    id= models.AutoField(primary_key=True)
    dia=models.CharField(max_length=15)
    class  Meta:
        db_table = 'tdia'
        managed = True
        verbose_name = 'Dias'
        verbose_name_plural = 'tdias'
    def __str__(self):
        return self.dia
        
class tdetalle_ca(models.Model):
    Id_D=models.AutoField(primary_key=True)
    Id_Carga=models.ForeignKey(tcarga_academica,on_delete=models.CASCADE)
    tipo=models.CharField(max_length=1,blank=False,null=False)
    hrTeorico=models.CharField(max_length=1,blank=False,null=False)
    hrPractico=models.CharField(max_length=1,blank=False,null=False)
    dia=models.ForeignKey(tdia,on_delete=models.CASCADE)
    hrInicio=models.CharField(max_length=2,blank=False,null=False)
    hrFin=models.CharField(max_length=2,blank=False,null=False)
    Aula=models.CharField(max_length=20,blank=False,null=False)
    class Meta:
        db_table='tdetalle_Carga'
        verbose_name = 'Detalle Carga Acdemica'
        verbose_name_plural = 'tdetalleCAs'
    def __str__(self):
        return str(self.Id_Carga)
        