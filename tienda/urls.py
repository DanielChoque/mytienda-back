from django.urls import path
from tienda.api import AgregarPrecioAPI, CsvFile, DatosInicialesApi, EditarPrecioAPI, PrecioApi

from tienda.views import EmpresaList, PrecioList, ProductoList, UnidadList

urlpatterns = [
    path('producto/',ProductoList.as_view(), name="producto_api_atencion"),
    path('precio/',PrecioList.as_view(), name="precio_api_atencion"),
    path('unidad/',UnidadList.as_view(), name="api_atencion"),
    
    path('precio_id/<int:id>/',PrecioApi.as_view(), name="api_precio_a"),
    path('datos_ini/',DatosInicialesApi.as_view(), name="datos_iniciales"),
    path('precio_edit/',EditarPrecioAPI.as_view(), name="api_precio_edit"),
    path('precio_add/',AgregarPrecioAPI.as_view(), name="api_precio_add"),
    path('csv_file/',CsvFile.as_view(), name="api_csv_file"),
]