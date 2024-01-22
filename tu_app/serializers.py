from rest_framework import serializers
from django.db.models import Count
from .models import Producto, Tienda, Orden, OrdenDetalle

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class TiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tienda
        fields = '__all__'

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'

class OrdenDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenDetalle
        fields = '__all__'