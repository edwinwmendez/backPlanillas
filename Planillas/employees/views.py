from rest_framework import viewsets
from .models import (
    Persona, Empleado, Beneficiario,
    Auditoria, Remuneracion,
    RemuneracionBeneficiario
)
from .serializers import (
    PersonaSerializer, EmpleadoSerializer, BeneficiarioSerializer, AuditoriaSerializer, RemuneracionSerializer,
    RemuneracionBeneficiarioSerializer
)


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer


class BeneficiarioViewSet(viewsets.ModelViewSet):
    queryset = Beneficiario.objects.all()
    serializer_class = BeneficiarioSerializer



class AuditoriaViewSet(viewsets.ModelViewSet):
    queryset = Auditoria.objects.all()
    serializer_class = AuditoriaSerializer


class RemuneracionViewSet(viewsets.ModelViewSet):
    queryset = Remuneracion.objects.all()
    serializer_class = RemuneracionSerializer


class RemuneracionBeneficiarioViewSet(viewsets.ModelViewSet):
    queryset = RemuneracionBeneficiario.objects.all()
    serializer_class = RemuneracionBeneficiarioSerializer