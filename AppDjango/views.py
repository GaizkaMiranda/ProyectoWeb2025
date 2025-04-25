from django.shortcuts import render, get_object_or_404, render, get_list_or_404
from django.http import HttpResponse
from .models import Empleado, Proyecto, Tarea, Herramienta
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import EmpleadoForm, ProyectoForm, TareaForm, HerramientaForm


# Create your views here.

#Vamos a realizar las vistas basadas en clases para facilitar tanto la creación como la manipulación de estas

# LIST VIEWS:
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

class HerramientaListView(View):
    def get(self, request):
        herramientas = get_list_or_404(Herramienta.objects.order_by("nombre"))  
        context = {"lista_herramientas": herramientas}
        return render (request, "listado-herramientas.html", context)  
        
#Usamos una vista basada en función esta vez, para mostrar las tareas asociadas a cada empleado    
def empleado_tareas(request, nombre_url):           
    empleado = get_object_or_404(Empleado, nombre=nombre_url) 
    
    tareas = empleado.trabajadores.all()
    
    context = {
        "empleado": empleado,
        "tareas": tareas
    }
    return render(request, "empleado-tareas.html", context)


# DETAIL VIEWS:
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

class HerramientaDetailView(DetailView):
    model = Herramienta
    template_name = "herramienta-detalle.html"
    context_object_name = "herramienta"


# CREATE VIEWS:
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

class HerramientCreateView(CreateView):
    model = Herramienta
    template_name = "crear-herramienta.html"
    form_class = HerramientaForm
    success_url = reverse_lazy("herramientas")
    context_object_name = "herramienta"


# DELETE VIEWS:    
class ProyectoDeleteView(DeleteView):
    model = Proyecto
    success_url = reverse_lazy('proyectos')
    
class TareaDeleteView(DeleteView):
    model = Tarea
    success_url = reverse_lazy('tareas')
    
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados')

class HerramientaDeleteView(DeleteView):
    model = Herramienta
    success_url = reverse_lazy('herramientas')
    

# UPDATE VIEWS:
class ProyectoUpdateView(UpdateView):
    model = Proyecto
    template_name = 'proyecto_update.html'
    form_class = ProyectoForm

    def get(self, request, pk):
        proyecto = get_object_or_404(Proyecto, pk=pk)
        formulario = self.form_class(instance=proyecto)
        context = {'formulario': formulario, 'proyecto': proyecto}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        proyecto = get_object_or_404(Proyecto, pk=pk)
        formulario = self.form_class(request.POST, instance=proyecto)
        if formulario.is_valid():
            formulario.save()
            return redirect('detalle_proyecto', pk=proyecto.pk)
        else:
            context = {'formulario': formulario, 'proyecto': proyecto}
            return render(request, self.template_name, context)
        

class TareaUpdateView(UpdateView):
    model = Tarea
    template_name = 'tarea_update.html'
    form_class = TareaForm

    def get(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk)
        formulario = self.form_class(instance=tarea)
        context = {'formulario': formulario, 'tarea': tarea}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk)
        formulario = self.form_class(request.POST, instance=tarea)
        if formulario.is_valid():
            formulario.save()
            return redirect('detalle_tarea', pk=tarea.pk)
        else:
            context = {'formulario': formulario, 'tarea': tarea}
            return render(request, self.template_name, context)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = 'empleado_update.html'
    form_class = EmpleadoForm

    def get(self, request, pk):
        empleado = get_object_or_404(Empleado, pk=pk)
        formulario = self.form_class(instance=empleado)
        context = {'formulario': formulario, 'empleado': empleado}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        empleado = get_object_or_404(Empleado, pk=pk)
        formulario = self.form_class(request.POST, instance=tarea)
        if formulario.is_valid():
            formulario.save()
            return redirect('detalle_empleado', pk=empleado.pk)
        else:
            context = {'formulario': formulario, 'empleado': empleado}
            return render(request, self.template_name, context)
    
        
class HerramientaUpdateView(UpdateView):
    model = Herramienta
    template_name = 'herramienta_update.html'
    form_class = HerramientaForm

    def get(self, request, pk):
        herramienta = get_object_or_404(Herramienta, pk=pk)
        formulario = self.form_class(instance=herramienta)
        context = {'formulario': formulario, 'herramienta': herramienta}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        herramienta = get_object_or_404(Herramienta, pk=pk)
        formulario = self.form_class(request.POST, instance=herramienta)
        if formulario.is_valid():
            formulario.save()
            return redirect('detalle_herramienta', pk=herramienta.pk)
        else:
            context = {'formulario': formulario, 'herramienta': herramienta}
            return render(request, self.template_name, context)

# Función de columna 1 del footer, para mostrar los 3 ultimos empleados añadidos
def UltimosTresEmpleados(request):
    ultimos_empleados = Empleado.objects.order_by('-id')[:3]
    # el "-id" le ponemos para el orden descendente, de esta manera al usar ":3", cogerá los 3 últimos de la lista
    return render(request, 'tu_template.html', {'ultimos_empleados': ultimos_empleados})