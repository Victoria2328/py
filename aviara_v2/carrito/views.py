from django.shortcuts import redirect, render, get_object_or_404
from productos.models import VariacionProducto
from .carrito import Carrito
from django.contrib.auth.decorators import login_required
from ventas.models import Pedido, ItemPedido 
from django.contrib import messages


# ===== VER CARRITO =====
@login_required(login_url='login')
def ver_carrito(request):
    carrito = request.session.get("carrito", {})

    if not carrito:
        messages.info(request, "Tu carrito está vacío.")

    return render(request, 'carrito/ver_carrito.html')


# ===== AGREGAR =====
@login_required(login_url='login')
def agregar_producto(request, variacion_id):
    carrito = Carrito(request)
    variacion = get_object_or_404(VariacionProducto, id=variacion_id)

    carrito.agregar(variacion=variacion)

    return redirect(request.META.get('HTTP_REFERER', 'catalogo'))


# ===== ELIMINAR =====
@login_required(login_url='login')
def eliminar_producto(request, variacion_id):
    carrito = Carrito(request)
    variacion = get_object_or_404(VariacionProducto, id=variacion_id)

    carrito.eliminar(variacion=variacion)

    return redirect("carrito:ver_carrito")


# ===== RESTAR =====
@login_required(login_url='login')
def restar_producto(request, variacion_id):
    carrito = Carrito(request)
    variacion = get_object_or_404(VariacionProducto, id=variacion_id)

    carrito.restar(variacion=variacion)

    return redirect("carrito:ver_carrito")


# ===== LIMPIAR =====
@login_required(login_url='login')
def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()

    messages.success(request, "Carrito vaciado correctamente.")

    return redirect("carrito:ver_carrito")
  # ajusta según tus modelos

@login_required(login_url='login')
def carrito_view(request):
    # obtener o crear carrito del usuario
    carrito, created = Carrito.objects.get_or_create(usuario=request.user, activo=True)
    
    #items = ItemCarrito.objects.filter(carrito=carrito)
    #total = sum(item.variacion.precio * item.cantidad for item in items)

    context = {
        'carrito': carrito,
        #'items': items,
        #'total': total
    }
    return render(request, 'ventas/carrito.html', context)


# carrito/views.py

def procesar_pedido(request):
    return redirect('home')