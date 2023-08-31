from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models import Max


import configuration.models as configuration


class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class Persona(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True,
        related_name='persona'
    )

    TIPO_DOCUMENTO_CHOICES = [
        ('DNI', 'DNI'),
        ('CET', 'Carnet de extranjería'),
        ('PAS', 'Pasaporte')
    ]

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro')
    ]

    tipo_documento = models.CharField(
        max_length=20,
        choices=TIPO_DOCUMENTO_CHOICES,
        default='DNI',
        verbose_name='Tipo de Documento'
    )
    numero_documento = models.CharField(
        max_length=8, unique=True, db_index=True,
        verbose_name='Número de Documento'
    )
    paterno = models.CharField(
        max_length=45, blank=True, verbose_name='Apellido Paterno')
    materno = models.CharField(
        max_length=45, blank=True, verbose_name='Apellido Materno')
    nombres = models.CharField(
        max_length=45, blank=True, verbose_name='Nombres')
    fecha_nacimiento = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Nacimiento')
    sexo = models.CharField(
        max_length=1, choices=SEXO_CHOICES, verbose_name='Sexo')
    direccion = models.CharField(
        max_length=100, blank=True, verbose_name='Dirección')
    email = models.CharField(max_length=45, blank=True, verbose_name='Email')

    def __str__(self):
        return f'{self.nombres} {self.paterno} {self.materno}'

    class Meta:
        db_table = 'persona'
        ordering = ['paterno', 'materno', 'nombres']
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'


class Empleado(models.Model):
    SITUACION_CHOICES = [
        ('HAB', 'Habilitado'),
        ('LSG', 'Licencia sin goce'),
        ('LCG', 'Licencia con goce'),
        ('DES', 'Desabilitado'),
        ('VAC', 'Vacaciones')
    ]
    ugel = models.ForeignKey(
        configuration.Ugel, on_delete=models.CASCADE, verbose_name='UGEL')
    persona = models.ForeignKey(
        Persona, on_delete=models.CASCADE, verbose_name='Persona', related_name='empleados')
    situacion = models.CharField(
        max_length=20, null=True, default='HAB', choices=SITUACION_CHOICES,
        verbose_name='Situación'
    )
    dias_licencia = models.IntegerField(
        null=True, blank=True, verbose_name='Días de Licencia', default=0)
    fecha_ini_licencia = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Inicio de Licencia')
    tiempo_servicios = models.CharField(
        max_length=6, blank=True, verbose_name='Tiempo de Servicios')
    dias_laborados = models.IntegerField(
        null=True, blank=True, verbose_name='Días Laborados', default=30)
    cargo = models.ForeignKey(
        configuration.Cargo, on_delete=models.CASCADE, verbose_name='Cargo', related_name='empleados')
    fecha_ingreso = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Ingreso')
    fecha_cese = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Cese')
    documento_contrato = models.CharField(
        max_length=45, blank=True, verbose_name='Documento de Contrato')
    documento_cese = models.CharField(
        max_length=45, blank=True, verbose_name='Documento de Cese')
    regimen_laboral = models.ForeignKey(
        configuration.RegimenLaboral, on_delete=models.CASCADE, verbose_name='Régimen Laboral'
    )
    tipo_servidor = models.ForeignKey(
        configuration.TipoServidor, on_delete=models.CASCADE, verbose_name='Tipo de Servidor')
    regimen_pensionario = models.ForeignKey(
        configuration.RegimenPensionario, on_delete=models.CASCADE, verbose_name='Régimen Pensionario'
    )
    afp = models.ForeignKey(configuration.AFP, on_delete=models.CASCADE, verbose_name='AFP')
    cuspp = models.CharField(max_length=12, blank=True, verbose_name='CUSPP')
    fecha_afiliacion = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Afiliación')
    fecha_devengue = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Devengue')
    codigo_nexus = models.CharField(
        max_length=10, blank=True, verbose_name='Código Nexus')
    jornada_laboral = models.IntegerField(
        null=True, blank=True, verbose_name='Jornada Laboral')
    descuentos_dias = models.IntegerField(
        null=True, blank=True, verbose_name='Descuentos en Días', default=0)
    descuentos_horas = models.IntegerField(
        null=True, blank=True, verbose_name='Descuentos en Horas', default=0)
    descuentos_minutos = models.IntegerField(
        null=True, blank=True, verbose_name='Descuentos en Minutos', default=0)
    leyenda_permanente = models.CharField(
        max_length=45, blank=True, verbose_name='Leyenda Permanente')
    leyenda_mensual = models.CharField(
        max_length=45, blank=True, verbose_name='Leyenda Mensual')
    banco = models.ForeignKey(
        configuration.Banco, on_delete=models.CASCADE, verbose_name='Banco')
    numero_cuenta = models.CharField(
        max_length=45, blank=True, verbose_name='Número de Cuenta')
    ruc = models.CharField(max_length=11, blank=True, verbose_name='RUC')

    def __str__(self):
        return f'{self.persona.nombres} {self.persona.paterno} {self.persona.materno} - {self.cargo.nombre_cargo} - {self.fecha_ingreso} - {self.fecha_cese}'

    class Meta:
        db_table = 'empleado'
        ordering = ['id']
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'


class HaberEmpleado(models.Model):
    trabajador = models.ForeignKey(
        Empleado,
        on_delete=models.CASCADE,
        verbose_name='Trabajador',
        related_name='haberes',
        null=True,
        blank=True
    )
    haber = models.ForeignKey(
        configuration.Haber, on_delete=models.CASCADE, verbose_name='Haber del Trabajador')
    monto_haber = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Monto de Haber'
    )
    periodo_inicial = models.CharField(
        max_length=6, blank=True, verbose_name='Periodo Inicial')
    periodo_final = models.CharField(
        max_length=6, blank=True, verbose_name='Periodo Final')
    correlativo = models.IntegerField(
        verbose_name='Correlativo', editable=False, null=True, blank=True)

    estado = models.BooleanField(verbose_name='Estado', default=True)

    def __str__(self):
        return f'{self.correlativo} - {self.trabajador} - {self.haber.descripcion} - {self.monto_haber}'

    class Meta:
        db_table = 'haberes_empleados'
        verbose_name = 'Haber del Empleado'
        verbose_name_plural = 'Haberes de los Empleados'
        ordering = ['haber', 'correlativo']

    def save(self, *args, **kwargs):
        if not self.pk:
            # Obtener el último correlativo para el mismo haber
            ultimo_correlativo = HaberEmpleado.objects.filter(
                haber=self.haber).aggregate(Max('correlativo'))['correlativo__max']

            if ultimo_correlativo is not None:
                # Si hay un correlativo anterior, incrementar en 1
                self.correlativo = ultimo_correlativo + 1
            else:
                # Si no hay correlativos anteriores, asignar 1
                self.correlativo = 1

        super().save(*args, **kwargs)


class DescuentoEmpleado(models.Model):
    trabajador = models.ForeignKey(
        Empleado,
        on_delete=models.CASCADE,
        verbose_name='Trabajador',
        related_name='descuentos',
        null=True,
        blank=True
    )
    descuento = models.ForeignKey(
        configuration.Descuento, on_delete=models.CASCADE, verbose_name='Descuento del Trabajador')
    monto_descuento = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Monto de Descuento'
    )
    periodo_inicial = models.CharField(
        max_length=6, blank=True, verbose_name='Periodo Inicial')
    periodo_final = models.CharField(
        max_length=6, blank=True, verbose_name='Periodo Final')
    correlativo = models.IntegerField(
        verbose_name='Correlativo', editable=False, null=True, blank=True)
    estado = models.BooleanField(verbose_name='Estado', default=True)

    def __str__(self):
        return self.correlativo + self.trabajador + self.descuento.descripcion

    class Meta:
        db_table = 'descuentos_empleados'
        verbose_name = 'Descuento del Empleado'
        verbose_name_plural = 'Descuentos de los Empleados'
        ordering = ['descuento', 'correlativo']

    def save(self, *args, **kwargs):
        if not self.pk:
            # Obtener el último correlativo para el mismo haber
            ultimo_correlativo = DescuentoEmpleado.objects.filter(
                Descuento=self.descuento).aggregate(Max('correlativo'))['correlativo__max']

            if ultimo_correlativo is not None:
                # Si hay un correlativo anterior, incrementar en 1
                self.correlativo = ultimo_correlativo + 1
            else:
                # Si no hay correlativos anteriores, asignar 1
                self.correlativo = 1

        super().save(*args, **kwargs)


class Beneficiario(models.Model):
    empleado = models.ForeignKey(
        Empleado, on_delete=models.CASCADE, verbose_name='Empleado', related_name='beneficiarios')
    persona = models.ForeignKey(
        Persona, on_delete=models.CASCADE, verbose_name='Persona')
    relacion_trabajador = models.CharField(
        max_length=45, blank=True, verbose_name='Relación del Trabajador')
    documento_descuento = models.CharField(
        max_length=45, blank=True, verbose_name='Documento de Descuento')
    numero_cuenta = models.CharField(
        max_length=11, blank=True, verbose_name='Número de Cuenta')

    TIPO_DESCUENTO_CHOICES = [
        ('MF', 'Monto Fijo'),
        ('DP', 'Descuento Porcentual')
    ]

    tipo_descuento = models.CharField(
        max_length=2,
        choices=TIPO_DESCUENTO_CHOICES,
        default='MF',
        verbose_name='Tipo de Descuento'
    )
    descuento_fijo = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Descuento Fijo'
    )
    porcentaje_descuento = models.IntegerField(
        null=True, blank=True, verbose_name='Porcentaje de Descuento')
    fecha_inicio = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Inicio')
    fecha_fin = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Fin')
    estado = models.BooleanField(
        verbose_name='Estado', default=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    banco = models.ForeignKey(
        configuration.Banco, on_delete=models.CASCADE, verbose_name='Banco')

    def __str__(self):
        return f'{self.persona.nombres} {self.persona.paterno} {self.persona.materno}'

    class Meta:
        db_table = 'beneficiario'
        ordering = ['id']
        verbose_name = 'Beneficiario'
        verbose_name_plural = 'Beneficiarios'


class Auditoria(models.Model):
    fecha = models.DateTimeField(null=True, blank=True, verbose_name='Fecha')
    descripcion = models.CharField(
        max_length=150, blank=True, verbose_name='Descripción')
    persona = models.ForeignKey(
        Persona, on_delete=models.CASCADE, verbose_name='Persona')

    def __str__(self):
        return self.descripcion

    class Meta:
        db_table = 'auditoria'
        ordering = ['id']
        verbose_name = 'Auditoría'
        verbose_name_plural = 'Auditorías'




class Remuneracion(models.Model):
    total_haberes = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Total de Haberes'
    )
    total_descuentos = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Total de Descuentos'
    )
    essalud = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='ESSALUD'
    )
    emitio_boleta = models.SmallIntegerField(
        null=True, blank=True, verbose_name='Emisión de Boleta')
    trabajador = models.ForeignKey(Empleado, on_delete=models.CASCADE,verbose_name='Trabajador', related_name='remuneraciones', null=True, blank=True)
    tipo_planilla = models.ForeignKey(
        configuration.TipoPlanilla, on_delete=models.CASCADE, verbose_name='Tipo de Planilla')
    periodo = models.ForeignKey(
        configuration.Periodo, on_delete=models.CASCADE, verbose_name='Período')
    ugel = models.ForeignKey(
        configuration.Ugel, on_delete=models.CASCADE, verbose_name='UGEL')

    def __str__(self):
        return f'{self.trabajador.persona.nombres} {self.trabajador.persona.paterno} {self.trabajador.persona.materno} - {self.periodo}'


    class Meta:
        db_table = 'remuneracion'
        ordering = ['id']
        verbose_name = 'Remuneración'
        verbose_name_plural = 'Remuneraciones'


class RemuneracionBeneficiario(models.Model):
    beneficiario = models.ForeignKey( Beneficiario, on_delete=models.CASCADE, verbose_name='Beneficiario')
    periodo = models.ForeignKey(configuration.Periodo, on_delete=models.CASCADE, verbose_name='Período')
    monto = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Monto')

    def __str__(self):
        return f'{self.beneficiario.persona.nombres} {self.beneficiario.persona.paterno} {self.beneficiario.persona.materno} - {self.periodo}'

    class Meta:
        db_table = 'remuneracion_beneficiario'
        ordering = ['id']
        verbose_name = 'Remuneración del Beneficiario'
        verbose_name_plural = 'Remuneraciones de los Beneficiarios'