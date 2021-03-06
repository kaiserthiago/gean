# Generated by Django 2.2.10 on 2020-08-27 18:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0014_auto_20200413_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificadoelemento',
            name='tipo_concentracao',
            field=models.IntegerField(choices=[[0, 'Certificado'], [1, 'Informado']], default=0),
        ),
        migrations.AlterField(
            model_name='medicao',
            name='concentracao_medicao',
            field=models.DecimalField(decimal_places=5, default=0, help_text='Dados da medição', max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Concentração'),
        ),
        migrations.AlterField(
            model_name='medicao',
            name='incerteza_expandida_combinada',
            field=models.DecimalField(blank=True, decimal_places=5, default=0, help_text='Dados da medição', max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Incerteza Expandida Combinada'),
        ),
        migrations.AlterField(
            model_name='medicao',
            name='incerteza_expandida_medicao',
            field=models.DecimalField(blank=True, decimal_places=5, default=0, help_text='Dados da medição', max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Incerteza Expandida'),
        ),
        migrations.AlterField(
            model_name='medicao',
            name='incerteza_padrao_medicao',
            field=models.DecimalField(blank=True, decimal_places=5, default=0, help_text='Dados da medição', max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Incerteza Padrão'),
        ),
    ]
