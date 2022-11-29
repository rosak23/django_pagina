from django.db import models

opcion_soporte_actual = [
    ('Planilla Electroníca?', 'Planilla Electroníca?'),
    ('Tengo un sistema pero no satizface mis necesidades', 'Tengo un sistema pero no satizface mis necesidades'),
    ('No utilizo ningun sistema', 'No utilizo ningun sistema'),
    ('Mala calidad de soporte técnico', 'Mala calidad de soporte técnico'),
    ('Necesito un sistema a medida', 'Necesito un sistema a medida'),
]

facturacion_mensual = [
    ('Facturación Anual? ', 'Facturación Anual? '),
    ('250 Mill a 400 Mill', '250 Mill a 400 Mill'),
    ('450 Mill a 750 Mill', '450 Mill a 750 Mill'),
    ('800 Mill a 1200 Mill', '800 Mill a 1200 Mill'),
    ('1500 Mill a 300 Mill', '1500 Mill a 300 Mill'),
]


# Create your models here.
class Formulario(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    empresa = models.CharField(max_length=100, verbose_name='Empresa')
    email = models.EmailField(max_length=100, verbose_name='Email')
    telefono = models.CharField(max_length=20, verbose_name='Teléfono')
    ciudad = models.CharField(max_length=150, verbose_name='Ciudad')
    soporte_actual = models.TextField(max_length=150, verbose_name='Soporte Actual',
                                      blank=True, choices=opcion_soporte_actual, default='Cuál es tu necesidad?')
    facturacion_mensual = models.CharField(max_length=60, verbose_name='Facturación Anual',
                                           blank=True, null=True, choices=facturacion_mensual,
                                           default='Facturación Anual ')
    descripcion = models.TextField(max_length=500, verbose_name='Decripción')

    class Meta:
        db_table = 'formulario'
