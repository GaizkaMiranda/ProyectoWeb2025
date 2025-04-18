from django.urls import path
from . import views

urlpatterns = [
    path("proyectos/",views.ProyectoListView.as_view(), name="proyectos"),
    path("tareas/",views.TareaListView.as_view(), name="tareas"),
    path("empleados/",views.EmpleadoListView.as_view(), name="empleados"),
    path("empleado/<str:dni_url>", views.empleado_tareas, name="empleado-tareas"),
    path("empleados/<int:dni>/", views.EmpleadoDetailView.as_view(), name="detalle_empleado"),
    path("proyectos/<int:id>/", views.ProyectoDetailView.as_view(), name="detalle_proyecto"),
    path("tareas/<int:id>/", views.TareaDetailView.as_view(), name="detalle_tarea"),




     
    #el name se usa para enlaces de navegación en los html
]