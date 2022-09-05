from django.db import models
from django.utils import timezone
# Create your models here.
class Cliente(models.Model):
    ci = models.CharField(null=True,max_length=16)
    nombre = models.CharField(max_length=100)
    modificado = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return "{n}".format(n = self.nombre)

class Usuario(models.Model):
    ci = models.CharField(null=True,max_length=16)
    nombre = models.CharField(max_length=100)
    modificado = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return "{n}".format(n = self.nombre)

class Medida(models.Model):
    nombre = models.CharField(null=True,max_length=16)
    modificado = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return "{n}".format(n = self.nombre)
    
class Envase(models.Model):
    nombre = models.CharField(max_length=50)
    modificado = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return "{n}".format(n = self.nombre)

class Unidad(models.Model):
    nombre = models.CharField(max_length=100)
    #unidades = models.IntegerField(default=0)
    modificado = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return "{n}".format(n = self.nombre)

class Empresa(models.Model):
    nit = models.IntegerField(default=0)
    nombre = models.CharField(max_length=100)
    elaboradopor = models.CharField(max_length=150)
    modificado = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return "{n}".format(n = self.nombre)

class Producto(models.Model):
    cod = models.CharField(max_length=30)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True) 
    #peso = models.IntegerField(default=0)
    medida = models.ForeignKey(Medida,null=True,on_delete = models.CASCADE)
    #cantidad = models.IntegerField(default=0)
    envase = models.ForeignKey(Envase,null=True,on_delete = models.CASCADE)
    empresa = models.ForeignKey(Empresa,null=True,on_delete = models.CASCADE)
    modificado = models.DateTimeField(default=timezone.now) 
    volumen = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    peso = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    def __str__(self):
        return "{n} {p}{m}".format(n = self.nombre,p = self.peso,m = self.medida)

class Precio(models.Model):    
    unidad = models.ForeignKey(Unidad,default = 1,on_delete = models.CASCADE)
    producto = models.ForeignKey(Producto,default = 1,on_delete = models.CASCADE)
    cantidad = models.IntegerField(default=1)
    precio_venta = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    precio_compra = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    modificado = models.DateTimeField(default=timezone.now) 
    def __str__(self):
        return "{p} {u} {pre}".format(p = self.producto, u = self.unidad, pre = self.precio_venta)

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente,default = 1,on_delete = models.CASCADE)
    usuario = models.ForeignKey(Usuario,default = 1,on_delete = models.CASCADE)
    #precio = models.ForeignKey(Precio,default = 1,on_delete = models.CASCADE)
    #cantidad = models.IntegerField(default=1)
    precio_total = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    efectivo = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    fecha = models.DateTimeField(default=timezone.now)
    modificado = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return "{pre} -- {c} -- {t} ".format(c = self.cantidad, t = self.total, pre = self.precio)

