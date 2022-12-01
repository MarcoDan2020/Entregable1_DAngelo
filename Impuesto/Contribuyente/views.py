from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Contribuyente, Empleado
from .forms import ContribuyenteForm



def contribuyente(request):

    if request.method=="POST":
        form=ContribuyenteForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            cuit = informacion ['cuit']
            denominacion = informacion ['denominacion']
            domicilio = informacion ['domicilio']
            email = informacion ['email']
            empleador = informacion ['empleador']
            empleado = informacion ['empleado']
            activo = informacion ['activo']

            contribuyente1 = Contribuyente(
                cuit =  cuit,
                denominacion =  denominacion,
                domicilio =  domicilio,
                email =  email,
                empleador =  empleador,
                empleado =  empleado,
                activo =  activo,
                )
            contribuyente1.save()
            return render (request, "inicio.html")
    else:
        formulario=ContribuyenteForm()


    return render(request, "contribuyenteFormulario", {"form":formulario})