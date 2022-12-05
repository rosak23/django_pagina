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
    formulario = FormularioForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('index')
    return render(request, 'paginas/registrarFormulario.html', {'formulario': formulario})


def producto(request):
    return render(request, 'paginas/producto.html')


# vista mostrar clientes
def editarSeguimiento(request):
    seguimiento = Formulario.objects.all()
    return render(request, 'paginas/mostrarCliente.html', {'seguimiento': seguimiento})
