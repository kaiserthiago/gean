# Generated by Django 2.2.10 on 2020-08-27 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0015_auto_20200827_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificadoelemento',
            name='tipo_concentracao',
            field=models.IntegerField(choices=[[0, 'Certificado'], [1, 'Informado']], default=0, verbose_name='Tipo Concentração'),
        ),
        migrations.AlterField(
            model_name='certificadoelemento',
            name='tipo_fracao_massa',
            field=models.IntegerField(choices=[[0, '%'], [1, 'PPM'], [2, 'PPB']], default=0, verbose_name='Tipo Fração de Massa'),
        ),
    ]
