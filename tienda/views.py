from django.shortcuts import render
from rest_framework import generics, viewsets

from tienda.models import Empresa, Precio, Producto, Unidad
from tienda.serializers import EmpresaSerializer, PrecioSerializer, ProductoSerializer, UnidadSerializer

# Create your views here.
class UnidadList(generics.ListCreateAPIView):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer

class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class PrecioList(generics.ListCreateAPIView):
    queryset = Precio.objects.all()
    serializer_class = PrecioSerializer

class EmpresaList(generics.ListCreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer