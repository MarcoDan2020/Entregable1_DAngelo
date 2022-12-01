from django.urls import path, include
from Contribuyente.views import *

urlpatterns = [
    path("contribuyente/", contribuyente, name="contribuyente"),
    '''path("cursos/", cursos, name="cursos"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("profesores/", profesores, name="profesores"),
    path("entregables/", entregables, name="entregables"),
    path("", inicio, name="inicio"),'''