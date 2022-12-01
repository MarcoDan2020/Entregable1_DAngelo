from django.urls import path
from Contribuyente.views import *

urlpatterns = [
    path ('contribuyente/', contribuyente, name='contribuyente'),
    path ('leerContribuyentes/', leerContribuyentes, name ='leerContribuyentes'),
    path("inicio/", inicio, name='inicio'),
]

