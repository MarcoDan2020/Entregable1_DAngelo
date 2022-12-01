from django.db import models

class Contribuyente (models.Model):
    cuit= models.IntegerField(primary_key=True, verbose_name='CUIT')
    denominacion=models.CharField(max_length=40, verbose_name='Denominación')
    domicilio= models.CharField(max_length=50, verbose_name='Domicilio')
    email = models.EmailField(verbose_name='e-mail')
    empleador = models.BooleanField(verbose_name='Es Empleador')
    empleado = models.BooleanField(verbose_name='Es Empleado')
    activo = models.BooleanField(verbose_name= 'Activo')

    class Meta:
        ordering = ["-cuit"]

    def __str__(self):
        return self.cuit+" - "+str(self.denominacion)


class Empleado (models.Model):
    cuit= models.IntegerField(primary_key=True, verbose_name='CUIT Empleado')
    cuit_empleador= models.IntegerField(verbose_name='CUIT Empleador')
    legajo = models.CharField (max_length=10, verbose_name='Legajo')
    fecha_inicio = models.DateField (verbose_name= 'Fecha de Inicio')
    conyuje = models.BooleanField (verbose_name='Conyuje a Cargo')
    hijos = models.IntegerField (verbose_name='Cantidad de Hijos a Cargo') 
        
    class Meta:
        ordering = ["-cuit"]

    def __str__(self):
        return self.cuit+" - "+str(self.denominacion)

class Concepto_Ingreso (models.Model):
    id_concepto = models.AutoField (primary_key=True)
    descripcion = models.CharField (max_length=30, verbose_name='Concepto')
    remunerativo = models.BooleanField ()

    class Meta:
        ordering = ["-descripcion"]

    def __str__(self):
        return self.descripcion
    
    