# RUBICON
## _Sistema de liquidación del Impuesto a las Ganancias 4ta categoría_
## _SLIG_

##### ✨MDsarrollado por Marco D'Angelo, estudiante de Coder
#
#

Rubicón SLIG es un sistema desarrollado en Django, aún en etapa de desarrollo, para el cálculo mensual y anual del Impuesto a las Ganancias 4ta categoría.Ademas genera los informes solicitados por AFIP. 
Reempaza las planillas en Excel por un sistema integral y con las actualizaciones de las normas que impactan en el cálculo mensual y anual.


## Características

- Administra los contribuyentes en dos categorías: Empleador y Empleado
- Administra los conceptos de ingresos del empleado
- Determina un Sueldo neto Mensual por empleado para ser verificado con el Recibo de Sueldo
- Calcula mensualmente las retenciones y proyecta la determinación anual del impuesto
- Genera las DDJJ 
- Muestra la cuenta corriente de cada contribuyente de acuerdo a lo determinado a pagar y lo pagado



## Estado del pryecto

Rubicon SLIG se encuentra en la primera etapa de desarrollo 

Permite hasta el momento:
- Agregar , listar, editar y buscar un Contribuyente
- Agregar y listar y editar un Empleado
- Agregar y listar un Concepto de Ingreso


## Instalación y acceso

Desde Visual Studio Code ejecutar el la terminal


cd Impuesto
python manage.py runserver

Para ingresar al inicio se debe ingresar a traves de la dirección de local server generado por el runserver y se accede a http://localhost:8000/home/
Esta es la pagina de inicio desde donde se acceden a todas las opciones del sistema



En la margen izquierda aparecen los siguientes accesos:
- Contribuyente: dar de alta un contribuyente, con los siguientes datos
    -   CUIT
    -   Denominación
    -   Domicilio
    -   e-mail
    -   Es Empleador: tildar si es empleador
    -   Es Empleado: tildar si es empleado
    -   Activo: tidar si está activo
- Listado de Contribuyentes: Lista todos los Contribuyentes y permite modoficar uno en particular
- Busqueda de un Contribuyente por CUIT
- Empleados: dar de alta un Empleado
    - CUIT Empleador
    - CUIT Empleado
    - Legajo	
    - Fecha de Inicio: fecha de inicio de la relación laboral con el empleador indicado
    - Conyuje a Cargo: tildar solo si esta a cargo del empleado
    - Cantidad de Hijos: cantidad de hijos a cargo
- Listado de Empleado: Lista todos los Empleados y permite modoficar uno en particular
- Conceptos de Ingreso: dar de alta un Concepto
    - Concepto: Descripción del concepto que no necesariamente debe ser el del recibo
    - Es remunerativo: tildar si es remunerativo
- Listado de Conceptos de Ingreso:Lista todos los Conceptos y permite modoficar uno en particular

En el extremo superior de la derecha el botón de Inicio nos lleva a la página principal

