from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Tienda(models.Model):
    id_tienda = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
    
class Orden(models.Model):
    id_orden = models.AutoField(primary_key=True)
    id_tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.id_orden

class OrdenDetalle(models.Model):
    id_orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.id_orden