from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse
from .models import Empleado, Proyecto, Tarea, Herramienta
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import EmpleadoForm, ProyectoForm, TareaForm, HerramientaForm, RegistroForm, EmailForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail




# Create your views here.

def vista_inicio(request):
    return render(request, 'inicio.html')

#Vamos a realizar las vistas basadas en CLASES para facilitar tanto la creación como la manipulación de estas

# LIST VIEWS:
class ProyectoListView(LoginRequiredMixin,View):
    def get(self, request):
        # Capturar el presupuesto desde la URL (?presupuesto=...)
        presupuesto_minimo = request.GET.get('presupuesto', 500)
        try:
            presupuesto_minimo = float(presupuesto_minimo)
        except ValueError:
            presupuesto_minimo = 500  # Valor por defecto si viene mal

        proyectos_alto_presupuesto = Proyecto.objects.filter(
            presupuesto__gt=presupuesto_minimo
        ).order_by('nombre')

        proyectos = Proyecto.objects.order_by("nombre")
        ultimos_proyectos = Proyecto.objects.order_by('-id')[:3]

        context = {
            "lista_proyectos": proyectos,
            "ultimos_proyectos": ultimos_proyectos,
            "presupuesto_minimo": presupuesto_minimo,
            "alta_lista": proyectos_alto_presupuesto,
        }
        return render(request, "listado-proyectos.html", context)

    
class TareaListView(LoginRequiredMixin, View):
    def get(self, request):
        tareas_en_proceso = Tarea.objects.filter(estado = "en_proceso").order_by("nombre")
        tareas = get_list_or_404(Tarea.objects.order_by("nombre"))
        ultimas_tareas = Tarea.objects.order_by('-id')[:3]
        context = {
            "tareas_en_proceso": tareas_en_proceso,
            "lista_tareas": tareas,
            "ultimas_tareas": ultimas_tareas,
        }
        return render(request, "listado-tareas.html", context)

class EmpleadoListView(LoginRequiredMixin,View):
    def get(self, request):
        empleados = Empleado.objects.order_by("dni")
        ultimos_empleados = Empleado.objects.order_by('-id')[:3]
        context = {
            "lista_empleados": empleados,
            "ultimos_empleados": ultimos_empleados,
        }
        return render(request, "listado-empleados.html", context)

class HerramientaListView(LoginRequiredMixin,View):
    def get(self, request):
        herramientas = Herramienta.objects.order_by("nombre")
        ultimas_herramientas = Herramienta.objects.order_by('-id')[:3]
        context = {
            "lista_herramientas": herramientas,
            "ultimas_herramientas": ultimas_herramientas,
        }
        return render(request, "listado-herramientas.html", context)

# DETAIL VIEWS:
class EmpleadoDetailView(LoginRequiredMixin,DetailView):
    model = Empleado 
    template_name = 'empleado-detalle.html'
    context_object_name = 'empleado'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimos_empleados'] = Empleado.objects.order_by('-id')[:3]
        return context

class ProyectoDetailView(LoginRequiredMixin,DetailView):
    model = Proyecto
    template_name = 'proyecto-detalle.html'
    context_object_name = 'proyecto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimos_proyectos'] = Proyecto.objects.order_by('-id')[:3]
        return context
    
class TareaDetailView(LoginRequiredMixin,DetailView):
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


class HerramientaDetailView(LoginRequiredMixin,DetailView):
    model = Herramienta
    template_name = "herramienta-detalle.html"
    context_object_name = "herramienta"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimas_herramientas'] = Herramienta.objects.order_by('-id')[:3]
        return context


# CREATE VIEWS:
class EmpleadoCreateView(LoginRequiredMixin,CreateView):
    model = Empleado
    template_name = 'crear-empleado.html'
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados')
    context_object_name = 'empleado'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimos_empleados'] = Empleado.objects.order_by('-id')[:3]
        return context

class ProyectoCreateView(LoginRequiredMixin,CreateView):
    model = Proyecto
    template_name = 'crear-proyecto.html'
    form_class = ProyectoForm
    success_url = reverse_lazy('proyectos')
    context_object_name = 'proyecto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimos_proyectos'] = Proyecto.objects.order_by('-id')[:3]
        return context

class TareaCreateView(LoginRequiredMixin,CreateView):
    model = Tarea
    template_name = 'crear-tarea.html'
    form_class = TareaForm
    success_url = reverse_lazy('tareas')
    context_object_name = 'tarea'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimas_tareas'] = Tarea.objects.order_by('-id')[:3]
        return context

class HerramientaCreateView(LoginRequiredMixin,CreateView):
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
class ProyectoDeleteView(LoginRequiredMixin,DeleteView):
    model = Proyecto
    success_url = reverse_lazy('proyectos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimos_proyectos'] = Proyecto.objects.order_by('-id')[:3]
        return context

class TareaDeleteView(LoginRequiredMixin,DeleteView):
    model = Tarea
    success_url = reverse_lazy('tareas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimas_tareas'] = Tarea.objects.order_by('-id')[:3]
        return context

class EmpleadoDeleteView(LoginRequiredMixin,DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimos_empleados'] = Empleado.objects.order_by('-id')[:3]
        return context

class HerramientaDeleteView(LoginRequiredMixin,DeleteView):
    model = Herramienta
    success_url = reverse_lazy('herramientas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimas_herramientas'] = Herramienta.objects.order_by('-id')[:3]
        return context


# UPDATE VIEWS:
class ProyectoUpdateView(LoginRequiredMixin,UpdateView):
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
        


class TareaUpdateView(LoginRequiredMixin,UpdateView):
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
    


class EmpleadoUpdateView(LoginRequiredMixin,UpdateView):
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
    
        
class HerramientaUpdateView(LoginRequiredMixin,UpdateView):
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


#Vistas realizadas para la E3-E4
# INICIO DE SESIÓN
# ha sido útil: https://stackoverflow.com/questions/75401759/how-to-set-up-login-view-in-python-django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    # Si el usuario ya está autenticado, redirigir
    if request.user.is_authenticated:
        return redirect('proyectos')
    
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        
        # Validación básica
        if not username or not password:
            messages.error(request, 'Todos los campos son obligatorios')
        else:
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                if user.is_staff:  # Verifica que el usuario sea admin
                    login(request, user)
                    next_url = request.GET.get('next', 'inicio') #envíamos al usuario a la pantalla de bienvdenida/ inicio al iniciar sesión
                    return redirect(next_url)
                else:
                    messages.error(request, 'No tienes permisos de administrador.')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    
    # Contexto para el template
    context = {
        'title': 'Inicio de Sesión',
        'messages': messages.get_messages(request)
    }
    return render(request, 'login.html', context)
# vista del registro
def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}')
            return redirect('login')
        else:
            messages.error(request, 'Error al crear la cuenta. Verifica los datos e intenta nuevamente.')
    # si el metodo no es POST se crea una instancia vacia del formulario para que la pagina de registro se muestre
    # correctamente, esto permite que la plantilla registro.html se renderice con un formulario vacio que el usuario
    # pueda rellenar
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})
#tengo que crear el template


@login_required(login_url='login')
def logout_view(request):
    """
    Vista para cerrar sesión que:
    1. Requiere que el usuario esté autenticado
    2. Cierra la sesión actual
    3. Muestra mensaje de confirmación
    4. Redirige a la página de login
    """
    # Almacenamos el nombre de usuario para el mensaje
    username = request.user.username
    
    # Cerramos la sesión
    logout(request)
    
    # Añadimos mensaje de confirmación
    messages.success(request, f'Has cerrado sesión correctamente. ¡Hasta pronto, {username}!')
    
    # Redirigimos a la página de login
    return redirect('login')


# vista de envio de emails
@login_required(login_url='login')
def enviar_mensaje_soporte(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            mensaje = form.cleaned_data['mensaje']
            try:
                send_mail(
                    'Mensaje de Soporte',
                    mensaje,
                    request.user.email,
                    ['deustronicdeusto@gmail.com']
                )
                messages.success(request, 'Tu mensaje ha sido enviado al equipo de soporte.')
                return redirect('soporte')
            except Exception as e:
                messages.error(request, f'Error al enviar el mensaje: {e}')
    else:
        form = EmailForm()
    return render(request, 'soporte.html', {'form': form})