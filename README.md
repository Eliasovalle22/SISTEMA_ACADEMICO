# SISTEMA_ACADEMICO
    - software para un sistema académico para una institución educativa de nivel superior

# Análisis General del Sistema
    - Arquitectura Propuesta
    - Backend: Django (Python)
    - Frontend: Bootstrap 5 + HTML/CSS/JS
    - Base de Datos: PostgreSQL
    - Autenticación: Django Auth con roles personalizados

# Crear Entorno Virtual
    - python -m venv venv
    - venv\Scripts\activate

# Crear proyecto Django
    - django-admin startproject config .

# Crear aplicación principal
    - python manage.py startapp academico

# Instalar Dependencias
    - pip install -r requirements.txt

# Actualizar las Dependencias
    - pip freeze > requirements.txt

# Ejecutar Migraciones
    - python manage.py makemigrations
    - python manage.py migrate

# Crear Superusuario
    - python manage.py createsuperuser

# Recolectar Archivos Estáticos
    - python manage.py collectstatic --noinput
    
# Ejecutar el Servidor
    - python manage.py runserver
