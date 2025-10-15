from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count
from django.core.paginator import Paginator
from .models import *
from django.contrib.auth.models import User

# ========================================
# VISTA PRINCIPAL
# ========================================
def index(request):
    """Vista principal del sistema"""
    context = {
        'total_estudiantes': Estudiante.objects.count(),
        'total_docentes': Docente.objects.count(),
        'total_programas': Programa.objects.count(),
        'total_facultades': Facultad.objects.count(),
    }
    return render(request, 'academico/index.html', context)

# ========================================
# DASHBOARD ADMINISTRADOR
# ========================================
@login_required
def administrador_dashboard(request):
    """Dashboard del administrador"""
    context = {
        'total_estudiantes': Estudiante.objects.count(),
        'total_docentes': Docente.objects.count(),
        'total_coordinadores': Coordinador.objects.count(),
        'total_programas': Programa.objects.count(),
        'total_facultades': Facultad.objects.count(),
        'total_materias': Materia.objects.count(),
        'total_aulas': Aula.objects.count(),
    }
    return render(request, 'academico/administrador/dashboard.html', context)

# ========================================
# GESTIÓN DE COORDINADORES
# ========================================
@login_required
def coordinadores_lista(request):
    """Lista de coordinadores con búsqueda"""
    search = request.GET.get('search', '')
    coordinadores = Coordinador.objects.all()
    
    if search:
        coordinadores = coordinadores.filter(
            Q(nombre__icontains=search) |
            Q(apellido__icontains=search) |
            Q(correo__icontains=search)
        )
    
    paginator = Paginator(coordinadores, 10)
    page = request.GET.get('page')
    coordinadores = paginator.get_page(page)
    
    context = {
        'coordinadores': coordinadores,
        'search': search,
    }
    return render(request, 'academico/administrador/coordinadores_lista.html', context)

@login_required
def coordinador_crear(request):
    """Crear nuevo coordinador"""
    if request.method == 'POST':
        # Crear usuario
        username = request.POST.get('correo').split('@')[0]
        user = User.objects.create_user(
            username=username,
            email=request.POST.get('correo'),
            password=request.POST.get('password', 'temporal123')
        )
        
        # Crear coordinador
        coordinador = Coordinador.objects.create(
            usuario=user,
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            fecha_nacimiento=request.POST.get('fecha_nacimiento'),
            sexo=request.POST.get('sexo'),
            celular=request.POST.get('celular'),
            correo=request.POST.get('correo'),
            direccion=request.POST.get('direccion'),
            ciudad=request.POST.get('ciudad'),
            departamento=request.POST.get('departamento'),
            pais=request.POST.get('pais'),
            programa_id=request.POST.get('programa')
        )
        
        messages.success(request, 'Coordinador creado exitosamente')
        return redirect('coordinadores_lista')
    
    programas = Programa.objects.all()
    context = {'programas': programas}
    return render(request, 'academico/administrador/coordinador_form.html', context)

@login_required
def coordinador_editar(request, pk):
    """Editar coordinador existente"""
    coordinador = get_object_or_404(Coordinador, pk=pk)
    
    if request.method == 'POST':
        coordinador.nombre = request.POST.get('nombre')
        coordinador.apellido = request.POST.get('apellido')
        coordinador.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        coordinador.sexo = request.POST.get('sexo')
        coordinador.celular = request.POST.get('celular')
        coordinador.correo = request.POST.get('correo')
        coordinador.direccion = request.POST.get('direccion')
        coordinador.ciudad = request.POST.get('ciudad')
        coordinador.departamento = request.POST.get('departamento')
        coordinador.pais = request.POST.get('pais')
        coordinador.programa_id = request.POST.get('programa')
        coordinador.save()
        
        messages.success(request, 'Coordinador actualizado exitosamente')
        return redirect('coordinadores_lista')
    
    programas = Programa.objects.all()
    context = {
        'coordinador': coordinador,
        'programas': programas,
        'editar': True
    }
    return render(request, 'academico/administrador/coordinador_form.html', context)

@login_required
def coordinador_eliminar(request, pk):
    """Eliminar coordinador"""
    coordinador = get_object_or_404(Coordinador, pk=pk)
    if request.method == 'POST':
        coordinador.delete()
        messages.success(request, 'Coordinador eliminado exitosamente')
        return redirect('coordinadores_lista')
    
    context = {'coordinador': coordinador}
    return render(request, 'academico/administrador/coordinador_confirmar_eliminar.html', context)

# ========================================
# GESTIÓN DE DOCENTES
# ========================================
@login_required
def docentes_lista(request):
    """Lista de docentes con búsqueda"""
    search = request.GET.get('search', '')
    docentes = Docente.objects.all()
    
    if search:
        docentes = docentes.filter(
            Q(nombre_docente__icontains=search) |
            Q(apellido_docente__icontains=search) |
            Q(correo__icontains=search)
        )
    
    paginator = Paginator(docentes, 10)
    page = request.GET.get('page')
    docentes = paginator.get_page(page)
    
    context = {
        'docentes': docentes,
        'search': search,
    }
    return render(request, 'academico/administrador/docentes_lista.html', context)

@login_required
def docente_crear(request):
    """Crear nuevo docente"""
    if request.method == 'POST':
        # Crear usuario
        username = request.POST.get('correo').split('@')[0]
        user = User.objects.create_user(
            username=username,
            email=request.POST.get('correo'),
            password=request.POST.get('password', 'temporal123')
        )
        
        # Crear docente
        docente = Docente.objects.create(
            usuario=user,
            nombre_docente=request.POST.get('nombre'),
            apellido_docente=request.POST.get('apellido'),
            fecha_nacimiento=request.POST.get('fecha_nacimiento'),
            sexo=request.POST.get('sexo'),
            celular=request.POST.get('celular'),
            correo=request.POST.get('correo'),
            direccion=request.POST.get('direccion'),
            ciudad=request.POST.get('ciudad'),
            departamento=request.POST.get('departamento'),
            pais=request.POST.get('pais')
        )
        
        messages.success(request, 'Docente creado exitosamente')
        return redirect('docentes_lista')
    
    return render(request, 'academico/administrador/docente_form.html')

@login_required
def docente_editar(request, pk):
    """Editar docente existente"""
    docente = get_object_or_404(Docente, pk=pk)
    
    if request.method == 'POST':
        docente.nombre_docente = request.POST.get('nombre')
        docente.apellido_docente = request.POST.get('apellido')
        docente.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        docente.sexo = request.POST.get('sexo')
        docente.celular = request.POST.get('celular')
        docente.correo = request.POST.get('correo')
        docente.direccion = request.POST.get('direccion')
        docente.ciudad = request.POST.get('ciudad')
        docente.departamento = request.POST.get('departamento')
        docente.pais = request.POST.get('pais')
        docente.save()
        
        messages.success(request, 'Docente actualizado exitosamente')
        return redirect('docentes_lista')
    
    context = {
        'docente': docente,
        'editar': True
    }
    return render(request, 'academico/administrador/docente_form.html', context)

@login_required
def docente_eliminar(request, pk):
    """Eliminar docente"""
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == 'POST':
        docente.delete()
        messages.success(request, 'Docente eliminado exitosamente')
        return redirect('docentes_lista')
    
    context = {'docente': docente}
    return render(request, 'academico/administrador/docente_confirmar_eliminar.html', context)

# ========================================
# GESTIÓN DE ESTUDIANTES
# ========================================
@login_required
def estudiantes_lista(request):
    """Lista de estudiantes con búsqueda y filtros"""
    search = request.GET.get('search', '')
    programa_filter = request.GET.get('programa', '')
    
    estudiantes = Estudiante.objects.select_related('programa', 'facultad')
    
    if search:
        estudiantes = estudiantes.filter(
            Q(nombre__icontains=search) |
            Q(apellido__icontains=search) |
            Q(correo__icontains=search) |
            Q(id_estudiante__icontains=search)
        )
    
    if programa_filter:
        estudiantes = estudiantes.filter(programa_id=programa_filter)
    
    paginator = Paginator(estudiantes, 15)
    page = request.GET.get('page')
    estudiantes = paginator.get_page(page)
    
    programas = Programa.objects.all()
    
    context = {
        'estudiantes': estudiantes,
        'search': search,
        'programas': programas,
        'programa_filter': programa_filter,
    }
    return render(request, 'academico/administrador/estudiantes_lista.html', context)

@login_required
def estudiante_crear(request):
    """Crear nuevo estudiante"""
    if request.method == 'POST':
        # Crear usuario
        username = request.POST.get('correo').split('@')[0]
        user = User.objects.create_user(
            username=username,
            email=request.POST.get('correo'),
            password=request.POST.get('password', 'temporal123')
        )
        
        # Crear estudiante
        estudiante = Estudiante.objects.create(
            usuario=user,
            tipo_documento=request.POST.get('tipo_documento'),
            fecha_expedicion=request.POST.get('fecha_expedicion'),
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            fecha_nacimiento=request.POST.get('fecha_nacimiento'),
            sexo=request.POST.get('sexo'),
            celular=request.POST.get('celular'),
            correo=request.POST.get('correo'),
            estado_civil=request.POST.get('estado_civil'),
            direccion=request.POST.get('direccion'),
            ciudad=request.POST.get('ciudad'),
            departamento=request.POST.get('departamento'),
            pais=request.POST.get('pais'),
            puntaje_icfes=request.POST.get('puntaje_icfes'),
            nombre_acudiente=request.POST.get('nombre_acudiente'),
            apellido_acudiente=request.POST.get('apellido_acudiente'),
            celular_acudiente=request.POST.get('celular_acudiente'),
            sisben=request.POST.get('sisben'),
            facultad_id=request.POST.get('facultad'),
            programa_id=request.POST.get('programa')
        )
        
        messages.success(request, 'Estudiante creado exitosamente')
        return redirect('estudiantes_lista')
    
    facultades = Facultad.objects.all()
    programas = Programa.objects.all()
    context = {
        'facultades': facultades,
        'programas': programas
    }
    return render(request, 'academico/administrador/estudiante_form.html', context)


@login_required
def estudiante_editar(request, pk):
    """Editar estudiante existente"""
    estudiante = get_object_or_404(Estudiante, pk=pk)
    
    if request.method == 'POST':
        estudiante.tipo_documento = request.POST.get('tipo_documento')
        estudiante.fecha_expedicion = request.POST.get('fecha_expedicion')
        estudiante.nombre = request.POST.get('nombre')
        estudiante.apellido = request.POST.get('apellido')
        estudiante.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        estudiante.sexo = request.POST.get('sexo')
        estudiante.celular = request.POST.get('celular')
        estudiante.correo = request.POST.get('correo')
        estudiante.estado_civil = request.POST.get('estado_civil')
        estudiante.direccion = request.POST.get('direccion')
        estudiante.ciudad = request.POST.get('ciudad')
        estudiante.departamento = request.POST.get('departamento')
        estudiante.pais = request.POST.get('pais')
        estudiante.puntaje_icfes = request.POST.get('puntaje_icfes')
        estudiante.nombre_acudiente = request.POST.get('nombre_acudiente')
        estudiante.apellido_acudiente = request.POST.get('apellido_acudiente')
        estudiante.celular_acudiente = request.POST.get('celular_acudiente')
        estudiante.sisben = request.POST.get('sisben')
        estudiante.facultad_id = request.POST.get('facultad')
        estudiante.programa_id = request.POST.get('programa')
        estudiante.save()
        
        messages.success(request, 'Estudiante actualizado exitosamente')
        return redirect('estudiantes_lista')
    
    facultades = Facultad.objects.all()
    programas = Programa.objects.all()
    context = {
        'estudiante': estudiante,
        'facultades': facultades,
        'programas': programas,
        'editar': True
    }
    return render(request, 'academico/administrador/estudiante_form.html', context)

@login_required
def estudiante_eliminar(request, pk):
    """Eliminar estudiante"""
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        estudiante.delete()
        messages.success(request, 'Estudiante eliminado exitosamente')
        return redirect('estudiantes_lista')
    
    context = {'estudiante': estudiante}
    return render(request, 'academico/administrador/estudiante_confirmar_eliminar.html', context)

# ========================================
# GESTIÓN DE FACULTADES
# ========================================
@login_required
def facultades_lista(request):
    """Lista de facultades"""
    facultades = Facultad.objects.annotate(
        num_programas=Count('programas'),
        num_estudiantes=Count('estudiantes')
    )
    
    context = {'facultades': facultades}
    return render(request, 'academico/administrador/facultades_lista.html', context)

@login_required
def facultad_crear(request):
    """Crear nueva facultad"""
    if request.method == 'POST':
        Facultad.objects.create(
            codigo_facultad=request.POST.get('codigo'),
            nombre_facultad=request.POST.get('nombre'),
            numero_programas=request.POST.get('numero_programas', 0)
        )
        messages.success(request, 'Facultad creada exitosamente')
        return redirect('facultades_lista')
    
    return render(request, 'academico/administrador/facultad_form.html')

@login_required
def facultad_editar(request, pk):
    """Editar facultad existente"""
    facultad = get_object_or_404(Facultad, pk=pk)
    
    if request.method == 'POST':
        facultad.nombre_facultad = request.POST.get('nombre')
        facultad.numero_programas = request.POST.get('numero_programas')
        facultad.save()
        
        messages.success(request, 'Facultad actualizada exitosamente')
        return redirect('facultades_lista')
    
    context = {
        'facultad': facultad,
        'editar': True
    }
    return render(request, 'academico/administrador/facultad_form.html', context)

@login_required
def facultad_eliminar(request, pk):
    """Eliminar facultad"""
    facultad = get_object_or_404(Facultad, pk=pk)
    if request.method == 'POST':
        facultad.delete()
        messages.success(request, 'Facultad eliminada exitosamente')
        return redirect('facultades_lista')
    
    context = {'facultad': facultad}
    return render(request, 'academico/administrador/facultad_confirmar_eliminar.html', context)

# ========================================
# GESTIÓN DE PROGRAMAS
# ========================================
@login_required
def programas_lista(request):
    """Lista de programas"""
    programas = Programa.objects.select_related('facultad').annotate(
        num_estudiantes=Count('estudiantes')
    )
    
    context = {'programas': programas}
    return render(request, 'academico/administrador/programas_lista.html', context)

@login_required
def programa_crear(request):
    """Crear nuevo programa"""
    if request.method == 'POST':
        Programa.objects.create(
            codigo_programa=request.POST.get('codigo'),
            nombre_programa=request.POST.get('nombre'),
            numero_creditos=request.POST.get('creditos'),
            facultad_id=request.POST.get('facultad')
        )
        messages.success(request, 'Programa creado exitosamente')
        return redirect('programas_lista')
    
    facultades = Facultad.objects.all()
    context = {'facultades': facultades}
    return render(request, 'academico/administrador/programa_form.html', context)

@login_required
def programa_editar(request, pk):
    """Editar programa existente"""
    programa = get_object_or_404(Programa, pk=pk)
    
    if request.method == 'POST':
        programa.nombre_programa = request.POST.get('nombre')
        programa.numero_creditos = request.POST.get('creditos')
        programa.facultad_id = request.POST.get('facultad')
        programa.save()
        
        messages.success(request, 'Programa actualizado exitosamente')
        return redirect('programas_lista')
    
    facultades = Facultad.objects.all()
    context = {
        'programa': programa,
        'facultades': facultades,
        'editar': True
    }
    return render(request, 'academico/administrador/programa_form.html', context)

@login_required
def programa_eliminar(request, pk):
    """Eliminar programa"""
    programa = get_object_or_404(Programa, pk=pk)
    if request.method == 'POST':
        programa.delete()
        messages.success(request, 'Programa eliminado exitosamente')
        return redirect('programas_lista')
    
    context = {'programa': programa}
    return render(request, 'academico/administrador/programa_confirmar_eliminar.html', context)

# ========================================
# GESTIÓN DE AULAS
# ========================================
@login_required
def aulas_lista(request):
    """Lista de aulas"""
    aulas = Aula.objects.all()
    context = {'aulas': aulas}
    return render(request, 'academico/administrador/aulas_lista.html', context)

@login_required
def aula_crear(request):
    """Crear nueva aula"""
    if request.method == 'POST':
        Aula.objects.create(
            codigo_aula=request.POST.get('codigo'),
            nombre_aula=request.POST.get('nombre'),
            capacidad=request.POST.get('capacidad', 30)
        )
        messages.success(request, 'Aula creada exitosamente')
        return redirect('aulas_lista')
    
    return render(request, 'academico/administrador/aula_form.html')

@login_required
def aula_editar(request, pk):
    """Editar aula existente"""
    aula = get_object_or_404(Aula, pk=pk)
    
    if request.method == 'POST':
        aula.nombre_aula = request.POST.get('nombre')
        aula.capacidad = request.POST.get('capacidad')
        aula.save()
        
        messages.success(request, 'Aula actualizada exitosamente')
        return redirect('aulas_lista')
    
    context = {
        'aula': aula,
        'editar': True
    }
    return render(request, 'academico/administrador/aula_form.html', context)

@login_required
def aula_eliminar(request, pk):
    """Eliminar aula"""
    aula = get_object_or_404(Aula, pk=pk)
    if request.method == 'POST':
        aula.delete()
        messages.success(request, 'Aula eliminada exitosamente')
        return redirect('aulas_lista')
    
    context = {'aula': aula}
    return render(request, 'academico/administrador/aula_confirmar_eliminar.html', context)

# ========================================
# GESTIÓN DE MATERIAS
# ========================================
@login_required
def materias_lista(request):
    """Lista de materias"""
    materias = Materia.objects.all()
    context = {'materias': materias}
    return render(request, 'academico/administrador/materias_lista.html', context)

@login_required
def materia_crear(request):
    """Crear nueva materia"""
    if request.method == 'POST':
        Materia.objects.create(
            codigo_materia=request.POST.get('codigo'),
            nombre_materia=request.POST.get('nombre'),
            numero_creditos=request.POST.get('creditos')
        )
        messages.success(request, 'Materia creada exitosamente')
        return redirect('materias_lista')
    
    return render(request, 'academico/administrador/materia_form.html')

@login_required
def materia_editar(request, pk):
    """Editar materia existente"""
    materia = get_object_or_404(Materia, pk=pk)
    
    if request.method == 'POST':
        materia.nombre_materia = request.POST.get('nombre')
        materia.numero_creditos = request.POST.get('creditos')
        materia.save()
        
        messages.success(request, 'Materia actualizada exitosamente')
        return redirect('materias_lista')
    
    context = {
        'materia': materia,
        'editar': True
    }
    return render(request, 'academico/administrador/materia_form.html', context)

@login_required
def materia_eliminar(request, pk):
    """Eliminar materia"""
    materia = get_object_or_404(Materia, pk=pk)
    if request.method == 'POST':
        materia.delete()
        messages.success(request, 'Materia eliminada exitosamente')
        return redirect('materias_lista')
    
    context = {'materia': materia}
    return render(request, 'academico/administrador/materia_confirmar_eliminar.html', context)

# ========================================
# DASHBOARD COORDINADOR
# ========================================
@login_required
def coordinador_dashboard(request):
    """Dashboard del coordinador"""
    try:
        coordinador = Coordinador.objects.get(usuario=request.user)
        programa = coordinador.programa
        
        context = {
            'coordinador': coordinador,
            'programa': programa,
            'total_estudiantes': Estudiante.objects.filter(programa=programa).count(),
            'total_materias': Microcurriculo.objects.filter(programa=programa).count(),
            'total_docentes': CargaAcademica.objects.filter(programa=programa).values('docente').distinct().count(),
        }
        return render(request, 'academico/coordinador/dashboard.html', context)
    except Coordinador.DoesNotExist:
        messages.error(request, 'No tienes un perfil de coordinador asignado')
        return redirect('index')

# ========================================
# CARGA ACADÉMICA
# ========================================
@login_required
def carga_academica_lista(request):
    """Lista de carga académica"""
    coordinador = get_object_or_404(Coordinador, usuario=request.user)
    cargas = CargaAcademica.objects.filter(programa=coordinador.programa)
    
    context = {'cargas': cargas}
    return render(request, 'academico/coordinador/carga_academica_lista.html', context)

@login_required
def carga_academica_crear(request):
    """Crear carga académica"""
    if request.method == 'POST':
        coordinador = get_object_or_404(Coordinador, usuario=request.user)
        
        CargaAcademica.objects.create(
            programa=coordinador.programa,
            materia_id=request.POST.get('materia'),
            docente_id=request.POST.get('docente'),
            aula_id=request.POST.get('aula'),
            hora=request.POST.get('hora'),
            grupo=request.POST.get('grupo'),
            dia=request.POST.get('dia'),
            periodo_carga=request.POST.get('periodo')
        )
        
        messages.success(request, 'Carga académica creada exitosamente')
        return redirect('carga_academica_lista')
    
    materias = Materia.objects.all()
    docentes = Docente.objects.all()
    aulas = Aula.objects.all()
    
    context = {
        'materias': materias,
        'docentes': docentes,
        'aulas': aulas
    }
    return render(request, 'academico/coordinador/carga_academica_form.html', context)

@login_required
def carga_academica_editar(request, pk):
    """Editar carga académica"""
    carga = get_object_or_404(CargaAcademica, pk=pk)
    
    if request.method == 'POST':
        carga.materia_id = request.POST.get('materia')
        carga.docente_id = request.POST.get('docente')
        carga.aula_id = request.POST.get('aula')
        carga.hora = request.POST.get('hora')
        carga.grupo = request.POST.get('grupo')
        carga.dia = request.POST.get('dia')
        carga.periodo_carga = request.POST.get('periodo')
        carga.save()
        
        messages.success(request, 'Carga académica actualizada exitosamente')
        return redirect('carga_academica_lista')
    
    materias = Materia.objects.all()
    docentes = Docente.objects.all()
    aulas = Aula.objects.all()
    
    context = {
        'carga': carga,
        'materias': materias,
        'docentes': docentes,
        'aulas': aulas,
        'editar': True
    }
    return render(request, 'academico/coordinador/carga_academica_form.html', context)

@login_required
def carga_academica_eliminar(request, pk):
    """Eliminar carga académica"""
    carga = get_object_or_404(CargaAcademica, pk=pk)
    if request.method == 'POST':
        carga.delete()
        messages.success(request, 'Carga académica eliminada exitosamente')
        return redirect('carga_academica_lista')
    
    context = {'carga': carga}
    return render(request, 'academico/coordinador/carga_confirmar_eliminar.html', context)

# ========================================
# MICROCURRÍCULOS
# ========================================
@login_required
def microcurriculos_lista(request):
    """Lista de microcurrículos"""
    coordinador = get_object_or_404(Coordinador, usuario=request.user)
    microcurriculos = Microcurriculo.objects.filter(programa=coordinador.programa)
    
    context = {'microcurriculos': microcurriculos}
    return render(request, 'academico/coordinador/microcurriculos_lista.html', context)

@login_required
def microcurriculo_crear(request):
    """Crear microcurrículo"""
    if request.method == 'POST':
        coordinador = get_object_or_404(Coordinador, usuario=request.user)
        
        Microcurriculo.objects.create(
            codigo_microcurriculo=request.POST.get('codigo'),
            programa=coordinador.programa,
            nombre_materia=request.POST.get('nombre_materia'),
            numero_creditos=request.POST.get('creditos'),
            nivel_superior=request.POST.get('nivel_superior'),
            nivel_normal=request.POST.get('nivel_normal'),
            nivel_bajo=request.POST.get('nivel_bajo'),
            nivel_deficiente=request.POST.get('nivel_deficiente'),
            prerequisitos=request.POST.get('prerequisitos'),
            departamento_oferente=request.POST.get('departamento_oferente'),
            tipo_asignatura=request.POST.get('tipo_asignatura'),
            naturaleza_asignatura=request.POST.get('naturaleza_asignatura'),
            descripcion_asignatura=request.POST.get('descripcion'),
            objetivo_general=request.POST.get('objetivo_general'),
            objetivos_especificos=request.POST.get('objetivos_especificos'),
            competencias_genericas=request.POST.get('competencias_genericas'),
            estrategias_pedagogicas_metodologicas=request.POST.get('estrategias'),
            referencias_bibliograficas=request.POST.get('referencias'),
            primer_parcial=request.POST.get('primer_parcial'),
            segundo_parcial=request.POST.get('segundo_parcial'),
            tercer_parcial=request.POST.get('tercer_parcial')
        )
        
        messages.success(request, 'Microcurrículo creado exitosamente')
        return redirect('microcurriculos_lista')
    
    return render(request, 'academico/coordinador/microcurriculo_form.html')

@login_required
def microcurriculo_editar(request, pk):
    """Editar microcurrículo"""
    microcurriculo = get_object_or_404(Microcurriculo, pk=pk)
    
    if request.method == 'POST':
        microcurriculo.nombre_materia = request.POST.get('nombre_materia')
        microcurriculo.numero_creditos = request.POST.get('creditos')
        microcurriculo.nivel_superior = request.POST.get('nivel_superior')
        microcurriculo.nivel_normal = request.POST.get('nivel_normal')
        microcurriculo.nivel_bajo = request.POST.get('nivel_bajo')
        microcurriculo.nivel_deficiente = request.POST.get('nivel_deficiente')
        microcurriculo.prerequisitos = request.POST.get('prerequisitos')
        microcurriculo.departamento_oferente = request.POST.get('departamento_oferente')
        microcurriculo.tipo_asignatura = request.POST.get('tipo_asignatura')
        microcurriculo.naturaleza_asignatura = request.POST.get('naturaleza_asignatura')
        microcurriculo.descripcion_asignatura = request.POST.get('descripcion')
        microcurriculo.objetivo_general = request.POST.get('objetivo_general')
        microcurriculo.objetivos_especificos = request.POST.get('objetivos_especificos')
        microcurriculo.competencias_genericas = request.POST.get('competencias_genericas')
        microcurriculo.estrategias_pedagogicas_metodologicas = request.POST.get('estrategias')
        microcurriculo.referencias_bibliograficas = request.POST.get('referencias')
        microcurriculo.primer_parcial = request.POST.get('primer_parcial')
        microcurriculo.segundo_parcial = request.POST.get('segundo_parcial')
        microcurriculo.tercer_parcial = request.POST.get('tercer_parcial')
        microcurriculo.save()
        
        messages.success(request, 'Microcurrículo actualizado exitosamente')
        return redirect('microcurriculos_lista')
    
    context = {
        'microcurriculo': microcurriculo,
        'editar': True
    }
    return render(request, 'academico/coordinador/microcurriculo_form.html', context)

@login_required
def microcurriculo_ver(request, pk):
    """Ver detalle del microcurrículo"""
    microcurriculo = get_object_or_404(Microcurriculo, pk=pk)
    competencias = ContenidoCompetenciasEspecificas.objects.filter(microcurriculo=microcurriculo)
    
    context = {
        'microcurriculo': microcurriculo,
        'competencias': competencias
    }
    return render(request, 'academico/coordinador/microcurriculo_detalle.html', context)

# ========================================
# HORARIOS
# ========================================
@login_required
def horarios_docentes(request):
    """Ver horarios de docentes"""
    coordinador = get_object_or_404(Coordinador, usuario=request.user)
    docentes = Docente.objects.filter(cargas_academicas__programa=coordinador.programa).distinct()
    
    docente_id = request.GET.get('docente')
    horarios = None
    
    if docente_id:
        horarios = HorarioDocente.objects.filter(docente_id=docente_id)
    
    context = {
        'docentes': docentes,
        'horarios': horarios,
        'docente_seleccionado': docente_id
    }
    return render(request, 'academico/coordinador/horarios_docentes.html', context)

@login_required
def horarios_estudiantes(request):
    """Ver horarios de estudiantes"""
    coordinador = get_object_or_404(Coordinador, usuario=request.user)
    estudiantes = Estudiante.objects.filter(programa=coordinador.programa)
    
    estudiante_id = request.GET.get('estudiante')
    horarios = None
    
    if estudiante_id:
        horarios = HorarioEstudiante.objects.filter(estudiante_id=estudiante_id)
    
    context = {
        'estudiantes': estudiantes,
        'horarios': horarios,
        'estudiante_seleccionado': estudiante_id
    }
    return render(request, 'academico/coordinador/horarios_estudiantes.html', context)

# ========================================
# DASHBOARD DOCENTE
# ========================================
@login_required
def docente_dashboard(request):
    """Dashboard del docente"""
    try:
        docente = Docente.objects.get(usuario=request.user)
        
        context = {
            'docente': docente,
            'total_materias': MateriaDocente.objects.filter(docente=docente).count(),
            'total_asistencias': Asistencia.objects.filter(docente_responsable=docente).count(),
            'proximas_clases': CargaAcademica.objects.filter(docente=docente)[:5],
        }
        return render(request, 'academico/docente/dashboard.html', context)
    except Docente.DoesNotExist:
        messages.error(request, 'No tienes un perfil de docente asignado')
        return redirect('index')

# ========================================
# ASISTENCIAS
# ========================================
@login_required
def asistencias_lista(request):
    """Lista de asistencias del docente"""
    docente = get_object_or_404(Docente, usuario=request.user)
    asistencias = Asistencia.objects.filter(docente_responsable=docente).order_by('-fecha', '-hora')
    
    paginator = Paginator(asistencias, 10)
    page = request.GET.get('page')
    asistencias = paginator.get_page(page)
    
    context = {'asistencias': asistencias}
    return render(request, 'academico/docente/asistencias_lista.html', context)

@login_required
def asistencia_crear(request):
    """Crear registro de asistencia"""
    if request.method == 'POST':
        docente = get_object_or_404(Docente, usuario=request.user)
        
        Asistencia.objects.create(
            docente_responsable=docente,
            asignatura=request.POST.get('asignatura'),
            codigo_asignatura=request.POST.get('codigo_asignatura'),
            grupo=request.POST.get('grupo'),
            tema=request.POST.get('tema'),
            fecha=request.POST.get('fecha'),
            sede=request.POST.get('sede'),
            aula_id=request.POST.get('aula'),
            hora=request.POST.get('hora')
        )
        
        messages.success(request, 'Asistencia creada exitosamente')
        return redirect('asistencias_lista')
    
    aulas = Aula.objects.all()
    materias = Materia.objects.all()
    
    context = {
        'aulas': aulas,
        'materias': materias
    }
    return render(request, 'academico/docente/asistencia_form.html', context)

@login_required
def asistencia_registrar(request, pk):
    """Registrar estudiantes en la asistencia"""
    asistencia = get_object_or_404(Asistencia, pk=pk)
    
    if request.method == 'POST':
        # Obtener todos los estudiantes del formulario
        estudiantes_ids = request.POST.getlist('estudiantes')
        estados = request.POST.getlist('estados')
        
        for i, est_id in enumerate(estudiantes_ids):
            estudiante = Estudiante.objects.get(pk=est_id)
            DetalleAsistencia.objects.update_or_create(
                asistencia=asistencia,
                estudiante=estudiante,
                defaults={
                    'estado': estados[i] if i < len(estados) else 'A',
                    'observacion': request.POST.get(f'observacion_{est_id}', '')
                }
            )
        
        messages.success(request, 'Asistencia registrada exitosamente')
        return redirect('asistencias_lista')
    
    # Obtener estudiantes del programa relacionado con la materia
    estudiantes = Estudiante.objects.all()[:50]  # Limitar para demo
    detalles_existentes = DetalleAsistencia.objects.filter(asistencia=asistencia)
    
    context = {
        'asistencia': asistencia,
        'estudiantes': estudiantes,
        'detalles_existentes': detalles_existentes
    }
    return render(request, 'academico/docente/asistencia_registrar.html', context)

@login_required
def asistencia_ver(request, pk):
    """Ver detalle de asistencia"""
    asistencia = get_object_or_404(Asistencia, pk=pk)
    detalles = DetalleAsistencia.objects.filter(asistencia=asistencia).select_related('estudiante')
    
    # Estadísticas
    total = detalles.count()
    presentes = detalles.filter(estado='P').count()
    ausentes = detalles.filter(estado='A').count()
    tardanzas = detalles.filter(estado='T').count()
    excusas = detalles.filter(estado='E').count()
    
    context = {
        'asistencia': asistencia,
        'detalles': detalles,
        'total': total,
        'presentes': presentes,
        'ausentes': ausentes,
        'tardanzas': tardanzas,
        'excusas': excusas,
        'porcentaje_asistencia': (presentes / total * 100) if total > 0 else 0
    }
    return render(request, 'academico/docente/asistencia_detalle.html', context)

# ========================================
# PLAN MICROCURRÍCULO (DOCENTE)
# ========================================
@login_required
def plan_microcurriculo_lista(request):
    """Lista de planes de microcurrículo del docente"""
    docente = get_object_or_404(Docente, usuario=request.user)
    planes = PlanMicrocurriculo.objects.filter(docente=docente)
    
    context = {'planes': planes}
    return render(request, 'academico/docente/plan_microcurriculo_lista.html', context)

@login_required
def plan_microcurriculo_crear(request):
    """Crear plan de microcurrículo"""
    if request.method == 'POST':
        docente = get_object_or_404(Docente, usuario=request.user)
        
        PlanMicrocurriculo.objects.create(
            microcurriculo_id=request.POST.get('microcurriculo'),
            docente=docente,
            programa_id=request.POST.get('programa'),
            facultad_id=request.POST.get('facultad'),
            año_lectivo=request.POST.get('año_lectivo'),
            periodo_academico=request.POST.get('periodo'),
            fecha_inicio=request.POST.get('fecha_inicio'),
            total_horas=request.POST.get('total_horas'),
            fecha_terminacion=request.POST.get('fecha_terminacion')
        )
        
        messages.success(request, 'Plan de microcurrículo creado exitosamente')
        return redirect('plan_microcurriculo_lista')
    
    microcurriculos = Microcurriculo.objects.all()
    programas = Programa.objects.all()
    facultades = Facultad.objects.all()
    
    context = {
        'microcurriculos': microcurriculos,
        'programas': programas,
        'facultades': facultades
    }
    return render(request, 'academico/docente/plan_microcurriculo_form.html', context)

@login_required
def plan_microcurriculo_ver(request, pk):
    """Ver plan de microcurrículo con detalles"""
    plan = get_object_or_404(PlanMicrocurriculo, pk=pk)
    detalles = DetallePlanMicrocurriculo.objects.filter(plan_microcurriculo=plan)
    
    context = {
        'plan': plan,
        'detalles': detalles
    }
    return render(request, 'academico/docente/plan_microcurriculo_detalle.html', context)

# ========================================
# HORARIO DOCENTE
# ========================================
@login_required
def docente_horario(request):
    """Ver horario del docente"""
    docente = get_object_or_404(Docente, usuario=request.user)
    horarios = HorarioDocente.objects.filter(docente=docente).order_by('dia', 'hora')
    
    context = {'horarios': horarios}
    return render(request, 'academico/docente/horario.html', context)

# ========================================
# DASHBOARD ESTUDIANTE
# ========================================
@login_required
def estudiante_dashboard(request):
    """Dashboard del estudiante"""
    try:
        estudiante = Estudiante.objects.get(usuario=request.user)
        
        context = {
            'estudiante': estudiante,
            'total_materias': HorarioEstudiante.objects.filter(estudiante=estudiante).count(),
            'programa': estudiante.programa,
            'facultad': estudiante.facultad,
        }
        return render(request, 'academico/estudiante/dashboard.html', context)
    except Estudiante.DoesNotExist:
        messages.error(request, 'No tienes un perfil de estudiante asignado')
        return redirect('index')

# ========================================
# HORARIO ESTUDIANTE
# ========================================
@login_required
def estudiante_horario(request):
    """Ver horario del estudiante"""
    estudiante = get_object_or_404(Estudiante, usuario=request.user)
    horarios = HorarioEstudiante.objects.filter(estudiante=estudiante).order_by('dia', 'hora')
    
    context = {'horarios': horarios}
    return render(request, 'academico/estudiante/horario.html', context)

@login_required
def estudiante_crear_horario(request):
    """Estudiante crea su horario"""
    if request.method == 'POST':
        estudiante = get_object_or_404(Estudiante, usuario=request.user)
        
        HorarioEstudiante.objects.create(
            estudiante=estudiante,
            materia_id=request.POST.get('materia'),
            aula_id=request.POST.get('aula'),
            hora=request.POST.get('hora'),
            grupo=request.POST.get('grupo'),
            dia=request.POST.get('dia'),
            periodo=request.POST.get('periodo')
        )
        
        messages.success(request, 'Materia agregada al horario exitosamente')
        return redirect('estudiante_horario')
    
    materias = Materia.objects.all()
    aulas = Aula.objects.all()
    
    context = {
        'materias': materias,
        'aulas': aulas
    }
    return render(request, 'academico/estudiante/crear_horario.html', context)

# ========================================
# ASISTENCIAS ESTUDIANTE
# ========================================
@login_required
def estudiante_asistencias(request):
    """Ver asistencias del estudiante"""
    estudiante = get_object_or_404(Estudiante, usuario=request.user)
    asistencias = DetalleAsistencia.objects.filter(estudiante=estudiante).select_related('asistencia')
    
    paginator = Paginator(asistencias, 15)
    page = request.GET.get('page')
    asistencias = paginator.get_page(page)
    
    context = {'asistencias': asistencias}
    return render(request, 'academico/estudiante/asistencias.html', context)

# ========================================
# SEGUIMIENTO MICROCURRÍCULO
# ========================================
@login_required
def estudiante_seguimiento_microcurriculo(request):
    """Seguimiento del microcurrículo para estudiante"""
    estudiante = get_object_or_404(Estudiante, usuario=request.user)
    microcurriculos = Microcurriculo.objects.filter(programa=estudiante.programa)
    
    context = {'microcurriculos': microcurriculos}
    return render(request, 'academico/estudiante/seguimiento_microcurriculo.html', context)