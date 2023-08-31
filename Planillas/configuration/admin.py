from django.contrib import admin
from .models import (
    Ugel,
    Cargo,
    RegimenLaboral,
    TipoServidor,
    AFP,
    Banco,
    RegimenPensionario,
    Haber,
    Descuento,
    Periodo,
    ComisionAFP,
    TipoPlanilla,
)

class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('periodo', 'es_adicional')
    readonly_fields = ('periodo_actual', 'periodo',)

admin.site.register(Ugel)
admin.site.register(Cargo)
admin.site.register(RegimenLaboral)
admin.site.register(TipoServidor)
admin.site.register(AFP)
admin.site.register(Banco)
admin.site.register(RegimenPensionario)
admin.site.register(Haber)
admin.site.register(Descuento)
admin.site.register(Periodo, PeriodoAdmin)
admin.site.register(ComisionAFP)
admin.site.register(TipoPlanilla)