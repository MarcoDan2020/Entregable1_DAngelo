from django import forms

class ContribuyenteForm(forms.Form):
    cuit= forms.IntegerField(label='CUIT', required = True)
    denominacion=forms.CharField(max_length=40, label='Denominación', required = True)
    domicilio= forms.CharField(max_length=50, label='Domicilio', required = True)
    email = forms.EmailField(label='e-mail')
    empleador = forms.BooleanField(label='Es Empleador')
    empleado = forms.BooleanField(label='Es Empleado')
    activo = forms.BooleanField(label= 'Activo',required = True, initial = True )

class EmpleadoForm(forms.Form):
    cuit= forms.IntegerField(label='CUIT Empleado')
    cuit_empleador= forms.IntegerField(label='CUIT Empleador')
    legajo = forms.CharField (max_length=10, label='Legajo')
    fecha_inicio = forms.DateField (label= 'Fecha de Inicio')
    conyuje = forms.BooleanField (label='Conyuje a Cargo')
    hijos = forms.IntegerField (label = 'Cantidad de Hijos') 