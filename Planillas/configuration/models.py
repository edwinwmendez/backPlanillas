from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Ugel(models.Model):
    nombre_ugel = models.CharField(
        max_length=100, verbose_name='Nombre de Ugel')
    nombre_corto = models.CharField(
        max_length=25, verbose_name='Nombre Corto', null=True, blank=True)

    def __str__(self):
        return self.nombre_corto

    class Meta:
        db_table = 'ugel'
        ordering = ['nombre_ugel']
        verbose_name = 'UGEL'
        verbose_name_plural = 'UGELs'


class Cargo(models.Model):
    nombre_cargo = models.CharField(
        max_length=45, verbose_name='Nombre de Cargo')

    def __str__(self):
        return self.nombre_cargo

    class Meta:
        db_table = 'cargo'
        ordering = ['nombre_cargo']
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'


class RegimenLaboral(models.Model):
    nombre_regimen_laboral = models.CharField(
        max_length=45, verbose_name='Nombre de Régimen Laboral')

    def __str__(self):
        return self.nombre_regimen_laboral

    class Meta:
        db_table = 'regimen_laboral'
        ordering = ['nombre_regimen_laboral']
        verbose_name = 'Régimen Laboral'
        verbose_name_plural = 'Regímenes Laborales'


class TipoServidor(models.Model):
    nombre_tipo_servidor = models.CharField(
        max_length=45, verbose_name='Nombre de Tipo de Servidor')

    def __str__(self):
        return self.nombre_tipo_servidor

    class Meta:
        db_table = 'tipo_servidor'
        ordering = ['nombre_tipo_servidor']
        verbose_name = 'Tipo de Servidor'
        verbose_name_plural = 'Tipos de Servidores'


class AFP(models.Model):
    nombre_afp = models.CharField(max_length=45, verbose_name='Nombre de AFP')

    def __str__(self):
        return self.nombre_afp

    class Meta:
        db_table = 'afp'
        ordering = ['nombre_afp']
        verbose_name = 'AFP'
        verbose_name_plural = 'AFPs'


class Banco(models.Model):
    nombre_banco = models.CharField(
        max_length=45, verbose_name='Nombre de Banco')

    def __str__(self):
        return self.nombre_banco

    class Meta:
        db_table = 'banco'
        ordering = ['nombre_banco']
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'


class RegimenPensionario(models.Model):
    nombre_regimen_pensionario = models.CharField(
        max_length=45, verbose_name='Nombre de Régimen Pensionario')

    def __str__(self):
        return self.nombre_regimen_pensionario

    class Meta:
        db_table = 'regimen_pensionario'
        ordering = ['nombre_regimen_pensionario']
        verbose_name = 'Régimen Pensionario'
        verbose_name_plural = 'Regímenes Pensionarios'


class Haber(models.Model):
    TIPO_CHOICES = [
        ('SUELDO', 'Sueldo'),
        ('BONIFICACION', 'Bonificación'),
        ('DEDUCCION', 'Deducción'),
        ('BENEFICIOS_SOCIALES', 'Beneficios Sociales')
    ]
    codigo_haber = models.CharField(
        max_length=4, verbose_name='Código de Haber', unique=True, null=True, blank=True, help_text='Código de Haber')
    descripcion = models.CharField(
        max_length=45, verbose_name='Descripción', null=True, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES,
                            default='SUELDO', verbose_name='Tipo de Haber', null=True, blank=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        db_table = 'haber'
        ordering = ['descripcion']
        verbose_name = 'Haber'
        verbose_name_plural = 'Haberes'


class Descuento(models.Model):
    TIPO_CHOICES = [
        ('DEDUCCION', 'Deducción'),
        ('APORTE', 'Aporte'),
        ('OTRO', 'Otro')
    ]
    codigo_descuento = models.CharField(
        max_length=4, verbose_name='Código de Descuento', unique=True, null=True, blank=True, help_text='Código de Descuento')
    descripcion = models.CharField(
        max_length=45, verbose_name='Descripción', null=True, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='DEDUCCION',
                            verbose_name='Tipo de Descuento', null=True, blank=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        db_table = 'descuento'
        ordering = ['descripcion']
        verbose_name = 'Descuento'
        verbose_name_plural = 'Descuentos'


class Periodo(models.Model):
    mes = models.CharField(max_length=2, blank=True, verbose_name='Mes')
    anio = models.CharField(max_length=4, blank=True, verbose_name='Año')
    periodo = models.CharField(
        max_length=6, blank=True, verbose_name='Periodo', editable=False)
    es_adicional = models.BooleanField(
        default=False, verbose_name='¿Es adicional?')
    periodo_actual = models.CharField(
        max_length=6, blank=True, verbose_name='Periodo Actual', editable=False, null=True, default=None)

    def __str__(self):
        return f'{self.periodo} - {self.mes}/{self.anio}'

    def save(self, *args, **kwargs):
        if not self.periodo:
            # Generar el valor del campo periodo a partir de mes y anio
            self.periodo = f'{self.anio}{self.mes}'

        if not self.es_adicional:
            # Actualizar el campo periodo_actual con el valor del último período principal
            last_principal_periodo = Periodo.objects.filter(
                es_adicional=False).order_by('-id').first()
            self.periodo_actual = last_principal_periodo.periodo if last_principal_periodo else None
            print(last_principal_periodo)

        # Validar si ya existe un periodo principal con la misma combinación de mes y año
        if not self.es_adicional and Periodo.objects.filter(mes=self.mes, anio=self.anio, es_adicional=False).exists():
            raise ValidationError(
                'Ya existe un período principal para este mes y año.')

        super().save(*args, **kwargs)

    class Meta:
        db_table = 'periodo'
        ordering = ['anio', 'mes']
        verbose_name = 'Período'
        verbose_name_plural = 'Períodos'

    class Meta:
        db_table = 'periodo'
        ordering = ['anio', 'mes']
        verbose_name = 'Período'
        verbose_name_plural = 'Períodos'


class ComisionAFP(models.Model):
    pension = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Pensión'
    )
    seguro = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Seguro'
    )
    comision = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Comisión'
    )
    total = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Total'
    )
    afp = models.ForeignKey(AFP, on_delete=models.CASCADE, verbose_name='AFP')
    periodo = models.ForeignKey(
        Periodo, on_delete=models.CASCADE, verbose_name='Período')

    def __str__(self):
        return f'{self.afp} - {self.periodo}'

    def save(self, *args, **kwargs):
        self.total = self.pension + self.seguro + self.comision
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'comision_afp'
        ordering = ['id']
        verbose_name = 'Comisión AFP'
        verbose_name_plural = 'Comisiones AFP'


class TipoPlanilla(models.Model):
    nombre_tipo_planilla = models.CharField(
        max_length=45, blank=True, verbose_name='Nombre de Tipo de Planilla')

    def __str__(self):
        return self.nombre_tipo_planilla

    class Meta:
        db_table = 'tipo_planilla'
        ordering = ['nombre_tipo_planilla']
        verbose_name = 'Tipo de Planilla'
        verbose_name_plural = 'Tipos de Planilla'


class FuentePlanilla(models.Model):
    nombre_fuente_planilla = models.CharField(
        max_length=45, blank=True, verbose_name='Nombre de Fuente de Planilla')
    tipo_planilla = models.ForeignKey(
        TipoPlanilla, on_delete=models.CASCADE, verbose_name='Tipo de Planilla', null=True, blank=True)

    def __str__(self):
        return self.nombre_fuente_planilla

    class Meta:
        db_table = 'fuente_planilla'
        ordering = ['nombre_fuente_planilla']
        verbose_name = 'Fuente de Planilla'
        verbose_name_plural = 'Fuentes de Planilla'