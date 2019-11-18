"""pi19oficina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from core.views import home, cadastro, perfil, dados, reservas, cadastro_reserva, editar_reserva, excluir_reserva, confirmar_reserva, confirmar, comentario, comentarios
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('cadastro/', cadastro, name="cadastro"),
    path('perfil/', perfil, name='perfil'),
    path('perfil/reservas/<int:user>', reservas, name='reservas'),
    path('perfil/reservas/confirmar', confirmar_reserva, name='confirmar_reserva'),
    path('perfil/reserva/confirmar/<int:id>', confirmar, name='confirmar'),
    path('perfil/cadastrar/reserva', cadastro_reserva, name='cadastro_reserva'),
    path('perfil/reserva/editar/<int:id>', editar_reserva, name='editar_reserva'),
    path('perfil/reserva/excluir/<int:id>', excluir_reserva, name='excluir_reserva'),
    path('perfil/comentario', comentario, name='comentario'),
    path('perfil/comentarios', comentarios, name='comentarios'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('dados/<int:id>/', dados, name='dados'),
]
