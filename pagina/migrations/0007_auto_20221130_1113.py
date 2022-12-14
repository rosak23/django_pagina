# Generated by Django 3.2.16 on 2022-11-30 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0006_alter_formulario_soporte_actual'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario',
            name='rubro',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Rubro'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='facturacion_mensual',
            field=models.CharField(choices=[('Facturación Anual en Gs? ', 'Facturación Anual en Gs? '), ('Más de 300 Mill', 'Más de 300 Mill'), ('Más de 500 Mill', 'Más de 500 Mill'), ('Más de 750 Mill', 'Más de 750 Mill'), ('Más de 1000 Mill', 'Más de 1000 Mill')], max_length=60, verbose_name='Facturación Anual'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='soporte_actual',
            field=models.TextField(choices=[('Soporte Actual?', 'Soporte Actual?'), ('No utilizo ningún sistema', 'No utilizo ningún sistema'), ('Planilla Electrónica Excel, Otros', 'Planilla Electrónica Excel, Otros'), ('Tengo un sistema, pero no satisface mis necesidades', 'Tengo un sistema, pero no satisface mis necesidades'), ('Mejor calidad de soporte técnico', 'Mejor calidad de soporte técnico'), ('Necesito un sistema a medida para mi Empresa', 'Necesito un sistema a medida para mi Empresa'), ('Otros', 'Otros')], max_length=150, verbose_name='Soporte Actual'),
        ),
    ]
