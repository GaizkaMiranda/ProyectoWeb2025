## Github 
https://github.com/GaizkaMiranda/ProyectoWeb2025.git

## Extras
Además de las relaciones entre las entidades enunciadas, se ha implementado la entidad "Herramienta". Siendo esta una relacion many to many con las tareas. 
De esta manera se dispondrá de n herramientas en m tareas. 

También, se han añadido funcionalidades extra en cada listado de cada entidad. 
En caso de los empleados, se ha añadido un listado con los empleados no disponibles, es decir, con el campo "disponibilidad" en "baja médica", "vacaciones" o "viaje". Estas se listarán en un listado
y en caso de no haber ninguno, se mostrará el mensaje "Todos los empleados están disponibles".
En caso de los proyectos, se ha implementado un listado con los proyectos de alto presupuesto, consideransose este superior a 500€ del campo "presupuesto".
Para las tareas se ha implementado un listado para informar de las tareas en proceso, es decir, mostrar las tareas con el campo "estado" en "en_proceso".
Por último, para las herramientas se ha implementado un último listado para mostrar las herramientas con baja disponibilidad, es decir, con este listado informaremos a los usuarios de las herramientas 
que tengan menos de 5 horas de disponibilidad. 
