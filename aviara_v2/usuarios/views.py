from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegistroForm

# --- GESTIÓN DE SESIÓN Y REGISTRO ---

def registro_view(request):
    if request.method == 'POST':
        # CAMBIO: Usamos RegistroForm en lugar de UserCreationForm estándar
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada. Por favor, inicia sesión.")
            return redirect('login') 
    else:
        form = RegistroForm()
    
    return render(request, 'registration/registro.html', {'form': form})

def salir(request):
    """Cierra sesión y redirige al login"""
    django_logout(request)
    return redirect('login')

# --- DASHBOARD Y ROLES ---

@login_required
def check_auth(request):
    if request.user.is_staff:
        return redirect('dashboard')
    else:
        return redirect('catalogo')

@login_required
def dashboard(request):
    """Vista del panel administrativo"""
    if not request.user.is_staff:
        return redirect('produccion_lista')
    return render(request, 'dashboard.html')