from django.db import models
opcion_soporte_actual = [
    ('Soporte Actual?', 'Soporte Actual?'),
    ('No utilizo ningún sistema', 'No utilizo ningún sistema'),
    ('Planilla Electrónica Excel, Otros', 'Planilla Electrónica Excel, Otros'),
    ('Tengo un sistema, pero no satisface mis necesidades', 'Tengo un sistema, pero no satisface mis necesidades'),
    ('Mejor calidad de soporte técnico', 'Mejor calidad de soporte técnico'),
    ('Necesito un sistema a medida para mi Empresa', 'Necesito un sistema a medida para mi Empresa'),
    ('Otros', 'Otros'),

]


facturacion_mensual = [
    ('Facturación Anual en Gs? ', 'Facturación Anual en Gs? '),
    ('Más de 300 Mill', 'Más de 300 Mill'),
    ('Más de 500 Mill', 'Más de 500 Mill'),
    ('Más de 750 Mill', 'Más de 750 Mill'),
    ('Más de 1000 Mill', 'Más de 1000 Mill'),

]

esta_seguimiento = [
    ('Nuevo', 'Nuevo'),
    ('En Atención', 'En Atención'),
    ('Cuncluido', 'Cuncluido'),
]




# Create your models here.
class Formulario(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    empresa = models.CharField(max_length=100, verbose_name='Empresa')
    email = models.EmailField(max_length=100, verbose_name='Email')
    telefono = models.CharField(max_length=20, verbose_name='Teléfono')
    ciudad = models.CharField(max_length=150, verbose_name='Ciudad')
    rubro = models.CharField(max_length=150, verbose_name='Rubro', blank=False, null=True)
    soporte_actual = models.TextField(max_length=150, verbose_name='Soporte Actual', blank=False, null=False, choices=opcion_soporte_actual, default='Soporte Actual?')
    facturacion_mensual = models.CharField(max_length=60, verbose_name='Facturación Anual', blank=False, null=False, choices=facturacion_mensual, default='Facturación Anual en Gs? ')
    descripcion = models.TextField(max_length=500, verbose_name='Decripción')
    estado = models.CharField(max_length=20, verbose_name='Estado de Venta', null=True, blank=True,
                              choices=esta_seguimiento, default='En Atención', editable=False)


    class Meta:
        db_table = 'formulario'


