from .models import Empresa, Envase, Medida, Precio, Producto, Unidad
from rest_framework import serializers

class UnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = '__all__'   

class EnvaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envase
        fields = '__all__'

class MedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medida
        fields = '__all__'

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    medida = MedidaSerializer()
    envase = EnvaseSerializer()
    empresa = EmpresaSerializer()
    class Meta:
        model = Producto
        fields = '__all__'


class PrecioSerializer(serializers.ModelSerializer):
    unidad = UnidadSerializer()
    producto = ProductoSerializer()
    class Meta:
        model = Precio
        fields = '__all__'
