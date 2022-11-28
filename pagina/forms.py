from django import forms
from .models import Formulario


class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['nombre',
                  'empresa',
                  'email',
                  'telefono',
                  'ciudad',
                  'soporte_actual',
                  'facturacion_mensual',
                  'descripcion', ]

        widgets = {
            'nombre': forms.TextInput(attrs={'Placeholder': 'Nombre'}),
            'empresa': forms.TextInput(attrs={'Placeholder': 'Empresa'}),
            'email': forms.EmailInput(attrs={'Placeholder': 'Correo Electronico'}),
            'telefono': forms.TextInput(attrs={'Placeholder': 'Celular'}),
            'ciudad': forms.TextInput(attrs={'Placeholder': 'Ciudad'}),
            'soporte_actual': forms.TextInput(attrs={'Placeholder': 'Soporte Actual'}),
            'facturacion_mensual': forms.TextInput(attrs={'Placeholder': 'Facturación Mensual'}),
            'descripcion': forms.Textarea(attrs={'Placeholder': 'Describenos para conocerte mejor'}), }
