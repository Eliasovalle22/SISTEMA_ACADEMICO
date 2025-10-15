from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# ===============================
# MODELO ADMINISTRADOR
# ===============================
class Administrador(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro')
    ]
    
    id_administrador = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    celular = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ===============================
# MODELO FACULTAD
# ===============================
class Facultad(models.Model):
    codigo_facultad = models.CharField(max_length=20, primary_key=True)
    nombre_facultad = models.CharField(max_length=200)
    numero_programas = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Facultad'
        verbose_name_plural = 'Facultades'
    
    def __str__(self):
        return self.nombre_facultad

# ===============================
# MODELO PROGRAMA
# ===============================
class Programa(models.Model):
    codigo_programa = models.CharField(max_length=20, primary_key=True)
    nombre_programa = models.CharField(max_length=200)
    numero_creditos = models.IntegerField()
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE, related_name='programas')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'
    
    def __str__(self):
        return self.nombre_programa

# ===============================
# MODELO COORDINADOR
# ===============================
class Coordinador(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro')
    ]
    
    id_coordinador = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    celular = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name='coordinadores')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Coordinador'
        verbose_name_plural = 'Coordinadores'
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.programa}"

# ===============================
# MODELO MATERIA
# ===============================
class Materia(models.Model):
    codigo_materia = models.CharField(max_length=20, primary_key=True)
    nombre_materia = models.CharField(max_length=200)
    numero_creditos = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'
    
    def __str__(self):
        return self.nombre_materia

# ===============================
# MODELO DOCENTE
# ===============================
class Docente(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro')
    ]
    
    id_docente = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre_docente = models.CharField(max_length=100)
    apellido_docente = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    celular = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
    
    def __str__(self):
        return f"{self.nombre_docente} {self.apellido_docente}"

# ===============================
# MODELO ESTUDIANTE
# ===============================
class Estudiante(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        ('PA', 'Pasaporte')
    ]
    
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro')
    ]
    
    ESTADO_CIVIL_CHOICES = [
        ('S', 'Soltero'),
        ('C', 'Casado'),
        ('U', 'Unión Libre'),
        ('D', 'Divorciado'),
        ('V', 'Viudo')
    ]
    
    id_estudiante = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    tipo_documento = models.CharField(max_length=2, choices=TIPO_DOCUMENTO_CHOICES)
    fecha_expedicion = models.DateField()
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    celular = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL_CHOICES)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    puntaje_icfes = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    nombre_acudiente = models.CharField(max_length=100)
    apellido_acudiente = models.CharField(max_length=100)
    celular_acudiente = models.CharField(max_length=20)
    sisben = models.CharField(max_length=10, null=True, blank=True)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE, related_name='estudiantes')
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name='estudiantes')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.programa}"

# ===============================
# MODELO AULA
# ===============================
class Aula(models.Model):
    codigo_aula = models.CharField(max_length=20, primary_key=True)
    nombre_aula = models.CharField(max_length=100)
    capacidad = models.IntegerField(default=30)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'
    
    def __str__(self):
        return self.nombre_aula

# ===============================
# MODELO ASISTENCIA
# ===============================
class Asistencia(models.Model):
    codigo_asistencia = models.AutoField(primary_key=True)
    docente_responsable = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='asistencias')
    asignatura = models.CharField(max_length=200)
    codigo_asignatura = models.CharField(max_length=20)
    grupo = models.CharField(max_length=10)
    tema = models.TextField()
    fecha = models.DateField()
    sede = models.CharField(max_length=100)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, related_name='asistencias')
    hora = models.TimeField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'
        ordering = ['-fecha', '-hora']
    
    def __str__(self):
        return f"{self.asignatura} - {self.fecha} - {self.grupo}"

# ===============================
# MODELO DETALLE ASISTENCIA
# ===============================
class DetalleAsistencia(models.Model):
    ESTADO_CHOICES = [
        ('P', 'Presente'),
        ('A', 'Ausente'),
        ('T', 'Tardanza'),
        ('E', 'Excusa')
    ]
    
    id_detalle = models.AutoField(primary_key=True)
    asistencia = models.ForeignKey(Asistencia, on_delete=models.CASCADE, related_name='detalles')
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='asistencias')
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='A')
    observacion = models.TextField(null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Detalle de Asistencia'
        verbose_name_plural = 'Detalles de Asistencia'
        unique_together = ['asistencia', 'estudiante']
    
    def __str__(self):
        return f"{self.estudiante} - {self.asistencia} - {self.get_estado_display()}"

# ===============================
# MODELO SENSOR ASISTENCIA
# ===============================
class SensorAsistencia(models.Model):
    codigo_sensor = models.CharField(max_length=50, primary_key=True)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, related_name='sensores')
    nombre_aula = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    fecha_instalacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Sensor de Asistencia'
        verbose_name_plural = 'Sensores de Asistencia'
    
    def __str__(self):
        return f"Sensor {self.codigo_sensor} - {self.nombre_aula}"

# ===============================
# MODELO MICROCURRICULO
# ===============================
class Microcurriculo(models.Model):
    TIPO_ASIGNATURA_CHOICES = [
        ('OB', 'Obligatoria'),
        ('OP', 'Optativa'),
        ('EL', 'Electiva')
    ]
    
    NATURALEZA_ASIGNATURA_CHOICES = [
        ('TE', 'Teórica'),
        ('PR', 'Práctica'),
        ('TP', 'Teórico-Práctica')
    ]
    
    codigo_microcurriculo = models.CharField(max_length=20, primary_key=True)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name='microcurriculos')
    nombre_materia = models.CharField(max_length=200)
    numero_creditos = models.IntegerField()
    nivel_superior = models.TextField()
    nivel_normal = models.TextField()
    nivel_bajo = models.TextField()
    nivel_deficiente = models.TextField()
    prerequisitos = models.TextField(null=True, blank=True)
    departamento_oferente = models.CharField(max_length=200)
    tipo_asignatura = models.CharField(max_length=2, choices=TIPO_ASIGNATURA_CHOICES)
    naturaleza_asignatura = models.CharField(max_length=2, choices=NATURALEZA_ASIGNATURA_CHOICES)
    descripcion_asignatura = models.TextField()
    objetivo_general = models.TextField()
    objetivos_especificos = models.TextField()
    competencias_genericas = models.TextField()
    estrategias_pedagogicas_metodologicas = models.TextField()
    referencias_bibliograficas = models.TextField()
    primer_parcial = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    segundo_parcial = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    tercer_parcial = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Microcurrículo'
        verbose_name_plural = 'Microcurrículos'
    
    def __str__(self):
        return f"{self.nombre_materia} - {self.programa}"

# ===============================
# MODELO CONTENIDO COMPETENCIAS ESPECIFICAS
# ===============================
class ContenidoCompetenciasEspecificas(models.Model):
    codigo_competencia = models.AutoField(primary_key=True)
    microcurriculo = models.ForeignKey(Microcurriculo, on_delete=models.CASCADE, related_name='competencias')
    unidad_tematica = models.CharField(max_length=200)
    competencias_especificas = models.TextField()
    resultados_de_aprendizaje = models.TextField()
    nivel_superior = models.TextField()
    nivel_normal = models.TextField()
    nivel_bajo = models.TextField()
    nivel_deficiente = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Contenido Competencias Específicas'
        verbose_name_plural = 'Contenidos Competencias Específicas'
    
    def __str__(self):
        return f"{self.unidad_tematica} - {self.microcurriculo}"

# ===============================
# MODELO PLAN MICROCURRICULO
# ===============================
class PlanMicrocurriculo(models.Model):
    codigo_plan_microcurriculo = models.AutoField(primary_key=True)
    microcurriculo = models.ForeignKey(Microcurriculo, on_delete=models.CASCADE, related_name='planes')
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='planes_microcurriculo')
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    año_lectivo = models.IntegerField()
    periodo_academico = models.CharField(max_length=20)
    fecha_inicio = models.DateField()
    total_horas = models.IntegerField()
    fecha_terminacion = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Plan de Microcurrículo'
        verbose_name_plural = 'Planes de Microcurrículo'
    
    def __str__(self):
        return f"{self.microcurriculo} - {self.periodo_academico} - {self.año_lectivo}"

# ===============================
# MODELO DETALLE PLAN MICROCURRICULO
# ===============================
class DetallePlanMicrocurriculo(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    plan_microcurriculo = models.ForeignKey(PlanMicrocurriculo, on_delete=models.CASCADE, related_name='detalles')
    semana = models.IntegerField()
    fecha_clase = models.DateField()
    tema = models.CharField(max_length=300)
    descripcion_actividad = models.TextField()
    horas_asignadas = models.IntegerField()
    recursos_necesarios = models.TextField()
    cumplido = models.BooleanField(default=False)
    observaciones = models.TextField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Detalle Plan de Microcurrículo'
        verbose_name_plural = 'Detalles Planes de Microcurrículo'
        ordering = ['semana', 'fecha_clase']
    
    def __str__(self):
        return f"Semana {self.semana} - {self.tema}"

# ===============================
# MODELO CARGA ACADEMICA
# ===============================
class CargaAcademica(models.Model):
    DIAS_SEMANA = [
        ('LU', 'Lunes'),
        ('MA', 'Martes'),
        ('MI', 'Miércoles'),
        ('JU', 'Jueves'),
        ('VI', 'Viernes'),
        ('SA', 'Sábado')
    ]
    
    id_carga = models.AutoField(primary_key=True)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name='cargas_academicas')
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='cargas_academicas')
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='cargas_academicas')
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, related_name='cargas_academicas')
    hora = models.TimeField()
    grupo = models.CharField(max_length=10)
    dia = models.CharField(max_length=2, choices=DIAS_SEMANA)
    periodo_carga = models.CharField(max_length=20)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Carga Académica'
        verbose_name_plural = 'Cargas Académicas'
    
    def __str__(self):
        return f"{self.materia} - {self.docente} - {self.grupo}"

# ===============================
# MODELO HORARIO ESTUDIANTE
# ===============================
class HorarioEstudiante(models.Model):
    DIAS_SEMANA = [
        ('LU', 'Lunes'),
        ('MA', 'Martes'),
        ('MI', 'Miércoles'),
        ('JU', 'Jueves'),
        ('VI', 'Viernes'),
        ('SA', 'Sábado')
    ]
    
    codigo_horario = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='horarios')
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    hora = models.TimeField()
    grupo = models.CharField(max_length=10)
    dia = models.CharField(max_length=2, choices=DIAS_SEMANA)
    periodo = models.CharField(max_length=20)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Horario Estudiante'
        verbose_name_plural = 'Horarios Estudiantes'
    
    def __str__(self):
        return f"{self.estudiante} - {self.materia} - {self.get_dia_display()}"

# ===============================
# MODELO MATERIA DOCENTE
# ===============================
class MateriaDocente(models.Model):
    codigo_materia_docente = models.AutoField(primary_key=True)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='materias_asignadas')
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='docentes_asignados')
    periodo = models.CharField(max_length=20)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Materia Docente'
        verbose_name_plural = 'Materias Docentes'
        unique_together = ['docente', 'materia', 'periodo']
    
    def __str__(self):
        return f"{self.docente} - {self.materia}"

# ===============================
# MODELO HORARIO DOCENTE
# ===============================
class HorarioDocente(models.Model):
    DIAS_SEMANA = [
        ('LU', 'Lunes'),
        ('MA', 'Martes'),
        ('MI', 'Miércoles'),
        ('JU', 'Jueves'),
        ('VI', 'Viernes'),
        ('SA', 'Sábado')
    ]
    
    codigo_horario_docente = models.AutoField(primary_key=True)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='horarios')
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    hora = models.TimeField()
    grupo = models.CharField(max_length=10)
    dia = models.CharField(max_length=2, choices=DIAS_SEMANA)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=20)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Horario Docente'
        verbose_name_plural = 'Horarios Docentes'
    
    def __str__(self):
        return f"{self.docente} - {self.materia} - {self.get_dia_display()}"