# Generated by Django 2.2.10 on 2020-04-13 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0012_medicao_tipo_incerteza'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicao',
            name='descricao',
            field=models.CharField(default='', max_length=150, verbose_name='Descrição'),
            preserve_default=False,
        ),
    ]
