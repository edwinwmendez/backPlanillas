from django.urls import include, path
from rest_framework import routers
from .views import (
    PersonaViewSet, EmpleadoViewSet, BeneficiarioViewSet,AuditoriaViewSet,    RemuneracionViewSet, RemuneracionBeneficiarioViewSet
)

router = routers.DefaultRouter()
router.register('persona', PersonaViewSet)
router.register('empleado', EmpleadoViewSet)
router.register('beneficiario', BeneficiarioViewSet)
router.register('auditoria', AuditoriaViewSet)
router.register('remuneracion', RemuneracionViewSet)
router.register('remuneracion-beneficiario', RemuneracionBeneficiarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]