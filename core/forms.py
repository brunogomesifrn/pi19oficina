from django.forms import ModelForm
from .models import Reserva

class ReservaForm(ModelForm):
	class Meta:
		model = Reserva
		fields= ['data', 'hora', 'contato']