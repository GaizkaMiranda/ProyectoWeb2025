from django.shortcuts import render, get_object_or_404, render, get_list_or_404
from django.http import HttpResponse
from .models import Empleado, Proyecto, Tarea
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import EmpleadoForm, ProyectoForm, TareaForm


# Create your views here.

#Vamos a realizar las vistas basadas en clases para facilitar tanto la creación como la manipulación de estas

class ProyectoListView(View):
    def get(self, request):
        proyectos = get_list_or_404(Proyecto.objects.order_by("nombre"))
        context = {"lista_proyectos": proyectos}
        return render (request, "listado-proyectos.html", context)
    
class TareaListView(View):
    def get(self, request):
        tareas = get_list_or_404(Tarea.objects.order_by("nombre"))
        context = {"lista_tareas": tareas}
        return render (request, "listado-tareas.html", context)
    
    
class EmpleadoListView(View):
    def get(self, request):
        empleados = get_list_or_404(Empleado.objects.order_by("dni"))
        context = {"lista_empleados": empleados}
        return render (request, "listado-empleados.html", context)
    
#Usamos una vista basada en función esta vez, para mostrar las tareas asociadas a cada empleado    
def empleado_tareas(request, nombre_url):           
    empleado = get_object_or_404(Empleado, nombre=nombre_url) 
    
    tareas = empleado.trabajadores.all()
    
    context = {
        "empleado": empleado,
        "tareas": tareas
    }
    return render(request, "empleado-tareas.html", context)
    
class EmpleadoDetailView(DetailView):
    model = Empleado 
    template_name = 'empleado-detalle.html'
    context_object_name = 'empleado' 

class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = 'proyecto-detalle.html'
    context_object_name = 'proyecto'
    
class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tarea-detalle.html'
    context_object_name = 'tarea'
    
class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'crear-empleado.html'
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados')
    context_object_name = 'empleado'

class ProyectoCreateView(CreateView):
    model = Proyecto
    template_name = 'crear-proyecto.html'
    form_class = ProyectoForm
    success_url = reverse_lazy('proyectos')
    context_object_name = 'proyecto'

class TareaCreateView(CreateView):
    model = Tarea
    template_name = 'crear-tarea.html'
    form_class = TareaForm
    success_url = reverse_lazy('tareas')
    context_object_name = 'tarea'
    
class ProyectoDeleteView(DeleteView):
    model = Proyecto
    success_url = reverse_lazy('proyectos')
    
class TareaDeleteView(DeleteView):
    model = Tarea
    success_url = reverse_lazy('tareas')
    
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados')
    
