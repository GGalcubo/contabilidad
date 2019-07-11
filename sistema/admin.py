from django.contrib import admin
from .models import TipoGasto, Gasto
# Register your models here.
class GastoAdmin(admin.ModelAdmin):
    list_display =  ('fecha', 'tipo', 'concepto', 'monto')
    list_filter = ['fecha', 'tipo']
    search_fields = ['concepto']

admin.site.register(TipoGasto)
admin.site.register(Gasto,GastoAdmin)