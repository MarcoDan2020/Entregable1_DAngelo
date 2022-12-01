from django import forms

class ContribuyenteForm(forms.Form):
    cuit= forms.IntegerField(label='CUIT', required = True)
    denominacion=forms.CharField(max_length=40, label='Denominación', required = True)
    domicilio= forms.CharField(max_length=50, label='Domicilio', required = True)
    email = forms.EmailField(label='e-mail')
    empleador = forms.BooleanField(label='Es Empleador', initial = False)
    empleado = forms.BooleanField(label='Es Empleado', initial = False)
    activo = forms.BooleanField(label= 'Activo',required = True, initial = True )

class EmpleadoForm(forms.Form):
    cuit= forms.IntegerField(label='CUIT Empleado')
    cuit_empleador= forms.IntegerField(label='CUIT Empleador')
    legajo = forms.CharField (max_length=10, label='Legajo')
    fecha_inicio = forms.DateField (label= 'Fecha de Inicio')
    conyuje = forms.BooleanField (label='Conyuje a Cargo')
    hijos = forms.IntegerField (label = 'Cantidad de Hijos') 

class ConceptoForm (forms.Form):
    id_concepto = forms.IntegerField (label=id)
    descripcion = forms.CharField (max_length=30, label='Concepto')
    remunerativo = forms.BooleanField (label= 'Es remunerativo', initial = True)
