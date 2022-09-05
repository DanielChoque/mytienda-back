from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.http import Http404
from django.http import JsonResponse
from .dictionary import EmpresaDictionary, EnvaseDictionary, MedidaDictionary, UnidadDictionary
import csv
import math
#import unicodecsv as csv


from tienda.models import Empresa, Envase, Medida, Precio, Producto, Unidad
from tienda.serializers import PrecioSerializer


class DateNow(APIView):
    def get(self,request):
        res={"inicioHora":timezone.now()}        
        return Response(res)


class PrecioApi(APIView):
    def get_object(self, id):        
        try:
            print("auiq_1:")
            return Precio.objects.get(id = id)
        except Precio.DoesNotExist:
            raise Http404
    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = PrecioSerializer(snippet)
        print(snippet)
        return Response(serializer.data)

class DatosInicialesApi(APIView):
    def get(self, request, format=None):
        empresas = Empresa.objects.all()
        tempEmpresas = []
        for i in range(len(empresas)):
            tempEmpresas.append(EmpresaDictionary(empresas[i]))
        empresas = tempEmpresas

        envase = Envase.objects.all()
        tempEnvase = []
        for i in range(len(envase)):
            tempEnvase.append(EnvaseDictionary(envase[i]))
        envase = tempEnvase

        unidad = Unidad.objects.all()
        tempUnidad = []
        for i in range(len(unidad)):
            tempUnidad.append(UnidadDictionary(unidad[i]))
        unidad = tempUnidad

        medida = Medida.objects.all()
        tempMedida = []
        for i in range(len(medida)):
            tempMedida.append(MedidaDictionary(medida[i]))
        medida = tempMedida

        data = {
            "empresas" : empresas,
            "envases" : envase,
            "unidades" : unidad,
            "medides" : medida
        }
        return JsonResponse(data)


class EditarPrecioAPI(APIView):

    def post(self,validate_data):

        json_data = validate_data.data
        model_precio = Precio()
        model_precio = Precio.objects.get(id = json_data['id'])
        model_precio.precio_venta = json_data['precio_venta']
        
        json_producto = json_data.get('producto')
        model_producto = Producto.objects.get(id = json_producto['id'])
        model_producto.nombre = json_producto['nombre']
        model_producto.descripcion = json_producto['descripcion']
        model_producto.peso = json_producto['peso']

        json_medida = json_producto.get('medida')
        model_medida = Medida.objects.get(id = json_medida['id'])
        model_producto.medida = model_medida

        json_envase = json_producto.get('envase')
        model_envase = Envase.objects.get(id = json_envase['id'])
        model_producto.envase = model_envase

        json_empresa = json_producto.get('empresa')
        model_empresa = Empresa.objects.get(id = json_empresa['id'])
        model_producto.empresa = model_empresa
        model_producto.save()

        model_precio.producto = model_producto
        model_precio.save()

        print(model_producto)
        res={"respuesta":True}
        return Response(res, status = status.HTTP_201_CREATED)

class AgregarPrecioAPI(APIView):

    def post(self,validate_data):
        json_data = validate_data.data
        model_precio = Precio()
        #model_precio = Precio.objects.get(id = json_data['id'])
        model_precio.precio_venta = json_data['precio_venta']
        model_precio.precio_compra = json_data['precio_venta']
        model_precio.cantidad = json_data['cantidad']
        model_precio.modificado = timezone.now()
        
        json_producto = json_data.get('unidad')
        model_unidad = Unidad.objects.get(id = json_producto['id'])
        model_precio.unidad = model_unidad

        
        json_producto = json_data.get('producto')
        #model_producto = Producto.objects.get(id = json_producto['id'])
        model_producto = Producto()
        model_producto.cod = json_producto['cod']
        model_producto.nombre = json_producto['nombre']
        model_producto.descripcion = json_producto['descripcion']
        model_producto.peso = json_producto['peso']
        model_producto.modificado = timezone.now()

        json_medida = json_producto.get('medida')
        model_medida = Medida.objects.get(id = json_medida['id'])
        model_producto.medida = model_medida

        json_envase = json_producto.get('envase')
        model_envase = Envase.objects.get(id = json_envase['id'])
        model_producto.envase = model_envase

        json_empresa = json_producto.get('empresa')
        model_empresa = Empresa.objects.get(id = json_empresa['id'])
        model_producto.empresa = model_empresa
        model_producto.save()

        model_precio.producto = model_producto
        model_precio.save()

        print(model_producto)
        res={"respuesta":True}
        return Response(res, status = status.HTTP_201_CREATED)


class CsvFile(APIView):
    def get(self,request):
        with open('names.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Type','SKU','Name','Published','Visibility in catalog','Description','Regular price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            precio = Precio.objects.all()
            #tempEnvase = []
            #for i in range(len(precio)):
            #    tempEnvase.append(EnvaseDictionary(envase[i].id))
            #envase = tempEnvase
            for index, c in enumerate(precio):
                peso = 0.0
                parte_decimal, parte_entera = math.modf(c.producto.peso)
                if parte_decimal == 0:
                    peso = int(parte_entera)
                else:
                    peso = c.producto.peso 

                a,b = 'áéíóúü','aeiouu'
                trans = str.maketrans(a,b)
                nombre = c.producto.nombre
                nombre = nombre.translate(trans) + ' X '+ str(peso) + ' ' + c.producto.medida.nombre
                descripcion = c.producto.descripcion
                writer.writerow({'Type':'simple',
                                'SKU':c.producto.cod,
                                'Name':nombre,
                                'Published':'1',
                                'Visibility in catalog':'visible',
                                'Description':descripcion,
                                'Regular price':c.precio_venta})
        res={"inicioHora":timezone.now()}        
        return Response(res)
