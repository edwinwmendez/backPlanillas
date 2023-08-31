import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Planillas.settings')
django.setup()

from django.contrib.auth.models import Group, Permission

# Grupo Master - Todos los permisos
master_group, _ = Group.objects.get_or_create(name='Master')
master_group.permissions.set(Permission.objects.all())

# Grupo AdministradorProcesos - Permiso para la app 'procesos' y 'reportes'
procesos_permissions = Permission.objects.filter(content_type__app_label='procesos') | \
                       Permission.objects.filter(content_type__app_label='reportes')
admin_procesos_group, _ = Group.objects.get_or_create(name='AdministradorProcesos')
admin_procesos_group.permissions.set(procesos_permissions)

# Grupo TecnicoPlanillas - Permiso para CRUD de empleados y movimientos administrativos
planillas_permissions = Permission.objects.filter(content_type__model='empleado') | \
                        Permission.objects.filter(content_type__model='movimientoadministrativo')
tecnico_planillas_group, _ = Group.objects.get_or_create(name='TecnicoPlanillas')
tecnico_planillas_group.permissions.set(planillas_permissions)

# Grupo Empleados - Puedes asignar permisos específicos si es necesario
empleados_group, _ = Group.objects.get_or_create(name='Empleados')
