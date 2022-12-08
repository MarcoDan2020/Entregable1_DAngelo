from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Contribuyente, Empleado, Concepto_Ingreso
from .forms import ContribuyenteForm, EmpleadoForm, ConceptoForm 

from django.urls import reverse

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
            return render (request, "inicio.html", {"mensaje":"Contribuyente cargado"})
    else:
        formulario=ContribuyenteForm()
        


    return render(request, "contribuyente.html", {"form":formulario})


def leerContribuyentes(request):
    contribuyentes=Contribuyente.objects.all()
    return render(request, "leerContribuyentes.html", {"contribuyentes":contribuyentes})


def resultadosBusquedaContribuyente (request):

    if 'cuit' in request.GET:
        

        cuit = request.GET['cuit']

        contribuyentes = Contribuyente.objects.filter(cuit=cuit)
        return render(request,"leerContribuyentes.html", {"contribuyentes":contribuyentes , "mensaje":"CUIT encontrada:"})
    else:
        return render(request, "leerContribuyentes.html")


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

                return render (request, "leerContribuyentes.html", {"mensaje": "El Contribuyente ha sido correctamente editado!", "contribuyentes":contribuyentes})
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




def empleado (request):
    if request.method=="POST":
        form=EmpleadoForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            cuit = informacion ['cuit']
            cuit_empleador = informacion ['cuit_empleador']
            legajo = informacion ['legajo']
            fecha_inicio = informacion ['fecha_inicio']
            conyuje = informacion ['conyuje']
            hijos = informacion ['hijos']

            empleado1 = Empleado(
                cuit = cuit,
                cuit_empleador =  cuit_empleador,
                legajo =  legajo,
                fecha_inicio =  fecha_inicio,
                conyuje =  conyuje,
                hijos =  hijos
                )
            empleado1.save()
            return render (request, "inicio.html")
    else:
        formulario=EmpleadoForm()


    return render(request, "empleado.html", {"form":formulario})

def leerEmpleados(request):
    empleados=Empleado.objects.all()
    return render(request, "leerEmpleados.html", {"empleados":empleados})

def editarEmpleado (request, cuit):
    empleado=Empleado.objects.get(cuit=cuit)
    if request.method=="POST":
        form=EmpleadoForm (request.POST)
        print(form)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)

            if form.is_valid():
                informacion=form.cleaned_data
                empleado.cuit = informacion ['cuit']
                empleado.cuit_empleador = informacion ['cuit_empleador']
                empleado.legajo = informacion ['legajo']
                empleado.fecha_inicio = informacion ['fecha_inicio']
                empleado.conyuje = informacion ['conyuje']
                empleado.hijos = informacion ['hijos']
                

                empleado.save()
                empleados=Empleado.objects.all()

                return render (request, "leerEmpleados.html", {"mensaje": "El Empleado ha sido correctamente editado!", "empleados":empleados})
    else:
        
        formulario = EmpleadoForm (initial={
                'cuit':empleado.cuit,
                'cuit_empleador':empleado.cuit_empleador,
                'legajo' : empleado.legajo,
                'fecha_inicio':empleado.fecha_inicio,
                'conyuje':empleado.conyuje,
                'hijos':empleado.hijos
                })
    return render(request, "editarEmpleado.html", {"form":formulario, "empleado":empleado})


def concepto (request):
    if request.method=="POST":
        form=ConceptoForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            descripcion = informacion ['descripcion']
            remunerativo = informacion ['remunerativo']
            
            concepto1 = Concepto_Ingreso(
                descripcion = descripcion,
                remunerativo = remunerativo
                )
            concepto1.save()
            return render (request, "inicio.html")
    else:
        formulario=ConceptoForm()


    return render(request, "concepto.html", {"form":formulario})

def leerConceptos(request):
    conceptos=Concepto_Ingreso.objects.all()
    return render(request, "leerConceptos.html", {"conceptos":conceptos})




