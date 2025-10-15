from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # ===========================
    # AUTENTICACIÓN
    # ===========================
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='academico/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='academico/logout.html'), name='logout'),
    
    # ===========================
    # ADMINISTRADOR
    # ===========================
    path('administrador/dashboard/', views.administrador_dashboard, name='administrador_dashboard'),
    
    # Gestión de Coordinadores
    path('administrador/coordinadores/', views.coordinadores_lista, name='coordinadores_lista'),
    path('administrador/coordinadores/crear/', views.coordinador_crear, name='coordinador_crear'),
    path('administrador/coordinadores/editar/<int:pk>/', views.coordinador_editar, name='coordinador_editar'),
    path('administrador/coordinadores/eliminar/<int:pk>/', views.coordinador_eliminar, name='coordinador_eliminar'),
    
    # Gestión de Docentes
    path('administrador/docentes/', views.docentes_lista, name='docentes_lista'),
    path('administrador/docentes/crear/', views.docente_crear, name='docente_crear'),
    path('administrador/docentes/editar/<int:pk>/', views.docente_editar, name='docente_editar'),
    path('administrador/docentes/eliminar/<int:pk>/', views.docente_eliminar, name='docente_eliminar'),
    
    # Gestión de Estudiantes
    path('administrador/estudiantes/', views.estudiantes_lista, name='estudiantes_lista'),
    path('administrador/estudiantes/crear/', views.estudiante_crear, name='estudiante_crear'),
    path('administrador/estudiantes/editar/<int:pk>/', views.estudiante_editar, name='estudiante_editar'),
    path('administrador/estudiantes/eliminar/<int:pk>/', views.estudiante_eliminar, name='estudiante_eliminar'),
    
    # Gestión de Facultades
    path('administrador/facultades/', views.facultades_lista, name='facultades_lista'),
    path('administrador/facultades/crear/', views.facultad_crear, name='facultad_crear'),
    path('administrador/facultades/editar/<str:pk>/', views.facultad_editar, name='facultad_editar'),
    path('administrador/facultades/eliminar/<str:pk>/', views.facultad_eliminar, name='facultad_eliminar'),
    
    # Gestión de Programas
    path('administrador/programas/', views.programas_lista, name='programas_lista'),
    path('administrador/programas/crear/', views.programa_crear, name='programa_crear'),
    path('administrador/programas/editar/<str:pk>/', views.programa_editar, name='programa_editar'),
    path('administrador/programas/eliminar/<str:pk>/', views.programa_eliminar, name='programa_eliminar'),
    
    # Gestión de Aulas
    path('administrador/aulas/', views.aulas_lista, name='aulas_lista'),
    path('administrador/aulas/crear/', views.aula_crear, name='aula_crear'),
    path('administrador/aulas/editar/<str:pk>/', views.aula_editar, name='aula_editar'),
    path('administrador/aulas/eliminar/<str:pk>/', views.aula_eliminar, name='aula_eliminar'),
    
    # Gestión de Materias
    path('administrador/materias/', views.materias_lista, name='materias_lista'),
    path('administrador/materias/crear/', views.materia_crear, name='materia_crear'),
    path('administrador/materias/editar/<str:pk>/', views.materia_editar, name='materia_editar'),
    path('administrador/materias/eliminar/<str:pk>/', views.materia_eliminar, name='materia_eliminar'),
    
    # ===========================
    # COORDINADOR
    # ===========================
    path('coordinador/dashboard/', views.coordinador_dashboard, name='coordinador_dashboard'),
    
    # Carga Académica
    path('coordinador/carga-academica/', views.carga_academica_lista, name='carga_academica_lista'),
    path('coordinador/carga-academica/crear/', views.carga_academica_crear, name='carga_academica_crear'),
    path('coordinador/carga-academica/editar/<int:pk>/', views.carga_academica_editar, name='carga_academica_editar'),
    path('coordinador/carga-academica/eliminar/<int:pk>/', views.carga_academica_eliminar, name='carga_academica_eliminar'),
    
    # Microcurrículos
    path('coordinador/microcurriculos/', views.microcurriculos_lista, name='microcurriculos_lista'),
    path('coordinador/microcurriculos/crear/', views.microcurriculo_crear, name='microcurriculo_crear'),
    path('coordinador/microcurriculos/editar/<str:pk>/', views.microcurriculo_editar, name='microcurriculo_editar'),
    path('coordinador/microcurriculos/ver/<str:pk>/', views.microcurriculo_ver, name='microcurriculo_ver'),
    
    # Horarios
    path('coordinador/horarios/docentes/', views.horarios_docentes, name='horarios_docentes'),
    path('coordinador/horarios/estudiantes/', views.horarios_estudiantes, name='horarios_estudiantes'),
    
    # ===========================
    # DOCENTE
    # ===========================
    path('docente/dashboard/', views.docente_dashboard, name='docente_dashboard'),
    
    # Asistencias
    path('docente/asistencias/', views.asistencias_lista, name='asistencias_lista'),
    path('docente/asistencias/crear/', views.asistencia_crear, name='asistencia_crear'),
    path('docente/asistencias/registrar/<int:pk>/', views.asistencia_registrar, name='asistencia_registrar'),
    path('docente/asistencias/ver/<int:pk>/', views.asistencia_ver, name='asistencia_ver'),
    
    # Plan de Microcurrículo
    path('docente/plan-microcurriculo/', views.plan_microcurriculo_lista, name='plan_microcurriculo_lista'),
    path('docente/plan-microcurriculo/crear/', views.plan_microcurriculo_crear, name='plan_microcurriculo_crear'),
    path('docente/plan-microcurriculo/ver/<int:pk>/', views.plan_microcurriculo_ver, name='plan_microcurriculo_ver'),
    
    # Horario
    path('docente/horario/', views.docente_horario, name='docente_horario'),
    
    # ===========================
    # ESTUDIANTE
    # ===========================
    path('estudiante/dashboard/', views.estudiante_dashboard, name='estudiante_dashboard'),
    
    # Horario
    path('estudiante/horario/', views.estudiante_horario, name='estudiante_horario'),
    path('estudiante/horario/crear/', views.estudiante_crear_horario, name='estudiante_crear_horario'),
    
    # Asistencias
    path('estudiante/asistencias/', views.estudiante_asistencias, name='estudiante_asistencias'),
    
    # Seguimiento Microcurrículo
    path('estudiante/seguimiento-microcurriculo/', views.estudiante_seguimiento_microcurriculo, name='estudiante_seguimiento_microcurriculo'),
]