# Generated by Django 4.2.4 on 2023-08-31 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AFP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_afp', models.CharField(max_length=45, verbose_name='Nombre de AFP')),
            ],
            options={
                'verbose_name': 'AFP',
                'verbose_name_plural': 'AFPs',
                'db_table': 'afp',
                'ordering': ['nombre_afp'],
            },
        ),
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_banco', models.CharField(max_length=45, verbose_name='Nombre de Banco')),
            ],
            options={
                'verbose_name': 'Banco',
                'verbose_name_plural': 'Bancos',
                'db_table': 'banco',
                'ordering': ['nombre_banco'],
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cargo', models.CharField(max_length=45, verbose_name='Nombre de Cargo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
                'db_table': 'cargo',
                'ordering': ['nombre_cargo'],
            },
        ),
        migrations.CreateModel(
            name='Descuento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_descuento', models.CharField(blank=True, help_text='Código de Descuento', max_length=4, null=True, unique=True, verbose_name='Código de Descuento')),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True, verbose_name='Descripción')),
                ('tipo', models.CharField(blank=True, choices=[('DEDUCCION', 'Deducción'), ('APORTE', 'Aporte'), ('OTRO', 'Otro')], default='DEDUCCION', max_length=20, null=True, verbose_name='Tipo de Descuento')),
            ],
            options={
                'verbose_name': 'Descuento',
                'verbose_name_plural': 'Descuentos',
                'db_table': 'descuento',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='Haber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_haber', models.CharField(blank=True, help_text='Código de Haber', max_length=4, null=True, unique=True, verbose_name='Código de Haber')),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True, verbose_name='Descripción')),
                ('tipo', models.CharField(blank=True, choices=[('SUELDO', 'Sueldo'), ('BONIFICACION', 'Bonificación'), ('DEDUCCION', 'Deducción'), ('BENEFICIOS_SOCIALES', 'Beneficios Sociales')], default='SUELDO', max_length=20, null=True, verbose_name='Tipo de Haber')),
            ],
            options={
                'verbose_name': 'Haber',
                'verbose_name_plural': 'Haberes',
                'db_table': 'haber',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(blank=True, max_length=2, verbose_name='Mes')),
                ('anio', models.CharField(blank=True, max_length=4, verbose_name='Año')),
                ('periodo', models.CharField(blank=True, editable=False, max_length=6, verbose_name='Periodo')),
                ('es_adicional', models.BooleanField(default=False, verbose_name='¿Es adicional?')),
                ('periodo_actual', models.CharField(blank=True, default=None, editable=False, max_length=6, null=True, verbose_name='Periodo Actual')),
            ],
            options={
                'verbose_name': 'Período',
                'verbose_name_plural': 'Períodos',
                'db_table': 'periodo',
                'ordering': ['anio', 'mes'],
            },
        ),
        migrations.CreateModel(
            name='RegimenLaboral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_regimen_laboral', models.CharField(max_length=45, verbose_name='Nombre de Régimen Laboral')),
            ],
            options={
                'verbose_name': 'Régimen Laboral',
                'verbose_name_plural': 'Regímenes Laborales',
                'db_table': 'regimen_laboral',
                'ordering': ['nombre_regimen_laboral'],
            },
        ),
        migrations.CreateModel(
            name='RegimenPensionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_regimen_pensionario', models.CharField(max_length=45, verbose_name='Nombre de Régimen Pensionario')),
            ],
            options={
                'verbose_name': 'Régimen Pensionario',
                'verbose_name_plural': 'Regímenes Pensionarios',
                'db_table': 'regimen_pensionario',
                'ordering': ['nombre_regimen_pensionario'],
            },
        ),
        migrations.CreateModel(
            name='TipoPlanilla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo_planilla', models.CharField(blank=True, max_length=45, verbose_name='Nombre de Tipo de Planilla')),
            ],
            options={
                'verbose_name': 'Tipo de Planilla',
                'verbose_name_plural': 'Tipos de Planilla',
                'db_table': 'tipo_planilla',
                'ordering': ['nombre_tipo_planilla'],
            },
        ),
        migrations.CreateModel(
            name='TipoServidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo_servidor', models.CharField(max_length=45, verbose_name='Nombre de Tipo de Servidor')),
            ],
            options={
                'verbose_name': 'Tipo de Servidor',
                'verbose_name_plural': 'Tipos de Servidores',
                'db_table': 'tipo_servidor',
                'ordering': ['nombre_tipo_servidor'],
            },
        ),
        migrations.CreateModel(
            name='Ugel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ugel', models.CharField(max_length=100, verbose_name='Nombre de Ugel')),
                ('nombre_corto', models.CharField(blank=True, max_length=25, null=True, verbose_name='Nombre Corto')),
            ],
            options={
                'verbose_name': 'UGEL',
                'verbose_name_plural': 'UGELs',
                'db_table': 'ugel',
                'ordering': ['nombre_ugel'],
            },
        ),
        migrations.CreateModel(
            name='FuentePlanilla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_fuente_planilla', models.CharField(blank=True, max_length=45, verbose_name='Nombre de Fuente de Planilla')),
                ('tipo_planilla', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configuration.tipoplanilla', verbose_name='Tipo de Planilla')),
            ],
            options={
                'verbose_name': 'Fuente de Planilla',
                'verbose_name_plural': 'Fuentes de Planilla',
                'db_table': 'fuente_planilla',
                'ordering': ['nombre_fuente_planilla'],
            },
        ),
        migrations.CreateModel(
            name='ComisionAFP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pension', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Pensión')),
                ('seguro', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Seguro')),
                ('comision', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Comisión')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total')),
                ('afp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.afp', verbose_name='AFP')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.periodo', verbose_name='Período')),
            ],
            options={
                'verbose_name': 'Comisión AFP',
                'verbose_name_plural': 'Comisiones AFP',
                'db_table': 'comision_afp',
                'ordering': ['id'],
            },
        ),
    ]