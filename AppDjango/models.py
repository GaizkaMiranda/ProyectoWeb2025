from django.db import models

# Create your models here.
# 1 Proyecto tiene varias tareas (relacion 1-N)

class Empleado(models.Model):
    dni = models.CharField(max_length=9, unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    telefono = models.IntegerField()
    
    def __str__(self):
        return f"{self.dni}- {self.nombre}- {self.apellidos}- {self.email}- {self.telefono}"


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    fecha_inicio= models.DateTimeField("Fecha inicio")
    fecha_fin= models.DateTimeField("Fecha fin")
    presupuesto = models.FloatField(default=0)
    cliente = models.CharField(max_length=100)
    empleados = models.ManyToManyField(Empleado, related_name="proyectos")

    def __str__(self):
        return f"{self.nombre}- {self.descripcion}- {self.fecha_inicio}- {self.fecha_fin}- {self.presupuesto}- {self.cliente}"
    
      
class Tarea(models.Model):
    PRIORIDAD_ELECCION = [
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baja', 'Baja'),
    ]
    Proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name= "tareas")
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    fecha_inicio= models.DateTimeField("Fecha inicio")
    fecha_fin= models.DateTimeField("Fecha fin")
    responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name= "tareas")
    n_responsabilidad = models.CharField(max_length=10,choices=PRIORIDAD_ELECCION, default='media')
        
    def __str__(self):
        return f"{self.nombre}- {self.descripcion}- {self.fecha_inicio}- {self.fecha_fin}- {self.responsable}- {self.n_responsabilidad}"
        
        
    
        