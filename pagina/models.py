from django.db import models


# Create your models here.
class Formulario(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    empresa = models.CharField(max_length=100, verbose_name='Empresa')
    email = models.EmailField(max_length=100, verbose_name='Email')
    telefono = models.CharField(max_length=20, verbose_name='Teléfono')
    ciudad = models.CharField(max_length=150, verbose_name='Ciudad')
    soporte_actual = models.TextField(max_length=150, verbose_name='Soporte Actual')
    facturacion_mensual = models.CharField(max_length=60, verbose_name='Facturación Mensual', blank=True, null=True)
    descripcion = models.TextField(max_length=500, verbose_name='Decripción')

    class Meta:
        db_table = 'formulario'
