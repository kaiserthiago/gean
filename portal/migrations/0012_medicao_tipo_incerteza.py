# Generated by Django 2.2.10 on 2020-04-13 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_auto_20200413_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicao',
            name='tipo_incerteza',
            field=models.IntegerField(choices=[[0, 'Expandida'], [1, 'Padrão'], [2, 'Confiança'], [3, 'Combinada']], default=0),
        ),
    ]
