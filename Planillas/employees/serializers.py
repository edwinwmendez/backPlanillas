from rest_framework import serializers
from .models import Persona, Empleado, Beneficiario, Auditoria, Remuneracion, RemuneracionBeneficiario
from configuration.serializers import CargoSerializer


class PersonaSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Persona.
    """
    class Meta:
        model = Persona
        fields = '__all__'


class EmpleadoSerializer(serializers.ModelSerializer):
    persona = PersonaSerializer(read_only=True)
    cargo = CargoSerializer(read_only=True)
    """
    Serializer para el modelo Empleado.
    """
    class Meta:
        model = Empleado
        fields = '__all__'


class BeneficiarioSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Beneficiario.
    """
    class Meta:
        model = Beneficiario
        fields = '__all__'


class AuditoriaSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Auditoria.
    """
    class Meta:
        model = Auditoria
        fields = '__all__'


class RemuneracionSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Remuneracion.
    """
    class Meta:
        model = Remuneracion
        fields = '__all__'


class RemuneracionBeneficiarioSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo RemuneracionBeneficiario.
    """
    class Meta:
        model = RemuneracionBeneficiario
        fields = '__all__'
