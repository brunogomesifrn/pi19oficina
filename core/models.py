from django.db import models

# Create your models here.
class Reserva(models.Model):
	data = models.DateField('Data')
	hora = models.TimeField('Data')
	contato = models.IntegerField('Telefone', max_length=11)
	resultado = models.BooleanField('Situação', default=False)
	conclusao = models.BooleanField('Concluído', default=False)
