import subprocess
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Planillas.settings')


# Lista de nombres de aplicaciones a crear
app_names = [
    "accounts",
    "employees",
    "payroll",
    "processes",
    "reports",
    "movements",
    "benefits",
    "configuration",
    "audit",
    "integrations",
    "help",
    "labor_regimes",
    "work_history",
    "documentation",
    "api",
    "notifications"
]


# Comando para crear una aplicación usando manage.py startapp
def create_app(app_name):
    subprocess.run(["python", "manage.py", "startapp", app_name])

# Crear todas las aplicaciones en la lista
for app_name in app_names:
    create_app(app_name)
    print(f"Aplicación {app_name} creada.")

print("Todas las aplicaciones han sido creadas.")
