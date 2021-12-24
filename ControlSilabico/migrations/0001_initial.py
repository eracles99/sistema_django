# Generated by Django 4.0 on 2021-12-22 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tcarga_academica',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nameDocente', models.CharField(max_length=200)),
                ('nameCurso', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'tcargaAcademica',
                'verbose_name_plural': 'tcargaAcademica',
                'db_table': 'tcarga',
                'ordering': ['nameDocente'],
            },
        ),
        migrations.CreateModel(
            name='tcreadito',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nro', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name': 'tcredito',
                'verbose_name_plural': 'tcreditos',
                'db_table': 'tcredito',
                'ordering': ['nro'],
            },
        ),
        migrations.CreateModel(
            name='tcurso',
            fields=[
                ('codeC', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('credits', models.CharField(max_length=10)),
                ('carrera', models.CharField(max_length=100)),
                ('grupo', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'verbose_name': 'tcurso',
                'verbose_name_plural': 'tcursos',
                'db_table': 'tcurso',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='tdia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dia', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Dias',
                'verbose_name_plural': 'tdias',
                'db_table': 'tdia',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='tdocente',
            fields=[
                ('codeD', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('Categoria', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=100)),
            ],
            options={
                'verbose_name': 'tdocente',
                'verbose_name_plural': 'tdocentes',
                'db_table': 'tdocente',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='tdetalle_ca',
            fields=[
                ('Id_D', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=1)),
                ('hrTeorico', models.CharField(max_length=1)),
                ('hrPractico', models.CharField(max_length=1)),
                ('hrInicio', models.CharField(max_length=2)),
                ('hrFin', models.CharField(max_length=2)),
                ('Aula', models.CharField(max_length=20)),
                ('Id_Carga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ControlSilabico.tcarga_academica')),
                ('dia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ControlSilabico.tdia')),
            ],
            options={
                'verbose_name': 'Detalle Carga Acdemica',
                'verbose_name_plural': 'tdetalleCAs',
                'db_table': 'tdetalle_Carga',
            },
        ),
        migrations.AddField(
            model_name='tcarga_academica',
            name='codeC',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ControlSilabico.tcurso'),
        ),
        migrations.AddField(
            model_name='tcarga_academica',
            name='codeD',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ControlSilabico.tdocente'),
        ),
        migrations.AddField(
            model_name='tcarga_academica',
            name='creditos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ControlSilabico.tcreadito'),
        ),
    ]