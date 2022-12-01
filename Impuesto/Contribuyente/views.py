from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Contribuyente, Empleado, Concepto_Ingreso
from .forms import ContribuyenteForm, EmpleadoForm, ConceptoForm 



def inicio(request):
    return render(request, "inicio.html")

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
            return render (request, "contribuyente.html")
    else:
        formulario=ContribuyenteForm()


    return render(request, "contribuyente.html", {"form":formulario})


def leerContribuyentes(request):
    contribuyentes=Contribuyente.objects.all()
    return render(request, "leerContribuyentes.html", {"contribuyentes":contribuyentes})

def editarContribuyente (request, cuit):
    contribuyente=Contribuyente.objects.get(cuit=cuit)
    if request.method=="POST":
        form=ContribuyenteForm (request.POST)
        print(form)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
                  
            if form.is_valid():
                informacion=form.cleaned_data
                contribuyente.cuit = informacion ['cuit']
                contribuyente.denominacion = informacion ['denominacion']
                contribuyente.domicilio = informacion ['domicilio']
                contribuyente.email = informacion ['email']
                contribuyente.empleador = informacion ['empleador']
                contribuyente.empleado = informacion ['empleado']
                contribuyente.activo = informacion ['activo']

                contribuyente.save()
                contribuyentes=Contribuyente.objects.all()

                return render (request, "lerContribuyentes.html", {"mensaje": "El Contribuyente ha sido correctamente editado!", "contribuyentes":contribuyentes})
    else:
        formulario = ContribuyenteForm (initial={
                'cuit':contribuyente.cuit,
                'denominacion':contribuyente.denominacion,
                'domicilio':contribuyente.domicilio,
                'email':contribuyente.email,
                'empleador':contribuyente.empleador,
                'empleado':contribuyente.empleado,
                'activo':contribuyente.activo
                })
    return render(request, "editarContribuyente.html", {"form":formulario, "contribuyente":contribuyente})


def concepto (request):
    if request.method=="POST":
        form=ConceptoForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            id_concepto = informacion ['id_concepto']
            descripcion = informacion ['descripcion']
            remunerativo = informacion ['remunerativo']
            
            concepto1 = Concepto_Ingreso(
                id_concepto = id_concepto,
                descripcion = descripcion,
                remunerativo = remunerativo
                )
            concepto1.save()
            return render (request, "concepto.html")
    else:
        formulario=ConceptoForm()


    return render(request, "concepto.html", {"form":formulario})