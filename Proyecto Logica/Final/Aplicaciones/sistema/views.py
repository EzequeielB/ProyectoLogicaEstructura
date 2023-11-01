from django.shortcuts import render, redirect
from .models import cliente

# Create your views here.

def home(request):
    clientes=cliente.objects.all
    return render(request, "gestionClientes.html", {"clientes":clientes})

def inicio(request):
    return render(request, 'inicio.html')

def registrarCliente(request):
    nombre=request.POST['clienteNombre']
    apellido=request.POST['clienteApellido']
    correo=request.POST['clienteEmail']
    direccion=request.POST['clienteDireccion']
    numero=request.POST['clienteNumero']
    
    Cliente = cliente.objects.create( nombre=nombre,apellido=apellido,correo=correo,direccion=direccion,numeroDeTelefono=numero)
    return redirect('/')

def eliminarCliente(request,id):
    Cliente = cliente.objects.get(id=id)
    Cliente.delete()
    return redirect('/')

def editarCliente(request,id):
    Cliente = cliente.objects.get(id=id)
    return render(request, "editarCliente.html",{"cliente":Cliente})

def editar(request):
    id=request.POST['clienteID']
    nombre=request.POST['clienteNombre']
    apellido=request.POST['clienteApellido']
    correo=request.POST['clienteEmail']
    direccion=request.POST['clienteDireccion']
    numero=request.POST['clienteNumero']
    
    Cliente = cliente.objects.get(id=id)
    Cliente.nombre = nombre
    Cliente.apellido = apellido
    Cliente.correo = correo
    Cliente.direccion = direccion
    Cliente.numeroDeTelefono = numero
    Cliente.save()
    return redirect('/')