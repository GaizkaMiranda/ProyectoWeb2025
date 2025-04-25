from django import forms
from .models import Empleado, Proyecto, Tarea, Herramienta

# Formulario del modelo EMPLEADO
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

# Formulario del modelo PROYECTO
class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'

# Formulario del modelo TAREA
class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'

# Formulario del modelo HERRAMIENTA
class HerramientaForm(forms.ModelForm):
    class Meta:
        model = Herramienta
        fields = '__all__'