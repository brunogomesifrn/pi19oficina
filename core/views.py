from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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