from django.contrib import admin
from .models import TipoGasto, Gasto, Estado, Factura


# Register your models here.
class GastoAdmin(admin.ModelAdmin):
    list_display =  ('fecha', 'tipo', 'estado', 'concepto', 'monto', 'asignado')
    list_filter = ['fecha', 'tipo', 'estado', 'asignado']
    search_fields = ['concepto']


class FacturaAdmin(admin.ModelAdmin):
    list_display =  ('fecha', 'numero', 'estado', 'monto', 'asignado')
    list_filter = ['fecha', 'numero', 'estado', 'asignado']
    search_fields = ['numero']


admin.site.register(TipoGasto)
admin.site.register(Estado)
admin.site.register(Factura,FacturaAdmin)
admin.site.register(Gasto,GastoAdmin)