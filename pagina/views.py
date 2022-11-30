from django.shortcuts import render, redirect
from .models import Formulario
from .forms import FormularioForm


def vistaIndex(request):
    return render(request, 'paginas/index.html')


# vista formulario
def portafolio(request):
    return render(request, 'paginas/portafolio.html')


def nuestro_servicio(request):
    return render(request, 'paginas/nuestro_servicio.html')


def insertarFormulario(request):
    # contex = {}
    # template_name = 'registrarFormulario.html'
    # if request.method == "POST":
    #     form = FormularioForm(request.POST)
    #     if form.is_valid():
    #         nombre = form.cleaned_data.get('nombre')
    #         empresa = form.cleaned_data.get('empresa')
    #         email = form.cleaned_data.get('email')
    #         telefono = form.cleaned_data.get('telefono')
    #         ciudad = form.cleaned_data.get('ciudad')
    #         soporte_actual = form.cleaned_data.get('soporte_actual')
    #         facturacion_mensual = form.cleaned_data.get('facturacion_mensual')
    #         descripcion = form.cleaned_data.get('descripcion')
    #         registrar = Formulario.objects.create(
    #             nombre=nombre,
    #             empresa=empresa,
    #             email=email,
    #             telefono=telefono,
    #             ciudad=ciudad,
    #             soporte_actual=soporte_actual,
    #             facturacion_mensual=facturacion_mensual,
    #             descripcion=descripcion
    #         )
    #         registrar.save()
    # else:
    #     form = FormularioForm()
    # contex['form'] = form
    # return render(request, template_name, contex)

    formulario = FormularioForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('index')
    return render(request, 'paginas/registrarFormulario.html', {'formulario': formulario})


def producto(request):
    return render(request, 'paginas/producto.html')