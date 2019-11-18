from django.forms import ModelForm
from .models import Reservas, Comentarios
from django import forms

class ReservaForm(ModelForm):
	class Meta:
		model = Reservas
		fields = ['data', 'hora', 'contato']

class ComentarioForm(ModelForm):
	class Meta:
		model = Comentarios
		fields = ['nome', 'comentario']