from django.db import models

opcion_soporte_actual = [
    ('Cuál es tu necesidad?', 'Cuál es tu necesidad?'),
    ('Tengo un sistema pero no satizface mis necesidades', 'Tengo un sistema pero no satizface mis necesidades'),
    ('No utilizo ningun sistema', 'No utilizo ningun sistema'),
    ('Mal calidad de soporte tecnico', 'Mal calidad de soporte tecnico'),
    ('Necesito un sistema a medida', 'Necesito un sistema a medida'),
]

facturacion_mensual = [
    ('Facturacin Anual ', 'Facturacin Anual '),
    ( '45.000.000Gs a 90.000.000Gs', '45.000.000Gs a 90.000.000Gs'),
    ('95.000.000Gs a 150.000.000Gs', '95.000.000Gs a 150.000.000Gs'),
    ('160.000.000Gs a 250.000.000Gs', '160.000.000Gs a 250.000.000Gs'),
    ('300.000.000Gs a 450.000.000Gs', '300.000.000Gs a 450.000.000Gs'),
]

# Create your models here.
class Formulario(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    empresa = models.CharField(max_length=100, verbose_name='Empresa')
    email = models.EmailField(max_length=100, verbose_name='Email')
    telefono = models.CharField(max_length=20, verbose_name='Teléfono')
    ciudad = models.CharField(max_length=150, verbose_name='Ciudad')
    soporte_actual = models.TextField(max_length=150, verbose_name='Soporte Actual', blank=True, choices=opcion_soporte_actual, default='Cuál es tu necesidad?')
    facturacion_mensual = models.CharField(max_length=60, verbose_name='Facturación Mensual', blank=True, null=True, choices=facturacion_mensual, default='Facturacin Anual ')
    descripcion = models.TextField(max_length=500, verbose_name='Decripción')

    class Meta:
        db_table = 'formulario'
