from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    # verbose_name es el nombre que aparece en el panel de administrador
    telefono = models.CharField(max_length=10, verbose_name="Teléfono")

    # __str__ permite modificar como se muestra cada objeto en el panel de administrador
    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()


class Pedido(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
