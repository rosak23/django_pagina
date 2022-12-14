# Generated by Django 3.2.6 on 2022-11-30 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0004_alter_formulario_facturacion_mensual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='facturacion_mensual',
            field=models.CharField(choices=[('Facturación Anual en Gs? ', 'Facturación Anual en Gs? '), ('Más de 300 Mill', 'Más de 300 Mill'), ('Más de 500 Mill', 'Más de 500 Mill'), ('Más de 750 Mill', 'Más de 750 Mill'), ('Más de 1000 Mill', 'Más de 1000 Mill')], default='Facturación Anual en Gs? ', max_length=60, verbose_name='Facturación Anual'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='soporte_actual',
            field=models.TextField(choices=[('Soporte Actual?', 'Soporte Actual?'), ('No utilizo ningun sistema', 'No utilizo ningun sistema'), ('Planilla Electroníca Excel, Otros', 'Planilla Electroníca Excel, Otros'), ('Tengo un sistema pero no satizface mis necesidades', 'Tengo un sistema pero no satizface mis necesidades'), ('Mejor calidad de soporte técnico', 'Mejor calidad de soporte técnico'), ('Necesito un sistema a medida para mi Empresa', 'Necesito un sistema a medida para mi Empresa'), ('Otros', 'Otros')], default='Soporte Actual?', max_length=150, verbose_name='Soporte Actual'),
        ),
    ]
