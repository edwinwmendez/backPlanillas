from django.urls import include, path
from rest_framework import routers
from .views import (
    UgelViewSet, CargoViewSet, RegimenLaboralViewSet,
    TipoServidorViewSet, AFPViewSet, BancoViewSet, RegimenPensionarioViewSet,
    HaberViewSet, DescuentoViewSet,
    PeriodoViewSet, ComisionAFPViewSet, TipoPlanillaViewSet, FuentePlanillaViewSet,
)

router = routers.DefaultRouter()
router.register('ugel', UgelViewSet)
router.register('cargo', CargoViewSet)
router.register('regimen-laboral', RegimenLaboralViewSet)
router.register('tipo-servidor', TipoServidorViewSet)
router.register('afp', AFPViewSet)
router.register('banco', BancoViewSet)
router.register('regimen-pensionario', RegimenPensionarioViewSet)
router.register('haber', HaberViewSet)
router.register('descuento', DescuentoViewSet)
router.register('periodo', PeriodoViewSet)
router.register('comision-afp', ComisionAFPViewSet)
router.register('tipo-planilla', TipoPlanillaViewSet)
router.register('fuente-planilla', FuentePlanillaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]