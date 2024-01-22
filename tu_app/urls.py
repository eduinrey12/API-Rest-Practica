from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, TiendaViewSet, OrdenViewSet, OrdenDetalleViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'tiendas', TiendaViewSet)
router.register(r'ordenes', OrdenViewSet)
router.register(r'ordenes-detalles', OrdenDetalleViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]