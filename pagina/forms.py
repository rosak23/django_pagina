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
                  'rubro',
                  'soporte_actual',
                  'facturacion_mensual',
                  'descripcion', ]

        widgets = {
            'nombre': forms.TextInput(attrs={'Placeholder': 'Nombre', 'class': 'form-control'}),
            'empresa': forms.TextInput(attrs={'Placeholder': 'Empresa', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'Placeholder': 'Correo Electronico', 'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'Placeholder': 'Celular', 'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'Placeholder': 'Ciudad', 'class': 'form-control'}),
            'rubro': forms.TextInput(attrs={'Placeholder': 'A que rubro se dedica tú Empresa?', 'class': 'form-control'}),
            'soporte_actual': forms.Select(attrs={'Placeholder': 'Soporte Actual', 'class': 'form-control'}),
            'facturacion_mensual': forms.Select(attrs={'Placeholder': 'Facturación Mensual', 'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'Placeholder': 'Describenos las necesidades detalladamente de tu Empresa', 'class': 'form-control'}),
        }
