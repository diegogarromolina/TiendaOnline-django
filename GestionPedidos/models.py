from django.db import models

# Create your models here.

class Clientes(models.Model):

    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    tfno = models.CharField(max_length=7)

class Articulos(models.Model):

    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return('El nombre del producto es {}, la sección es {} y el precio es {}.'.format(self.nombre, self.seccion, self.precio))

class Pedidos(models.Model):

    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()