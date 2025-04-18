from django.urls import path
from .views import EmpleadoCreateView, EmpleadoDetailView, EmpleadoListView, ProyectoCreateView, ProyectoDetailView, ProyectoListView, TareaCreateView, TareaDetailView, TareaListView
from . import views

urlpatterns = [
    path("proyectos/" , ProyectoListView.as_view(), name="proyectos"),
    path("tareas/",TareaListView.as_view(), name="tareas"),
    path("empleados/",EmpleadoListView.as_view(), name="empleados"),
    path("empleado/<str:dni_url>", views.empleado_tareas, name="empleado-tareas"),
    path("empleados/<int:pk>/", EmpleadoDetailView.as_view(), name="detalle_empleado"),
    path("proyectos/<int:pk>/",ProyectoDetailView.as_view(), name="detalle_proyecto"),
    path("tareas/<int:pk>/",TareaDetailView.as_view(), name="detalle_tarea"),
    path('empleados/crear/', EmpleadoCreateView.as_view(), name='crear-empleado'),
    path('proyectos/crear/', ProyectoCreateView.as_view(), name='crear-proyecto'),
    path('tareas/crear/', TareaCreateView.as_view(), name='crear-tarea'),





     
    #el name se usa para enlaces de navegación en los html
]