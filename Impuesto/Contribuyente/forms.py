from django import forms


class ContribuyenteForm(forms.Form):
    cuit= forms.IntegerField(primary_key=True, verbose_name='CUIT Empleado')
    cuit_empleador= forms.IntegerField(verbose_name='CUIT Empleador')
    legajo = forms.CharField (max_length=10, verbose_name='Legajo', verbose_name_plural = 'Legajos')
    fecha_inicio = forms.DateField (verbose_name= 'Fecha de Inicio')
    conyuje = forms.BooleanField (verbose_name='Conyuje a Cargo')
    hijos = forms.IntegerChoices (verbose_name = 'Cantidad de Hijos') 