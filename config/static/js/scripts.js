// ========================================
// SISTEMA ACADÉMICO - SCRIPTS PERSONALIZADOS
// ========================================

document.addEventListener('DOMContentLoaded', function() {
    
    // ========================================
    // CONFIRMACIÓN DE ELIMINACIÓN
    // ========================================
    const deleteButtons = document.querySelectorAll('.btn-delete, .delete-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('¿Estás seguro de que deseas eliminar este elemento? Esta acción no se puede deshacer.')) {
                e.preventDefault();
            }
        });
    });

    // ========================================
    // AUTO-DISMISS ALERTAS
    // ========================================
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000); // 5 segundos
    });

    // ========================================
    // TOOLTIPS DE BOOTSTRAP
    // ========================================
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // ========================================
    // POPOVERS DE BOOTSTRAP
    // ========================================
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // ========================================
    // BÚSQUEDA EN TABLAS
    // ========================================
    const searchInput = document.getElementById('table-search');
    if (searchInput) {
        searchInput.addEventListener('keyup', function() {
            const filter = this.value.toLowerCase();
            const table = document.querySelector('table tbody');
            const rows = table.getElementsByTagName('tr');

            for (let i = 0; i < rows.length; i++) {
                const row = rows[i];
                const cells = row.getElementsByTagName('td');
                let found = false;

                for (let j = 0; j < cells.length; j++) {
                    const cell = cells[j];
                    if (cell.textContent.toLowerCase().indexOf(filter) > -1) {
                        found = true;
                        break;
                    }
                }

                row.style.display = found ? '' : 'none';
            }
        });
    }

    // ========================================
    // VALIDACIÓN DE FORMULARIOS
    // ========================================
    const forms = document.querySelectorAll('.needs-validation');
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    // ========================================
    // SELECTOR DE TODOS LOS CHECKBOXES
    // ========================================
    const selectAllCheckbox = document.getElementById('select-all');
    if (selectAllCheckbox) {
        selectAllCheckbox.addEventListener('change', function() {
            const checkboxes = document.querySelectorAll('.item-checkbox');
            checkboxes.forEach(checkbox => {
                checkbox.checked = this.checked;
            });
        });
    }

    // ========================================
    // CONTADOR DE CARACTERES
    // ========================================
    const textareas = document.querySelectorAll('textarea[maxlength]');
    textareas.forEach(textarea => {
        const maxLength = textarea.getAttribute('maxlength');
        const counter = document.createElement('small');
        counter.className = 'text-muted';
        counter.textContent = `0 / ${maxLength} caracteres`;
        textarea.parentNode.appendChild(counter);

        textarea.addEventListener('input', function() {
            const currentLength = this.value.length;
            counter.textContent = `${currentLength} / ${maxLength} caracteres`;
            
            if (currentLength > maxLength * 0.9) {
                counter.classList.add('text-danger');
            } else {
                counter.classList.remove('text-danger');
            }
        });
    });

    // ========================================
    // PREVISUALIZACIÓN DE IMÁGENES
    // ========================================
    const imageInputs = document.querySelectorAll('input[type="file"][accept*="image"]');
    imageInputs.forEach(input => {
        input.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    let preview = input.parentNode.querySelector('.image-preview');
                    if (!preview) {
                        preview = document.createElement('img');
                        preview.className = 'image-preview mt-2 img-thumbnail';
                        preview.style.maxWidth = '200px';
                        input.parentNode.appendChild(preview);
                    }
                    preview.src = e.target.result;
                };
                reader.readAsDataURL(file);
            }
        });
    });

    // ========================================
    // CARGA DINÁMICA DE PROGRAMAS POR FACULTAD
    // ========================================
    const facultadSelect = document.getElementById('id_facultad');
    const programaSelect = document.getElementById('id_programa');
    
    if (facultadSelect && programaSelect) {
        facultadSelect.addEventListener('change', function() {
            const facultadId = this.value;
            
            if (facultadId) {
                fetch(`/api/programas/by-facultad/${facultadId}/`)
                    .then(response => response.json())
                    .then(data => {
                        programaSelect.innerHTML = '<option value="">Seleccione un programa</option>';
                        data.forEach(programa => {
                            const option = document.createElement('option');
                            option.value = programa.codigo_programa;
                            option.textContent = programa.nombre_programa;
                            programaSelect.appendChild(option);
                        });
                    })
                    .catch(error => {
                        console.error('Error al cargar programas:', error);
                        programaSelect.innerHTML = '<option value="">Error al cargar programas</option>';
                    });
            } else {
                programaSelect.innerHTML = '<option value="">Seleccione primero una facultad</option>';
            }
        });
    }

    // ========================================
    // REGISTRO DE ASISTENCIA
    // ========================================
    const asistenciaCheckboxes = document.querySelectorAll('.asistencia-checkbox');
    asistenciaCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const row = this.closest('tr');
            const estado = this.value;
            
            // Cambiar color de fila según estado
            row.classList.remove('asistencia-presente', 'asistencia-ausente', 'asistencia-tardanza', 'asistencia-excusa');
            
            if (estado === 'P') {
                row.classList.add('asistencia-presente');
            } else if (estado === 'A') {
                row.classList.add('asistencia-ausente');
            } else if (estado === 'T') {
                row.classList.add('asistencia-tardanza');
            } else if (estado === 'E') {
                row.classList.add('asistencia-excusa');
            }
        });
    });

    // ========================================
    // RELOJ EN TIEMPO REAL
    // ========================================
    const clockElement = document.getElementById('live-clock');
    if (clockElement) {
        function updateClock() {
            const now = new Date();
            const options = { 
                weekday: 'long', 
                year: 'numeric', 
                month: 'long', 
                day: 'numeric',
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit'
            };
            clockElement.textContent = now.toLocaleDateString('es-CO', options);
        }
        updateClock();
        setInterval(updateClock, 1000);
    }

    // ========================================
    // GRÁFICOS DE ESTADÍSTICAS (Chart.js)
    // ========================================
    const estadisticasCanvas = document.getElementById('estadisticas-chart');
    if (estadisticasCanvas && typeof Chart !== 'undefined') {
        // Aquí se pueden agregar gráficos personalizados
        // Ejemplo básico:
        const ctx = estadisticasCanvas.getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
                datasets: [{
                    label: 'Asistencias',
                    data: [12, 19, 3, 5, 2, 3],
                    backgroundColor: 'rgba(54, 162, 235, 0.5)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    // ========================================
    // EXPORTAR TABLA A CSV
    // ========================================
    const exportCsvBtn = document.getElementById('export-csv');
    if (exportCsvBtn) {
        exportCsvBtn.addEventListener('click', function() {
            const table = document.querySelector('table');
            let csv = [];
            const rows = table.querySelectorAll('tr');

            rows.forEach(row => {
                const cols = row.querySelectorAll('td, th');
                const csvRow = [];
                cols.forEach(col => {
                    csvRow.push(col.textContent.trim());
                });
                csv.push(csvRow.join(','));
            });

            const csvContent = csv.join('\n');
            const blob = new Blob([csvContent], { type: 'text/csv' });
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'datos.csv';
            a.click();
        });
    }

    // ========================================
    // IMPRIMIR PÁGINA
    // ========================================
    const printBtn = document.getElementById('print-btn');
    if (printBtn) {
        printBtn.addEventListener('click', function() {
            window.print();
        });
    }

    // ========================================
    // CAMBIO DINÁMICO DE TEMA
    // ========================================
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        const currentTheme = localStorage.getItem('theme') || 'light';
        document.documentElement.setAttribute('data-theme', currentTheme);

        themeToggle.addEventListener('click', function() {
            const theme = document.documentElement.getAttribute('data-theme');
            const newTheme = theme === 'light' ? 'dark' : 'light';
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
        });
    }

    // ========================================
    // NOTIFICACIONES TOAST
    // ========================================
    function showToast(message, type = 'success') {
        const toastContainer = document.getElementById('toast-container');
        if (!toastContainer) {
            const container = document.createElement('div');
            container.id = 'toast-container';
            container.className = 'position-fixed bottom-0 end-0 p-3';
            container.style.zIndex = '11';
            document.body.appendChild(container);
        }

        const toast = document.createElement('div');
        toast.className = `toast align-items-center text-white bg-${type} border-0`;
        toast.setAttribute('role', 'alert');
        toast.innerHTML = `
            <div class="d-flex">
                <div class="toast-body">${message}</div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
            </div>
        `;

        document.getElementById('toast-container').appendChild(toast);
        const bsToast = new bootstrap.Toast(toast);
        bsToast.show();

        toast.addEventListener('hidden.bs.toast', function() {
            toast.remove();
        });
    }

    // Exponer función showToast globalmente
    window.showToast = showToast;

    // ========================================
    // SCROLL SUAVE
    // ========================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // ========================================
    // VALIDACIÓN DE FECHAS
    // ========================================
    const fechaInicioInput = document.getElementById('id_fecha_inicio');
    const fechaFinInput = document.getElementById('id_fecha_terminacion');
    
    if (fechaInicioInput && fechaFinInput) {
        fechaInicioInput.addEventListener('change', function() {
            fechaFinInput.min = this.value;
        });

        fechaFinInput.addEventListener('change', function() {
            if (this.value < fechaInicioInput.value) {
                alert('La fecha de terminación no puede ser anterior a la fecha de inicio');
                this.value = '';
            }
        });
    }

    // ========================================
    // CÁLCULO AUTOMÁTICO DE PORCENTAJES
    // ========================================
    const parcialInputs = document.querySelectorAll('.parcial-input');
    if (parcialInputs.length > 0) {
        parcialInputs.forEach(input => {
            input.addEventListener('input', function() {
                let total = 0;
                parcialInputs.forEach(inp => {
                    total += parseFloat(inp.value) || 0;
                });

                const totalDisplay = document.getElementById('total-porcentaje');
                if (totalDisplay) {
                    totalDisplay.textContent = `Total: ${total}%`;
                    
                    if (total === 100) {
                        totalDisplay.classList.remove('text-danger');
                        totalDisplay.classList.add('text-success');
                    } else {
                        totalDisplay.classList.remove('text-success');
                        totalDisplay.classList.add('text-danger');
                    }
                }
            });
        });
    }

    // ========================================
    // LOADING SPINNER EN FORMULARIOS
    // ========================================
    const formsWithLoading = document.querySelectorAll('form.form-with-loading');
    formsWithLoading.forEach(form => {
        form.addEventListener('submit', function() {
            const submitBtn = this.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Procesando...';
            }
        });
    });

    // ========================================
    // FILTROS AVANZADOS
    // ========================================
    const filterForm = document.getElementById('filter-form');
    if (filterForm) {
        const filterInputs = filterForm.querySelectorAll('input, select');
        filterInputs.forEach(input => {
            input.addEventListener('change', function() {
                filterForm.submit();
            });
        });
    }

    // ========================================
    // COPIAR AL PORTAPAPELES
    // ========================================
    const copyButtons = document.querySelectorAll('.copy-btn');
    copyButtons.forEach(button => {
        button.addEventListener('click', function() {
            const textToCopy = this.getAttribute('data-copy');
            navigator.clipboard.writeText(textToCopy).then(() => {
                showToast('Copiado al portapapeles', 'success');
            });
        });
    });

    console.log('Sistema Académico - Scripts cargados correctamente');
});

// ========================================
// FUNCIONES GLOBALES
// ========================================

// Función para formatear números
function formatNumber(num) {
    return new Intl.NumberFormat('es-CO').format(num);
}

// Función para formatear fechas
function formatDate(date) {
    return new Date(date).toLocaleDateString('es-CO', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}

// Función para confirmar acción
function confirmAction(message) {
    return confirm(message || '¿Estás seguro de realizar esta acción?');
}