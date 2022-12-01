from django.db import models

class Contribuyente (models.Model)
    cuit= models.IntegerField(primary_key=True, verbose_name='CUIT')
    denominacion=models.CharField(max_length=40, verbose_name='Denominación')
    domicilio= models.CharField(max_length=50, verbose_name='Domicilio')
    email = models.EmailField(verbose_name='e-mail')
    empleador = models.BooleanField(verbose_name='Es Em´ñeador')
    empleado = models.BooleanField(verbose_name='Es Empleado')
    activo = models.BooleanField(verbose_name= 'Activo')

    class Meta:
        ordering = ["-cuit"]

    def __str__(self):
        return self.cuit+" - "+str(self.denominacion)


class Empleado (models.Model):
    cuit= models.IntegerField(primary_key=True, verbose_name='CUIT Empleado')
    cuit_empleador= models.IntegerField(verbose_name='CUIT Empleador')
    legajo = models.CharField (max_length=10, verbose_name='Legajo', verbose_name_plural = 'Legajos')
    fecha_inicio = models.DateField (verbose_name= 'Fecha de Inicio')
    conyuje = models.BooleanField (verbose_name='Conyuje a Cargo')
    hijos = models.IntegerChoices (verbose_name = 'Cantidad de Hijos') 
        
    class Meta:
        ordering = ["-cuit"]

    def __str__(self):
        return self.cuit+" - "+str(self.denominacion)
    
    