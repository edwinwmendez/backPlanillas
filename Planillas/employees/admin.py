from django.contrib import admin
from .models import (
    Persona,
    Empleado,
    HaberEmpleado,
    DescuentoEmpleado,
    Beneficiario,
    Auditoria,
    Remuneracion,
    RemuneracionBeneficiario,
)

admin.site.register(Persona)
admin.site.register(Empleado)
admin.site.register(HaberEmpleado)
admin.site.register(DescuentoEmpleado)
admin.site.register(Beneficiario)
admin.site.register(Auditoria)
admin.site.register(Remuneracion)
admin.site.register(RemuneracionBeneficiario)