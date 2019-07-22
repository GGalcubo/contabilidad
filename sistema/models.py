from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Estado(models.Model):
    estado = models.CharField(max_length=200)

    def __str__(self):
        return self.estado


class TipoGasto(models.Model):
    tipo = models.CharField(max_length=200)

    def __str__(self):
        return self.tipo


class Gasto(models.Model):
    fecha = models.DateField('fecha')
    tipo = models.ForeignKey(TipoGasto, on_delete=models.SET_NULL, null=True, blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True, blank=True)
    concepto = models.CharField(max_length=200)
    monto = models.IntegerField(default=0)
    comprobante = models.ImageField(upload_to='comprobante', null=True, blank=True)
    asignado = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return 'tipo: %s, asignado: %s' %(self.tipo, self.asignado) 


class Factura(models.Model):
    fecha = models.DateField('fecha')
    numero = models.CharField(max_length=200)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True, blank=True)
    monto = models.IntegerField(default=0)
    factura = models.ImageField(upload_to='facturas', null=True, blank=True)
    asignado = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.numero 
