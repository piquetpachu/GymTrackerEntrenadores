# usuarios/views.py
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroForm
from django.contrib.auth.decorators import login_required
from clientes.models import Cliente



def logout_view(request):
    logout(request)
    return redirect("account_login")

def registro_view(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("panel_entrenador")
    else:
        form = RegistroForm()
    return render(request, "usuarios/registro.html", {"form": form})

@login_required
def panel_entrenador(request):
    return render(request, "usuarios/panel_entrenador.html")

@login_required
def panel_admin(request):
    clientes = Cliente.objects.all()
    return render(request, "usuarios/panel_admin.html")