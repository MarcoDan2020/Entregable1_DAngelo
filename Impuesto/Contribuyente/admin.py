from django.contrib import admin

# Register yofrom django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Contribuyente)
admin.site.register(Empleado)
admin.site.register(Concepto_Ingreso)

