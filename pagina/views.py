from django.http import HttpRequest
from django.shortcuts import render



# Create your views here.
from pagina.forms import FormularioForm


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
        return render(request, 'paginas/registrarFormulario.html', {'formulario': formulario})
    return render(request, 'paginas/index.html')


def producto(request):
    return render(request, 'paginas/producto.html')
