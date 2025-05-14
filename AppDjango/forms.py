from django import forms
from .models import Empleado, Proyecto, Tarea, Herramienta
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 

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
        
# Formulario para el registro: UserCreationForm de Django
class RegistroForm(UserCreationForm):
    #vamos a hacer el autorrelleno en este campo
    email = forms.EmailField(required=True)
    class Meta:
        fields = ['username', 'email', 'password1']
        model = User # tenemos que usar el model User de Django: https://docs.djangoproject.com/en/5.2/ref/contrib/auth/  y   https://testdriven.io/blog/django-custom-user-model/

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    