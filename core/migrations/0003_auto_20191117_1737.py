# Generated by Django 2.2.4 on 2019-11-17 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191117_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='contato',
            field=models.IntegerField(verbose_name='Telefone'),
        ),
    ]