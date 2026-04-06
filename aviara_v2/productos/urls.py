from django.urls import path
from . import views

urlpatterns = [
    # Catálogo cliente (Base de datos local)
    path('', views.lista_productos_api, name='catalogo'),
    
    # Panel Admin (API Externa)
    path('admin-api/', views.admin_productos_api, name='productos_api'),
    
    # Rutas de creación (Para que no den error)
    path('nuevo/', views.crear_producto_api, name='crear_producto_api'),
    path('nuevo-suministro/', views.crear_producto_api, name='crear_suministro'),
]