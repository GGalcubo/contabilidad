from django.contrib import admin
from .models import TipoGasto, Gasto, Estado, Factura


# Register your models here.
class GastoAdmin(admin.ModelAdmin):
    list_display =  ('fecha', 'tipo', 'estado', 'concepto', 'monto')
    list_filter = ['fecha', 'tipo', 'estado']
    search_fields = ['concepto']


class FacturaAdmin(admin.ModelAdmin):
    list_display =  ('fecha', 'numero', 'estado', 'monto')
    list_filter = ['fecha', 'numero', 'estado']
    search_fields = ['numero']


admin.site.register(TipoGasto)
admin.site.register(Estado)
admin.site.register(Factura,FacturaAdmin)
admin.site.register(Gasto,GastoAdmin)