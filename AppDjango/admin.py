from django.contrib import admin
from .models import Empleado, Proyecto, Tarea
# Register your models here.
admin.site.register(Empleado)
admin.site.register(Proyecto)
admin.site.register(Tarea)
