from django.contrib import admin
from .models import (
    Administrador, Facultad, Programa, Coordinador, Materia, Docente,
    Estudiante, Aula, Asistencia, DetalleAsistencia, SensorAsistencia,
    Microcurriculo, ContenidoCompetenciasEspecificas, PlanMicrocurriculo,
    DetallePlanMicrocurriculo, CargaAcademica, HorarioEstudiante,
    MateriaDocente, HorarioDocente
)

# ===============================
# ADMINISTRADOR
# ===============================
@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('id_administrador', 'nombre', 'apellido', 'correo', 'celular', 'ciudad')
    search_fields = ('nombre', 'apellido', 'correo')
    list_filter = ('sexo', 'ciudad', 'departamento')
    ordering = ('apellido', 'nombre')

# ===============================
# FACULTAD
# ===============================
@admin.register(Facultad)
class FacultadAdmin(admin.ModelAdmin):
    list_display = ('codigo_facultad', 'nombre_facultad', 'numero_programas')
    search_fields = ('nombre_facultad', 'codigo_facultad')
    ordering = ('nombre_facultad',)

# ===============================
# PROGRAMA
# ===============================
@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('codigo_programa', 'nombre_programa', 'numero_creditos', 'facultad')
    search_fields = ('nombre_programa', 'codigo_programa')
    list_filter = ('facultad',)
    ordering = ('nombre_programa',)

# ===============================
# COORDINADOR
# ===============================
@admin.register(Coordinador)
class CoordinadorAdmin(admin.ModelAdmin):
    list_display = ('id_coordinador', 'nombre', 'apellido', 'correo', 'programa', 'celular')
    search_fields = ('nombre', 'apellido', 'correo')
    list_filter = ('programa', 'sexo', 'ciudad')
    ordering = ('apellido', 'nombre')

# ===============================
# MATERIA
# ===============================
@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('codigo_materia', 'nombre_materia', 'numero_creditos')
    search_fields = ('nombre_materia', 'codigo_materia')
    ordering = ('nombre_materia',)

# ===============================
# DOCENTE
# ===============================
@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('id_docente', 'nombre_docente', 'apellido_docente', 'correo', 'celular', 'ciudad')
    search_fields = ('nombre_docente', 'apellido_docente', 'correo')
    list_filter = ('sexo', 'ciudad', 'departamento')
    ordering = ('apellido_docente', 'nombre_docente')

# ===============================
# ESTUDIANTE
# ===============================
@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('id_estudiante', 'nombre', 'apellido', 'correo', 'programa', 'facultad')
    search_fields = ('nombre', 'apellido', 'correo', 'celular')
    list_filter = ('programa', 'facultad', 'sexo', 'tipo_documento', 'estado_civil')
    ordering = ('apellido', 'nombre')
    fieldsets = (
        ('Información Personal', {
            'fields': ('tipo_documento', 'fecha_expedicion', 'nombre', 'apellido', 'fecha_nacimiento', 'sexo', 'estado_civil')
        }),
        ('Contacto', {
            'fields': ('celular', 'correo', 'direccion', 'ciudad', 'departamento', 'pais')
        }),
        ('Información Académica', {
            'fields': ('facultad', 'programa', 'puntaje_icfes', 'sisben')
        }),
        ('Acudiente', {
            'fields': ('nombre_acudiente', 'apellido_acudiente', 'celular_acudiente')
        }),
    )

# ===============================
# AULA
# ===============================
@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('codigo_aula', 'nombre_aula', 'capacidad')
    search_fields = ('nombre_aula', 'codigo_aula')
    ordering = ('nombre_aula',)

# ===============================
# ASISTENCIA
# ===============================
@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('codigo_asistencia', 'asignatura', 'docente_responsable', 'fecha', 'hora', 'aula', 'grupo')
    search_fields = ('asignatura', 'codigo_asignatura', 'tema')
    list_filter = ('fecha', 'docente_responsable', 'aula', 'grupo')
    ordering = ('-fecha', '-hora')
    date_hierarchy = 'fecha'

# ===============================
# DETALLE ASISTENCIA
# ===============================
@admin.register(DetalleAsistencia)
class DetalleAsistenciaAdmin(admin.ModelAdmin):
    list_display = ('id_detalle', 'asistencia', 'estudiante', 'estado', 'fecha_registro')
    search_fields = ('estudiante__nombre', 'estudiante__apellido')
    list_filter = ('estado', 'asistencia__fecha')
    ordering = ('-fecha_registro',)

# ===============================
# SENSOR ASISTENCIA
# ===============================
@admin.register(SensorAsistencia)
class SensorAsistenciaAdmin(admin.ModelAdmin):
    list_display = ('codigo_sensor', 'nombre_aula', 'aula', 'activo', 'fecha_instalacion')
    search_fields = ('codigo_sensor', 'nombre_aula')
    list_filter = ('activo', 'aula')
    ordering = ('codigo_sensor',)

# ===============================
# MICROCURRICULO
# ===============================
@admin.register(Microcurriculo)
class MicrocurriculoAdmin(admin.ModelAdmin):
    list_display = ('codigo_microcurriculo', 'nombre_materia', 'programa', 'numero_creditos', 'tipo_asignatura')
    search_fields = ('nombre_materia', 'codigo_microcurriculo')
    list_filter = ('programa', 'tipo_asignatura', 'naturaleza_asignatura')
    ordering = ('nombre_materia',)
    fieldsets = (
        ('Información Básica', {
            'fields': ('codigo_microcurriculo', 'programa', 'nombre_materia', 'numero_creditos', 'tipo_asignatura', 'naturaleza_asignatura', 'departamento_oferente')
        }),
        ('Descripción', {
            'fields': ('descripcion_asignatura', 'prerequisitos')
        }),
        ('Objetivos', {
            'fields': ('objetivo_general', 'objetivos_especificos')
        }),
        ('Competencias', {
            'fields': ('competencias_genericas',)
        }),
        ('Metodología', {
            'fields': ('estrategias_pedagogicas_metodologicas', 'referencias_bibliograficas')
        }),
        ('Niveles de Desempeño', {
            'fields': ('nivel_superior', 'nivel_normal', 'nivel_bajo', 'nivel_deficiente')
        }),
        ('Evaluación', {
            'fields': ('primer_parcial', 'segundo_parcial', 'tercer_parcial')
        }),
    )

# ===============================
# CONTENIDO COMPETENCIAS ESPECIFICAS
# ===============================
@admin.register(ContenidoCompetenciasEspecificas)
class ContenidoCompetenciasEspecificasAdmin(admin.ModelAdmin):
    list_display = ('codigo_competencia', 'microcurriculo', 'unidad_tematica')
    search_fields = ('unidad_tematica', 'competencias_especificas')
    list_filter = ('microcurriculo',)
    ordering = ('microcurriculo', 'codigo_competencia')

# ===============================
# PLAN MICROCURRICULO
# ===============================
@admin.register(PlanMicrocurriculo)
class PlanMicrocurriculoAdmin(admin.ModelAdmin):
    list_display = ('codigo_plan_microcurriculo', 'microcurriculo', 'docente', 'periodo_academico', 'año_lectivo', 'fecha_inicio', 'fecha_terminacion')
    search_fields = ('microcurriculo__nombre_materia', 'docente__nombre_docente', 'periodo_academico')
    list_filter = ('año_lectivo', 'periodo_academico', 'programa', 'facultad')
    ordering = ('-año_lectivo', 'periodo_academico')
    date_hierarchy = 'fecha_inicio'

# ===============================
# DETALLE PLAN MICROCURRICULO
# ===============================
@admin.register(DetallePlanMicrocurriculo)
class DetallePlanMicrocurriculoAdmin(admin.ModelAdmin):
    list_display = ('id_detalle', 'plan_microcurriculo', 'semana', 'fecha_clase', 'tema', 'cumplido')
    search_fields = ('tema', 'descripcion_actividad')
    list_filter = ('cumplido', 'semana')
    ordering = ('plan_microcurriculo', 'semana', 'fecha_clase')

# ===============================
# CARGA ACADEMICA
# ===============================
@admin.register(CargaAcademica)
class CargaAcademicaAdmin(admin.ModelAdmin):
    list_display = ('id_carga', 'programa', 'materia', 'docente', 'grupo', 'dia', 'hora', 'aula')
    search_fields = ('materia__nombre_materia', 'docente__nombre_docente', 'grupo')
    list_filter = ('programa', 'dia', 'periodo_carga')
    ordering = ('dia', 'hora')

# ===============================
# HORARIO ESTUDIANTE
# ===============================
@admin.register(HorarioEstudiante)
class HorarioEstudianteAdmin(admin.ModelAdmin):
    list_display = ('codigo_horario', 'estudiante', 'materia', 'dia', 'hora', 'aula', 'grupo')
    search_fields = ('estudiante__nombre', 'estudiante__apellido', 'materia__nombre_materia')
    list_filter = ('dia', 'periodo', 'aula')
    ordering = ('estudiante', 'dia', 'hora')

# ===============================
# MATERIA DOCENTE
# ===============================
@admin.register(MateriaDocente)
class MateriaDocenteAdmin(admin.ModelAdmin):
    list_display = ('codigo_materia_docente', 'docente', 'materia', 'periodo')
    search_fields = ('docente__nombre_docente', 'materia__nombre_materia')
    list_filter = ('periodo',)
    ordering = ('docente', 'materia')

# ===============================
# HORARIO DOCENTE
# ===============================
@admin.register(HorarioDocente)
class HorarioDocenteAdmin(admin.ModelAdmin):
    list_display = ('codigo_horario_docente', 'docente', 'materia', 'dia', 'hora', 'aula', 'grupo')
    search_fields = ('docente__nombre_docente', 'materia__nombre_materia')
    list_filter = ('dia', 'periodo', 'aula')
    ordering = ('docente', 'dia', 'hora')