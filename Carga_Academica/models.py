from django.db import models

# Create your models here.

class CargaAcademica(models.Model):
    Codigo = models.CharField(primary_key=True, max_length=8)
    Carrera=models.CharField(max_length=50)
    Docente=models.CharField(max_length=50)
    Creditos=models.PositiveSmallIntegerField()
    Tipo=models.CharField(max_length=50)
    Gpo=models.CharField(max_length=50)
    Ht=models.CharField(max_length=50)
    Hp=models.CharField(max_length=50)
    Dia=models.CharField(max_length=50)
    Horario_I=models.CharField(max_length=50)
    Horario_F=models.CharField(max_length=50)
    Aula=models.CharField(max_length=50)
    Matriculados=models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} ({1}) ({2}) ({3}) ({4}) ({5}) ({6}) ({7}) ({8}) ({9}) ({10}),({11})"
        return texto.format(self.Carrera, self.Docente, self.Creditos, self.Creditos, 
        self.Tipo, self.Gpo, self.Ht, self.Hp, self.Dia, self.Horario_I,self.Horario_F, self.Aula, self.Matriculados)