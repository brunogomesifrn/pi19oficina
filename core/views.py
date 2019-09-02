from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'home.html')
def perfil(request):
	return render(request, 'perfil.html')
def cadastro(request):
	return render(request, 'cadastro.html')
