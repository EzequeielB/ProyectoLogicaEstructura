from django.db import models

# Create your models here.

class cliente(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    correo=models.EmailField(max_length=50)
    direccion=models.CharField(max_length=150)
    numeroDeTelefono=models.CharField(max_length=50)
    
    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.nombre,self.apellido)