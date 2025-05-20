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
from django import forms

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateTimeInput(attrs={
                'type': 'datetime-local',   
            }),
            'fecha_fin': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            }),
        }


from django import forms

class HerramientaForm(forms.ModelForm):
    class Meta:
        model = Herramienta
        fields = '__all__'
        widgets = {
            'fecha_compra': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
            }),
            'caducidad_garantia': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.fecha_compra:
            self.initial['fecha_compra'] = self.instance.fecha_compra.strftime('%Y-%m-%dT%H:%M')
        if self.instance and self.instance.caducidad_garantia:
            self.initial['caducidad_garantia'] = self.instance.caducidad_garantia.strftime('%Y-%m-%d')


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
            }),
            'fecha_fin': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ['fecha_inicio', 'fecha_fin']:
            if self.instance and getattr(self.instance, field):
                self.initial[field] = getattr(self.instance, field).strftime('%Y-%m-%dT%H:%M')

        
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
    

# formulario para el envio de emails
class EmailForm(forms.Form):
    mensaje = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 100}),
        
        required=True
    )

    def clean_mensaje(self):
        mensaje = self.cleaned_data.get('mensaje')
        palabras_prohibidas = ["palabra1", "palabra2", "palabra3"]
        for palabra in palabras_prohibidas:
            mensaje = mensaje.replace(palabra, '*' * len(palabra))
        return mensaje
