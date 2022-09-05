from django.contrib import admin
from tienda.models import Cliente, Empresa,Envase,Medida,Precio,Producto,Unidad,Usuario,Venta
# Register your models here.

class MedidaAdmin(admin.ModelAdmin):
    list_display = ["nombre"]

class EnvaseAdmin(admin.ModelAdmin):
    list_display = ["nombre"]

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["cod","nombre","medida"]

admin.site.register(Cliente)
admin.site.register(Envase,EnvaseAdmin)
admin.site.register(Empresa)
admin.site.register(Medida,MedidaAdmin)
admin.site.register(Precio)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Unidad)
admin.site.register(Usuario)
admin.site.register(Venta)
