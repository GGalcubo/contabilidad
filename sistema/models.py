from django.db import models

# Create your models here.
class TipoGasto(models.Model):
    tipo = models.CharField(max_length=200)

    def __str__(self):
        return self.tipo

class Gasto(models.Model):
    fecha = models.DateField('fecha')
    tipo = models.ForeignKey(TipoGasto, on_delete=models.SET_NULL, null=True, blank=True)
    concepto = models.CharField(max_length=200)
    monto = models.IntegerField(default=0)

    def __str__(self):
        return 'fecha: ' + self.fecha + ' tipo: ' + self.tipo 

