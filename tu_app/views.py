from rest_framework import viewsets
from .models import Tienda, Orden, OrdenDetalle, Producto
from .serializers import TiendaSerializer, OrdenSerializer, OrdenDetalleSerializer, ProductoSerializer

# Create your views here.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class TiendaViewSet(viewsets.ModelViewSet):
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

class OrdenDetalleViewSet(viewsets.ModelViewSet):
    queryset = OrdenDetalle.objects.all()
    serializer_class = OrdenDetalleSerializer