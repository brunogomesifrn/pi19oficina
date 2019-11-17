from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reserva
from .forms import ReservaForm
# Create your views here.

def home(request):
	return render(request, 'home.html')

@login_required
def perfil(request):
	return render(request, 'perfil.html')

def cadastro(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('login')
	contexto = {
	'form': form
	}
	return render(request, 'cadastro.html', contexto)

@login_required
def dados(request, id):
	user = User.objects.get(pk=id)
	form = UserCreationForm(request.POST or None, instance=user)
	if form.is_valid():
		form.save()
		return redirect('perfil')
	contexto = {
	'form': form
	}
	return render(request, 'cadastro.html', contexto)

@login_required
def base(request):
	return render(request, 'base2.html')

@login_required
def reservas(request):
	reservas = Reserva.objects.all()
	contexto = {
	'lista_reservas': reservas
	}
	return render(request, 'reservas.html', contexto)
@login_required
def cadastro_reserva(request):
	form = ReservaForm(request.POST or None)
	if form.is_valid():
			form.save()
			return redirect('reservas')
	contexto = {
	'form': form
	}
	return render(request, 'cadastro_reserva.html', contexto)

@login_required
def editar_reserva(request, id):
	reserva = Reserva.objects.get(pk=id)
	form = ReservaForm(request.POST or None, instance=reserva)

	if form.is_valid():
			form.save()
			return redirect('reservas')
	contexto = {
	'form': form
	}
	return render(request, 'cadastro_reserva.html', contexto)

@login_required
def excluir_reserva(request, id):
	reserva = Reserva.objects.get(pk=id)
	reserva.delete()
	return redirect('reservas')