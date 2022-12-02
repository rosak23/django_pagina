from django.contrib import admin
from pagina.models import Formulario

# Register your models here.
@admin.register(Formulario)
class Formulario(admin.ModelAdmin):
    list_display = ('nombre', 'empresa', 'email', 'telefono', 'ciudad', 'rubro', 'soporte_actual', 'facturacion_mensual', 'descripcion')
