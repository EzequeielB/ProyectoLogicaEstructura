from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('inicio/',views.inicio),
    path('registrarCliente/', views.registrarCliente),
    path('editarCliente/<id>', views.editarCliente),
    path('eliminarCliente/<id>', views.eliminarCliente),
    path('editar/', views.editar)
]
