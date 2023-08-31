from rest_framework import serializers
from .models import Ugel, Cargo, RegimenLaboral, TipoServidor, AFP, Banco, RegimenPensionario,    Haber, Descuento, Periodo, ComisionAFP, TipoPlanilla, FuentePlanilla


class UgelSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Ugel.
    """
    class Meta:
        model = Ugel
        fields = '__all__'


class CargoSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Cargo.
    """
    class Meta:
        model = Cargo
        fields = '__all__'


class RegimenLaboralSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo RegimenLaboral.
    """
    class Meta:
        model = RegimenLaboral
        fields = '__all__'


class TipoServidorSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo TipoServidor.
    """
    class Meta:
        model = TipoServidor
        fields = '__all__'


class AFPSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo AFP.
    """
    class Meta:
        model = AFP
        fields = '__all__'


class BancoSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Banco.
    """
    class Meta:
        model = Banco
        fields = '__all__'


class RegimenPensionarioSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo RegimenPensionario.
    """
    class Meta:
        model = RegimenPensionario
        fields = '__all__'


class HaberSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Haber.
    """
    class Meta:
        model = Haber
        fields = '__all__'


class DescuentoSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Descuento.
    """
    class Meta:
        model = Descuento
        fields = '__all__'


class PeriodoSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Periodo.
    """
    class Meta:
        model = Periodo
        fields = '__all__'


class ComisionAFPSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo ComisionAFP.
    """
    class Meta:
        model = ComisionAFP
        fields = '__all__'


class TipoPlanillaSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo TipoPlanilla.
    """
    class Meta:
        model = TipoPlanilla
        fields = '__all__'


class FuentePlanillaSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo FuentePlanilla.
    """
    class Meta:
        model = FuentePlanilla
        fields = '__all__'
