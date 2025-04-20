from django.urls import path
from .views import EmpleadoCreateView, EmpleadoDetailView, EmpleadoListView, ProyectoCreateView, ProyectoDetailView, ProyectoListView, TareaCreateView, TareaDetailView, TareaListView, ProyectoDeleteView, TareaDeleteView, EmpleadoDeleteView, ProyectoUpdateView, EmpleadoUpdateView, TareaUpdateView
from . import views

urlpatterns = [
    
    #urls para proyectos
    path("proyectos/" , ProyectoListView.as_view(), name="proyectos"),
    path("proyectos/<int:pk>/",ProyectoDetailView.as_view(), name="detalle_proyecto"),
    path('proyectos/crear/', ProyectoCreateView.as_view(), name='crear-proyecto'),
    path('proyectos/eliminar/<int:pk>/', ProyectoDeleteView.as_view(), name='proyecto_delete'),
    path('proyectos/modificar/<int:pk>', ProyectoUpdateView.as_view(), name='proyecto_update'),


    #urls para tareas
    path("tareas/",TareaListView.as_view(), name="tareas"),
    path('tareas/crear/', TareaCreateView.as_view(), name='crear-tarea'),
    path('tareas/eliminar/<int:pk>/', TareaDeleteView.as_view(), name='tarea_delete'),
    path("tareas/<int:pk>/",TareaDetailView.as_view(), name="detalle_tarea"),
    path('tareas/modificar/<int:pk>', TareaUpdateView.as_view(), name='tarea_update'),


    #urls para empleados
    path("empleados/",EmpleadoListView.as_view(), name="empleados"),
    path("empleado/<str:dni_url>", views.empleado_tareas, name="empleado-tareas"),
    path("empleados/<int:pk>/", EmpleadoDetailView.as_view(), name="detalle_empleado"),    
    path('empleados/crear/', EmpleadoCreateView.as_view(), name='crear-empleado'),
    path('empleados/eliminar/<int:pk>/', EmpleadoDeleteView.as_view(), name='empleado_delete'),
    path('empleados/modificar/<int:pk>', EmpleadoUpdateView.as_view(), name='empleado_update'),


]