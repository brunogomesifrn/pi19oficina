# Generated by Django 2.2.4 on 2019-11-17 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data')),
                ('hora', models.TimeField(verbose_name='Data')),
                ('contato', models.IntegerField(max_length=11, verbose_name='Número')),
                ('resultado', models.BooleanField(default=False, verbose_name='Situação')),
                ('conclusao', models.BooleanField(default=False, verbose_name='Concluído')),
            ],
        ),
    ]
