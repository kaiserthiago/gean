# Generated by Django 2.2.10 on 2020-04-03 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20200403_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificado',
            name='codigo',
            field=models.CharField(default='', max_length=150, verbose_name='Código'),
            preserve_default=False,
        ),
    ]