from django.urls import path
from Contribuyente.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path ('contribuyente/',                 contribuyente,                      name='contribuyente'            ),
    path ('leerContribuyentes/',            leerContribuyentes,                 name ='leerContribuyentes'      ),
    path ('editarContribuyente/<cuit>',     editarContribuyente,                name ='editarContribuyente'     ),
    path ('resultadoBusquedaContribuyente', resultadosBusquedaContribuyente,    name = 'resultadosBusquedaContribuyente'),
    path ('empleado/',                      empleado,                           name ='empleado'                ),
    path ('leerEmpleados/',                 leerEmpleados,                      name ='leerEmpleados'           ),
    path ('editarEmpleado/<cuit>',          editarEmpleado,                     name= 'editarEmpleado'          ),
    path ('concepto/',                      concepto,                           name ='concepto'                ),
    path ('leerConceptos/',                 leerConceptos,                      name ='leerConceptos'            ),
    path("", inicio, name='inicio'),
]

