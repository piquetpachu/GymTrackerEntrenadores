# usuarios/views.py
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroForm
from django.contrib.auth.decorators import login_required
from clientes.models import Cliente


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.rol == "entrenador":
                return redirect("usuarios:panel_entrenador")
            elif user.rol == "admin":
                return redirect("usuarios:panel_admin")
            else:
                messages.error(request, "Rol no reconocido.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    return render(request, "usuarios/login.html")

def logout_view(request):
    logout(request)
    return redirect("usuarios:login")

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