// Document Ready
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips and popovers
    initializeTooltips();
    
    // Handle image preview
    handleImagePreview();
    
    // Form validation
    validateForms();
});

/** Initialize Bootstrap Tooltips */
function initializeTooltips() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

/** Handle Image Preview on File Upload */
function handleImagePreview() {
    const fileInput = document.getElementById('image');
    if (fileInput) {
        fileInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(event) {
                    const preview = document.getElementById('imagePreview');
                    if (preview) {
                        preview.src = event.target.result;
                        preview.style.display = 'block';
                    }
                };
                reader.readAsDataURL(file);
            }
        });
    }
}

/** Form Validation */
function validateForms() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!form.checkValidity()) {
                e.preventDefault();
                e.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });
}

/** Alert Auto-dismiss */
function dismissAlert(delay = 5000) {
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bootstrapAlert = new bootstrap.Alert(alert);
            bootstrapAlert.close();
        }, delay);
    });
}

/** Format Date */
function formatDate(date) {
    const options = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' };
    return new Date(date).toLocaleDateString('en-US', options);
}

/** Confirm Delete */
function confirmDelete(message = 'Are you sure you want to delete this?') {
    return confirm(message);
}

/** Show Loading Spinner */
function showSpinner(message = 'Loading...') {
    const spinnerHTML = `
        <div id="loading-spinner" class="fixed-top d-flex align-items-center justify-content-center" style="background: rgba(0,0,0,0.5); z-index: 9999; width: 100%; height: 100%;">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">${message}</span>
            </div>
        </div>
    `;
    document.body.insertAdjacentHTML('beforeend', spinnerHTML);
}

/** Hide Loading Spinner */
function hideSpinner() {
    const spinner = document.getElementById('loading-spinner');
    if (spinner) {
        spinner.remove();
    }
}

/** Copy to Clipboard */
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showAlert('Copied to clipboard!', 'success');
    }).catch(() => {
        showAlert('Failed to copy', 'danger');
    });
}

/** Show Alert Toast */
function showAlert(message, type = 'info') {
    const alertHTML = `
        <div class="alert alert-${type} alert-dismissible fade show position-fixed" style="top: 20px; right: 20px; z-index: 9999; min-width: 300px;" role="alert">
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;
    document.body.insertAdjacentHTML('beforeend', alertHTML);
    const alertElement = document.body.lastElementChild;
    setTimeout(() => {
        const bootstrapAlert = new bootstrap.Alert(alertElement);
        bootstrapAlert.close();
    }, 3000);
}

/** Debounce Function */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/** Filter Table */
function filterTable(inputId, tableId) {
    const input = document.getElementById(inputId);
    if (!input) return;
    
    input.addEventListener('keyup', debounce(function() {
        const filter = input.value.toUpperCase();
        const table = document.getElementById(tableId);
        const rows = table.getElementsByTagName('tr');
        
        for (let i = 1; i < rows.length; i++) {
            const text = rows[i].textContent.toUpperCase();
            rows[i].style.display = text.includes(filter) ? '' : 'none';
        }
    }, 300));
}

/** Export Table to CSV */
function exportTableToCSV(tableId, filename = 'export.csv') {
    const table = document.getElementById(tableId);
    if (!table) return;
    
    let csv = [];
    const rows = table.querySelectorAll('tr');
    
    rows.forEach(row => {
        const cols = row.querySelectorAll('td, th');
        const csvRow = [];
        cols.forEach(col => {
            csvRow.push('"' + col.textContent + '"');
        });
        csv.push(csvRow.join(','));
    });
    
    downloadCSV(csv.join('\n'), filename);
}

/** Download CSV */
function downloadCSV(csv, filename) {
    const BOM = '\uFEFF';
    const csvFile = new Blob([BOM + csv], {type: 'text/csv;charset=utf-8;'});
    const link = document.createElement('a');
    const url = URL.createObjectURL(csvFile);
    
    link.setAttribute('href', url);
    link.setAttribute('download', filename);
    link.style.visibility = 'hidden';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

/** Initialize Complaints Map on User Dashboard */
function initMap() {
    // Only init if map container exists and user logged in
    const mapContainer = document.getElementById('map');
    if (!mapContainer || !window.sessionStorage.getItem('user_id')) return;

    // Initialize Leaflet map centered on Tamil Nadu
    const map = L.map('map').setView([11.1271, 78.6569], 7);
    
    // Add OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Fetch complaint data
    fetch('/map-data')
        .then(response => response.json())
        .then(data => {
            // Color mapping by status
            const statusColors = {
                'Pending': '#ff0000',
                'In Progress': '#ffaa00',
                'Resolved': '#00aa00'
            };

            data.forEach(complaint => {
                const markerColor = statusColors[complaint.status] || '#3388ff';
                
                // Custom marker icon
                const markerIcon = L.divIcon({
                    className: 'complaint-marker',
                    html: `<div style="background-color: ${markerColor}; width: 20px; height: 20px; border-radius: 50%; border: 3px solid white; box-shadow: 0 2px 6px rgba(0,0,0,0.3);"></div>`,
                    iconSize: [26, 26],
                    iconAnchor: [13, 13]
                });

                L.marker([complaint.lat, complaint.lng], {icon: markerIcon})
                    .addTo(map)
                    .bindPopup(`
                        <div style="min-width: 200px;">
                            <h6 style="margin: 0 0 8px 0; color: #333;">${complaint.title}</h6>
                            <span class="badge bg-${complaint.status === 'Pending' ? 'danger' : complaint.status === 'In Progress' ? 'warning' : 'success'}">${complaint.status}</span>
                        </div>
                    `);
            });

            // Fit map to markers if any exist
            if (data.length > 0) {
                map.fitBounds(L.latLngBounds(data.map(c => [c.lat, c.lng])));
            }
        })
        .catch(error => {
            console.error('Map data fetch error:', error);
        });
}

/** Initialize Page */
window.addEventListener('load', function() {
    dismissAlert(5000);
    initMap();  // Initialize map after page load
});
