from rest_framework import viewsets
from .models import (
     Ugel, Cargo, RegimenLaboral, TipoServidor, AFP, Banco,
    RegimenPensionario, Haber, Descuento, 
    Periodo, ComisionAFP, TipoPlanilla, FuentePlanilla
)
from .serializers import (
    UgelSerializer, CargoSerializer,
    RegimenLaboralSerializer, TipoServidorSerializer, AFPSerializer,
    BancoSerializer, RegimenPensionarioSerializer,
    HaberSerializer, DescuentoSerializer,
    PeriodoSerializer, ComisionAFPSerializer,
    TipoPlanillaSerializer, FuentePlanillaSerializer
)

# Create your views here.
class UgelViewSet(viewsets.ModelViewSet):
    queryset = Ugel.objects.all()
    serializer_class = UgelSerializer


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


class RegimenLaboralViewSet(viewsets.ModelViewSet):
    queryset = RegimenLaboral.objects.all()
    serializer_class = RegimenLaboralSerializer


class TipoServidorViewSet(viewsets.ModelViewSet):
    queryset = TipoServidor.objects.all()
    serializer_class = TipoServidorSerializer


class AFPViewSet(viewsets.ModelViewSet):
    queryset = AFP.objects.all()
    serializer_class = AFPSerializer


class BancoViewSet(viewsets.ModelViewSet):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer


class RegimenPensionarioViewSet(viewsets.ModelViewSet):
    queryset = RegimenPensionario.objects.all()
    serializer_class = RegimenPensionarioSerializer


class HaberViewSet(viewsets.ModelViewSet):
    queryset = Haber.objects.all()
    serializer_class = HaberSerializer


class DescuentoViewSet(viewsets.ModelViewSet):
    queryset = Descuento.objects.all()
    serializer_class = DescuentoSerializer


class PeriodoViewSet(viewsets.ModelViewSet):
    queryset = Periodo.objects.all()
    serializer_class = PeriodoSerializer


class ComisionAFPViewSet(viewsets.ModelViewSet):
    queryset = ComisionAFP.objects.all()
    serializer_class = ComisionAFPSerializer


class TipoPlanillaViewSet(viewsets.ModelViewSet):
    queryset = TipoPlanilla.objects.all()
    serializer_class = TipoPlanillaSerializer


class FuentePlanillaViewSet(viewsets.ModelViewSet):
    queryset = FuentePlanilla.objects.all()
    serializer_class = FuentePlanillaSerializer