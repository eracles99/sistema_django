# Generated by Django 4.0 on 2021-12-22 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ControlSilabico', '0006_alter_tcreadito_options_remove_tcreadito_nro_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tdetalle_ca',
            options={'ordering': ['Id_Carga'], 'verbose_name': 'Detalle Carga Acdemica', 'verbose_name_plural': 'tdetalleCAs'},
        ),
    ]
