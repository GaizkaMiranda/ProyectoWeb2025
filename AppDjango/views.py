from django.shortcuts import render, get_object_or_404, render, get_list_or_404
from django.http import HttpResponse
from .models import Empleado, Proyecto, Tarea, Herramienta
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import EmpleadoForm, ProyectoForm, TareaForm, HerramientaForm
from django.contrib import messages

# Create your views here.

#Vamos a realizar las vistas basadas en CLASES para facilitar tanto la creación como la manipulación de estas

# LIST VIEWS:
class ProyectoListView(View):
    def get(self, request):
        proyectos = Proyecto.objects.order_by("nombre")
        ultimos_proyectos = Proyecto.objects.order_by('-id')[:3]  
        context = {
            "lista_proyectos": proyectos,
            "ultimos_proyectos": ultimos_proyectos,  
        }
        return render(request, "listado-proyectos.html", context)
    
class TareaListView(View):
    def get(self, request):
        tareas = get_list_or_404(Tarea.objects.order_by("nombre"))
        ultimas_tareas = Tarea.objects.order_by('-id')[:3]
        context = {
            "lista_tareas": tareas,
            "ultimas_tareas": ultimas_tareas,
        }
        return render(request, "listado-tareas.html", context)

class EmpleadoListView(View):
    def get(self, request):
        empleados = Empleado.objects.order_by("dni")
        ultimos_empleados = Empleado.objects.order_by('-id')[:3]
        context = {
            "lista_empleados": empleados,
            "ultimos_empleados": ultimos_empleados,
        }
        return render(request, "listado-empleados.html", context)

class HerramientaListView(View):
    def get(self, request):
        herramientas = Herramienta.objects.order_by("nombre")
        ultimas_herramientas = Herramienta.objects.order_by('-id')[:3]
        context = {
            "lista_herramientas": herramientas,
            "ultimas_herramientas": ultimas_herramientas,
        }
        return render(request, "listado-herramientas.html", context)

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimos_empleados'] = Empleado.objects.order_by('-id')[:3]
        return context

class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = 'proyecto-detalle.html'
    context_object_name = 'proyecto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimos_proyectos'] = Proyecto.objects.order_by('-id')[:3]
        return context
    
class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tarea-detalle.html'
    context_object_name = 'tarea'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimas_tareas'] = Tarea.objects.order_by('-id')[:3]
        
        # Recupera y elimina el mensaje de sesión (si existe)
        mensaje_estado = self.request.session.pop('mensaje_estado', None)
        context['mensaje_estado'] = mensaje_estado

        return context


class HerramientaDetailView(DetailView):
    model = Herramienta
    template_name = "herramienta-detalle.html"
    context_object_name = "herramienta"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimas_herramientas'] = Herramienta.objects.order_by('-id')[:3]
        return context


# CREATE VIEWS:
class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'crear-empleado.html'
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados')
    context_object_name = 'empleado'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimos_empleados'] = Empleado.objects.order_by('-id')[:3]
        return context

class ProyectoCreateView(CreateView):
    model = Proyecto
    template_name = 'crear-proyecto.html'
    form_class = ProyectoForm
    success_url = reverse_lazy('proyectos')
    context_object_name = 'proyecto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimos_proyectos'] = Proyecto.objects.order_by('-id')[:3]
        return context

class TareaCreateView(CreateView):
    model = Tarea
    template_name = 'crear-tarea.html'
    form_class = TareaForm
    success_url = reverse_lazy('tareas')
    context_object_name = 'tarea'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimas_tareas'] = Tarea.objects.order_by('-id')[:3]
        return context

class HerramientaCreateView(CreateView):
    model = Herramienta
    template_name = "crear-herramienta.html"
    form_class = HerramientaForm
    success_url = reverse_lazy("herramientas")
    context_object_name = "herramienta"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimas_herramientas'] = Herramienta.objects.order_by('-id')[:3]
        return context


# DELETE VIEWS:
class ProyectoDeleteView(DeleteView):
    model = Proyecto
    success_url = reverse_lazy('proyectos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimos_proyectos'] = Proyecto.objects.order_by('-id')[:3]
        return context

class TareaDeleteView(DeleteView):
    model = Tarea
    success_url = reverse_lazy('tareas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimas_tareas'] = Tarea.objects.order_by('-id')[:3]
        return context

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimos_empleados'] = Empleado.objects.order_by('-id')[:3]
        return context

class HerramientaDeleteView(DeleteView):
    model = Herramienta
    success_url = reverse_lazy('herramientas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimas_herramientas'] = Herramienta.objects.order_by('-id')[:3]
        return context


# UPDATE VIEWS:
class ProyectoUpdateView(UpdateView):
    model = Proyecto
    template_name = 'proyecto_update.html'
    form_class = ProyectoForm

    def get(self, request, pk):
        proyecto = get_object_or_404(Proyecto, pk=pk)
        formulario = self.form_class(instance=proyecto)
        ultimos_empleados = Empleado.objects.order_by('-id')[:3]
        context = {
            'formulario': formulario,
            'proyecto': proyecto,
            'ultimos_empleados': ultimos_empleados,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        proyecto = get_object_or_404(Proyecto, pk=pk)
        formulario = self.form_class(request.POST, instance=proyecto)
        ultimos_empleados = Empleado.objects.order_by('-id')[:3]
        if formulario.is_valid():
            formulario.save()
            return redirect('detalle_proyecto', pk=proyecto.pk)
        else:
            context = {
                'formulario': formulario,
                'proyecto': proyecto,
                'ultimos_empleados': ultimos_empleados,
            }
            return render(request, self.template_name, context)
        


class TareaUpdateView(UpdateView):
    model = Tarea
    template_name = 'tarea_update.html'
    form_class = TareaForm

    def get(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk)
        formulario = self.form_class(instance=tarea)
        ultimos_empleados = Empleado.objects.order_by('-id')[:3]
        
        # Mostrar notificación si existe en sesión
        notificacion = request.session.pop('notificacion_estado_tarea', None)
        
        context = {
            'formulario': formulario,
            'tarea': tarea,
            'ultimos_empleados': ultimos_empleados,
            'notificacion': notificacion,  # Añadimos la notificación al contexto
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk)
        estado_anterior = tarea.estado
        formulario = self.form_class(request.POST, instance=tarea)

        if formulario.is_valid():
            tarea_actualizada = formulario.save()

            # Si el estado ha cambiado
            if estado_anterior != tarea_actualizada.estado:
                mensaje = f"La tarea '{tarea_actualizada.nombre}' ha cambiado de {tarea.get_estado_display()} a {tarea_actualizada.get_estado_display()}"
                
                # Opción 1: Usar el sistema de mensajes de Django
                messages.success(request, mensaje)
                
                # Opción 2: Guardar en sesión (como tenías)
                request.session['notificacion_estado_tarea'] = mensaje

            return redirect('detalle_tarea', pk=tarea_actualizada.pk)

        # En caso de error en el formulario
        ultimos_empleados = Empleado.objects.order_by('-id')[:3]
        context = {
            'formulario': formulario,
            'tarea': tarea,
            'ultimos_empleados': ultimos_empleados,
        }
        return render(request, self.template_name, context)
    


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = 'empleado_update.html'
    form_class = EmpleadoForm

    def get(self, request, pk):
        empleado = get_object_or_404(Empleado, pk=pk)
        formulario = self.form_class(instance=empleado)
        ultimos_empleados = Empleado.objects.order_by('-id')[:3]
        context = {
            'formulario': formulario,
            'empleado': empleado,
            'ultimos_empleados': ultimos_empleados,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        empleado = get_object_or_404(Empleado, pk=pk)
        formulario = self.form_class(request.POST, instance=empleado)
        ultimos_empleados = Empleado.objects.order_by('-id')[:3]
        if formulario.is_valid():
            formulario.save()
            return redirect('detalle_empleado', pk=empleado.pk)
        else:
            context = {
                'formulario': formulario,
                'empleado': empleado,
                'ultimos_empleados': ultimos_empleados,
            }
            return render(request, self.template_name, context)
    
        
class HerramientaUpdateView(UpdateView):
    model = Herramienta
    template_name = 'herramienta_update.html'
    form_class = HerramientaForm

    def get(self, request, pk):
        herramienta = get_object_or_404(Herramienta, pk=pk)
        formulario = self.form_class(instance=herramienta)
        ultimos_empleados = Empleado.objects.order_by('-id')[:3]
        context = {
            'formulario': formulario,
            'herramienta': herramienta,
            'ultimos_empleados': ultimos_empleados,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        herramienta = get_object_or_404(Herramienta, pk=pk)
        formulario = self.form_class(request.POST, instance=herramienta)
        ultimos_empleados = Empleado.objects.order_by('-id')[:3]
        if formulario.is_valid():
            formulario.save()
            return redirect('detalle_herramienta', pk=herramienta.pk)
        else:
            context = {
                'formulario': formulario,
                'herramienta': herramienta,
                'ultimos_empleados': ultimos_empleados,
            }
            return render(request, self.template_name, context)

# Función de columna 1 del footer, para mostrar los 3 ultimos empleados añadidos
def UltimosTresEmpleados(request):
    ultimos_empleados = Empleado.objects.order_by('-id')[:3]
    # el "-id" le ponemos para el orden descendente, de esta manera al usar ":3", cogerá los 3 últimos de la lista
    return render(request, 'tu_template.html', {'ultimos_empleados': ultimos_empleados})