from django.urls import path
from .views import EmpleadoCreateView, EmpleadoDetailView, EmpleadoListView, ProyectoCreateView, ProyectoDetailView, ProyectoListView, TareaCreateView, TareaDetailView, TareaListView, ProyectoDeleteView, TareaDeleteView, EmpleadoDeleteView, ProyectoUpdateView, EmpleadoUpdateView, TareaUpdateView, HerramientaListView, HerramientaDetailView, HerramientaCreateView, HerramientaUpdateView, HerramientaDeleteView, login_view
from . import views

urlpatterns = [
    #url inicial/ bienvenida
    path('', views.vista_inicio, name='inicio'),
    # urls de usuarios
    path('login/', login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('logout/', views.logout_view, name='logout'),
    
    # url envio emails
    path('consulta_email/', views.enviar_email, name='consulta_email'),
    #path('actualizar_estado_pedido/<int:pk>/', views.actualizar_estado_pedido, name='actualizar_estado_pedido'),
    
    #URLs modelo: PROYECTO
    path("proyectos/" , ProyectoListView.as_view(), name="proyectos"),
    path("proyectos/<int:pk>/",ProyectoDetailView.as_view(), name="detalle_proyecto"),
    path('proyectos/crear/', ProyectoCreateView.as_view(), name='crear-proyecto'),
    path('proyectos/eliminar/<int:pk>/', ProyectoDeleteView.as_view(), name='proyecto_delete'),
    path('proyectos/modificar/<int:pk>', ProyectoUpdateView.as_view(), name='proyecto_update'),

    #URLs modelo: TAREAS
    path("tareas/",TareaListView.as_view(), name="tareas"),
    path('tareas/crear/', TareaCreateView.as_view(), name='crear-tarea'),
    path('tareas/eliminar/<int:pk>/', TareaDeleteView.as_view(), name='tarea_delete'),
    path("tareas/<int:pk>/",TareaDetailView.as_view(), name="detalle_tarea"),
    path('tareas/modificar/<int:pk>', TareaUpdateView.as_view(), name='tarea_update'),

    #URLs modelo: EMPLEADO
    path("empleados/",EmpleadoListView.as_view(), name="empleados"),
    path("empleados/<int:pk>/", EmpleadoDetailView.as_view(), name="detalle_empleado"),    
    path('empleados/crear/', EmpleadoCreateView.as_view(), name='crear-empleado'),
    path('empleados/eliminar/<int:pk>/', EmpleadoDeleteView.as_view(), name='empleado_delete'),
    path('empleados/modificar/<int:pk>', EmpleadoUpdateView.as_view(), name='empleado_update'),

    #URLs modelo: HERRAMIENTA
    path('herramientas/', HerramientaListView.as_view(), name='herramientas'),
    path('herramientas/crear/', HerramientaCreateView.as_view(), name='crear_herramienta'),
    path('herramientas/<int:pk>/', HerramientaDetailView.as_view(), name='detalle_herramienta'),
    path('herramientas/modificar/<int:pk>/', HerramientaUpdateView.as_view(), name='herramienta_update'),
    path('herramientas/eliminar/<int:pk>/', HerramientaDeleteView.as_view(), name='herramienta_delete'),


]