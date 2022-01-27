# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Carga(models.Model):
    idcarga = models.AutoField(db_column='idCarga', primary_key=True)  # Field name made lowercase.
    iddocente = models.ForeignKey('Docente', models.DO_NOTHING, db_column='idDocente')  # Field name made lowercase.
    idhorario = models.ForeignKey('Horario', models.DO_NOTHING, db_column='idHorario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'carga'


class Catcurso(models.Model):
    idcat_curso = models.CharField(primary_key=True, max_length=5)

    class Meta:
        managed = False
        db_table = 'catcurso'
    def __str__(self):
        return self.idcat_curso

class Catdocente(models.Model):
    idcategoria = models.CharField(db_column='idCategoria', primary_key=True, max_length=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'catdocente'
    def __str__(self):
        return self.idcategoria


class Curso(models.Model):
    idcurso = models.CharField(db_column='idCurso', primary_key=True, max_length=10)  # Field name made lowercase.
    nombre = models.CharField(max_length=100, blank=True, null=True)
    carrera = models.CharField(max_length=45, blank=True, null=True)
    grupo = models.CharField(max_length=1, blank=True, null=True)
    creditos = models.CharField(max_length=2, blank=True, null=True)
    idcat_curso = models.ForeignKey(Catcurso, models.DO_NOTHING, db_column='idcat_curso')

    class Meta:
        managed = False
        db_table = 'curso'


class Cursodetalle(models.Model):
    idcursodetalle = models.AutoField(db_column='idCursoDetalle', primary_key=True)  # Field name made lowercase.
    idcurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='idCurso')  # Field name made lowercase.
    idtipocurso = models.ForeignKey('Tipocurso', models.DO_NOTHING, db_column='idtipoCurso')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cursodetalle'


class Dia(models.Model):
    idd = models.CharField(db_column='idD', primary_key=True, max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dia'


class Docente(models.Model):
    iddocente = models.CharField(db_column='idDocente', primary_key=True, max_length=10)  # Field name made lowercase.
    nombrecompleto = models.CharField(db_column='nombreCompleto', max_length=100)  # Field name made lowercase.
    correo = models.CharField(max_length=100, blank=True, null=True)
    idcategoria = models.ForeignKey(Catdocente, models.DO_NOTHING, db_column='idCategoria')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'docente'


class Horario(models.Model):
    idhorario = models.AutoField(db_column='idHorario', primary_key=True)  # Field name made lowercase.
    ht = models.IntegerField(db_column='hT')  # Field name made lowercase.
    hp = models.IntegerField(db_column='hP', blank=True, null=True)  # Field name made lowercase.
    idd = models.ForeignKey(Dia, models.DO_NOTHING, db_column='idD')  # Field name made lowercase.
    hrinicio = models.CharField(db_column='hrInicio', max_length=2)  # Field name made lowercase.
    hrfin = models.CharField(db_column='hrFin', max_length=2)  # Field name made lowercase.
    aula = models.CharField(db_column='Aula', max_length=15, blank=True, null=True)  # Field name made lowercase.
    idcursodetalle = models.ForeignKey(Cursodetalle, models.DO_NOTHING, db_column='idCursoDetalle')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'horario'


class Semestre(models.Model):
    idsemestre = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'semestre'


class Silabo(models.Model):
    idsilabo = models.AutoField(primary_key=True)
    unidad = models.CharField(max_length=4)
    capitulo = models.CharField(max_length=6)
    sesion = models.IntegerField()
    idcarga = models.ForeignKey(Carga, models.DO_NOTHING, db_column='idCarga')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'silabo'


class Tipocurso(models.Model):
    idtipocurso = models.CharField(db_column='idtipoCurso', primary_key=True, max_length=1)  # Field name made lowercase.
    tipo = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipocurso'


class Users(models.Model):
    usuario = models.OneToOneField(Docente, models.DO_NOTHING, db_column='usuario', primary_key=True)
    contrasenia = models.CharField(max_length=15)
    tipo = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'users'
        unique_together = (('usuario', 'tipo'),)
