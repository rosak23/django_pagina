from os import path
from pagina import views

urlpatterns = [
    path('', views.vistaIndex, name='index'),
]
