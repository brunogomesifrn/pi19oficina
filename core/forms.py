from django.forms import ModelForm
from .models import Reservas
from django import forms
#from django.contrib.auth.forms import UserCreationForm
#from .models import CustomUser

class ReservaForm(ModelForm):
	class Meta:
		model = Reservas
		fields = ['data', 'hora', 'contato']
#class CustomUserCreationForm(UserCreationForm):
#	class Meta:
#		model = CustomUser
#		fields = ['username', 'email', 'apelido']