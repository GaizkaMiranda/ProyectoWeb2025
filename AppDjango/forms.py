from django import forms
from .models import Empleado, Proyecto, Tarea


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'
