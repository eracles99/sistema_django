# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class Catdocente(models.Model):
    idcategoria = models.CharField(db_column='idCategoria', primary_key=True, max_length=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'catdocente'


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
