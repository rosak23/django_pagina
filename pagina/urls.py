from django.urls import path
from .import views

urlpatterns = [
    path('', views.vistaIndex),
    path('presupuesto', views.insertarFormulario, name='presupuesto'),
    # path('nuestro_servicio', views.nuestro_servicio, name='nuestro_servicio'),
]
