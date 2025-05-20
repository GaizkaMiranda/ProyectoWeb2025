from django.db import models

#CHOICES de los MODELOS:
#DEPARTAMENTO AL QUE PERTENECE X HERRAMIENTA
DEPARTAMENTOS = [
    ("it", "IT"),
    ("rrhh", "RRHH"),
    ("i+d", "I+D"),
    ("produccion", "Producción"),
    ("logistica", "Logística"),
    ("finanzas", "Finanzas"),
    ("planificacion", "Planificación"),
    ("pintura", "Pintura"),
    ("otro", "Otro"),
]

#ESTADO EN EL QUE SE ENCUENTRA X TAREA
ESTADO_TAREA = [
    ('abierta', 'Abierta'),
    ('asignada', 'Asignada'),
    ('en_proceso', 'En proceso'),
    ('finalizada', 'Finalizada'),
]

#IMPORTANCIA DE X TAREA
PRIORIDAD_ELECCION = [
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baja', 'Baja'),
    ]

#DISPONIBILIDAD DE LA QUE DISPONE X EMPLEADO
EMPLEADO_DISPONIBILIDAD = [
        ("disponible", "Disponible"),
        ("baja médica", "Baja Médica"),
        ("vacaciones", "Vacaciones"),
        ("viaje", "Viaje"),
    ]

# Create your models here.
# Modelo EMPLEADO
class Empleado(models.Model):
    dni = models.CharField(max_length=9, unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    telefono = models.IntegerField()
    disponibilidad = models.CharField(max_length=20, choices=EMPLEADO_DISPONIBILIDAD, default="disponible")
# Metodo del modelo empleado:
    def __str__(self):
        return f"{self.dni}- {self.nombre}- {self.apellidos}"

# Modelo PROYECTO
# Proyecto M-N Empleados
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField("Fecha inicio")
    fecha_fin= models.DateTimeField("Fecha fin")
    presupuesto = models.FloatField(default=0)
    cliente = models.CharField(max_length=100)
    #ManyToMany para disponer de n empleados en m proyectos
    empleados = models.ManyToManyField(Empleado, related_name="proyectos")
# Metodo del modelo proyecto:
    def __str__(self):
        return f"{self.nombre}"
 
# Modelo HERRAMIENTA
class Herramienta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    horas_disponibilidad = models.IntegerField(default=0)
    fecha_compra = models.DateTimeField(null=True, blank=True) # null: si se deja vacio en formulario (en bd = null)
    caducidad_garantia = models.DateField(null=True, blank=True) # null: si se deja vacio en formulario (en bd = null)
    pertenencia = models.CharField(max_length=20, choices=DEPARTAMENTOS, default='otro')
# Metodo del modelo herramienta:
    def __str__(self):
        return f"{self.nombre}-{self.descripcion}"   

# Modelo TAREA
class Tarea(models.Model):
    Proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name= "tareas")
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    fecha_inicio = models.DateTimeField("Fecha inicio")
    fecha_fin = models.DateTimeField("Fecha fin")
    responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name= "tareas")
    n_responsabilidad = models.CharField(max_length=10,choices=PRIORIDAD_ELECCION, default='media')
    estado = models.CharField(max_length=20, choices=ESTADO_TAREA, default='abierta')
    #ManyToMany para disponer de n herramientas en m tareas
    herramientas =models.ManyToManyField(Herramienta, related_name="herramientas")
    notas = models.TextField(max_length=500)
    # Metodo del modelo tarea   
    def __str__(self):
        return f"{self.nombre}- {self.descripcion}"