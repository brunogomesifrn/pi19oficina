# Generated by Django 2.2.4 on 2019-11-18 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20191117_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='nome',
            field=models.TextField(max_length=20, verbose_name='Nome'),
        ),
    ]
