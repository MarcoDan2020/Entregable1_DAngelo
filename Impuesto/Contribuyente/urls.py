from django.urls import path
from Contribuyente.views import *

urlpatterns = [
    path ('contribuyente/', contribuyente, name='contribuyente'),
    path ('leerContribuyentes/', leerContribuyentes, name ='leerContribuyentes'),
    path ('editarContribuyente/', editarContribuyente, name ='editarContribuyente'),
    path ('leerEmpleados/', leerEmpleados, name ='leerEmpleados'),
    path ('concepto/', concepto, name ='concepto'),
    path ('leerConceptos/', leerConceptos, name ='leerConceptos'),


    path("", inicio, name='inicio'),
]

