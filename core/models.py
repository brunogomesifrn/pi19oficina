from django.db import models
from django.contrib.auth.models import User
# Create your models here.	
class Reservas(models.Model):
	data = models.DateField('Data')
	hora = models.TimeField('Hora')
	contato = models.IntegerField('Telefone')
	resultado = models.BooleanField('Situação', default=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comentarios(models.Model):
	nome = models.CharField('nome', max_length=100)
	comentario = models.TextField('Comentário')
	user = models.ForeignKey(User, on_delete=models.CASCADE)