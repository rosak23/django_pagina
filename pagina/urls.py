from django.urls import path
from .import views

urlpatterns = [
    path('', views.vistaIndex, name='index'),
    path('producto', views.producto, name='producto'),
    path('portafolio', views.portafolio, name='portafolio'),
    path('nuestro_servicio', views.nuestro_servicio, name='nuestro_servicio'),
    path('formulario', views.insertarFormulario, name='formulario'),
]
