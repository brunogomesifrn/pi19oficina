# Generated by Django 2.2.4 on 2019-11-18 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20191117_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='nome'),
        ),
    ]