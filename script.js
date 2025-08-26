// Tab switching functionality
function showTab(tabName) {
    // Hide all tab contents
    const tabContents = document.querySelectorAll('.tab-content');
    tabContents.forEach(content => {
        content.classList.remove('active');
    });

    // Remove active class from all tab buttons
    const tabButtons = document.querySelectorAll('.tab-button');
    tabButtons.forEach(button => {
        button.classList.remove('active');
    });

    // Show selected tab content
    document.getElementById(tabName).classList.add('active');

    // Add active class to clicked button
    event.target.classList.add('active');
}

// Initialize charts when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeRevenueChart();
    initializePipelineCharts();
});

// Revenue Chart
function initializeRevenueChart() {
    const ctx = document.getElementById('revenueChart').getContext('2d');
    
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['2024', '2025', '2026', '2027', '2028', '2029', '2030'],
            datasets: [
                {
                    label: 'High Growth Scenario',
                    data: [847, 925, 1010, 1105, 1208, 1320, 1420],
                    borderColor: '#28a745',
                    backgroundColor: 'rgba(40, 167, 69, 0.1)',
                    borderWidth: 3,
                    fill: true,
                    tension: 0.4
                },
                {
                    label: 'Base Case',
                    data: [847, 909, 975, 1047, 1124, 1206, 1280],
                    borderColor: '#007bff',
                    backgroundColor: 'rgba(0, 123, 255, 0.1)',
                    borderWidth: 3,
                    fill: true,
                    tension: 0.4
                },
                {
                    label: 'Low Growth Scenario',
                    data: [847, 896, 948, 1003, 1061, 1122, 1180],
                    borderColor: '#dc3545',
                    backgroundColor: 'rgba(220, 53, 69, 0.1)',
                    borderWidth: 3,
                    fill: true,
                    tension: 0.4
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: 'Citrate Buffer Market Projections (2024-2030)',
                    font: {
                        size: 16,
                        weight: 'bold'
                    }
                },
                legend: {
                    position: 'top',
                    labels: {
                        usePointStyle: true,
                        padding: 20
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Market Size ($ Millions)'
                    },
                    ticks: {
                        callback: function(value) {
                            return '$' + value + 'M';
                        }
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Year'
                    }
                }
            }
        }
    });
}

// Pipeline Charts
function initializePipelineCharts() {
    // Bispecific Antibodies Chart
    const bispecificsCtx = document.getElementById('bispecificsChart').getContext('2d');
    new Chart(bispecificsCtx, {
        type: 'bar',
        data: {
            labels: ['Preclinical', 'Phase I', 'Phase II', 'Phase III', 'Approved'],
            datasets: [{
                label: 'Number of Assets',
                data: [156, 89, 67, 23, 12],
                backgroundColor: [
                    'rgba(102, 126, 234, 0.8)',
                    'rgba(118, 75, 162, 0.8)',
                    'rgba(255, 193, 7, 0.8)',
                    'rgba(40, 167, 69, 0.8)',
                    'rgba(23, 162, 184, 0.8)'
                ],
                borderColor: [
                    'rgba(102, 126, 234, 1)',
                    'rgba(118, 75, 162, 1)',
                    'rgba(255, 193, 7, 1)',
                    'rgba(40, 167, 69, 1)',
                    'rgba(23, 162, 184, 1)'
                ],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Number of Assets'
                    }
                }
            }
        }
    });

    // Radiopharmaceuticals Chart
    const radiopharmaCtx = document.getElementById('radiopharmaChart').getContext('2d');
    new Chart(radiopharmaCtx, {
        type: 'bar',
        data: {
            labels: ['Preclinical', 'Phase I', 'Phase II', 'Phase III', 'Approved'],
            datasets: [{
                label: 'Number of Assets',
                data: [78, 45, 34, 18, 8],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.8)',
                    'rgba(54, 162, 235, 0.8)',
                    'rgba(255, 205, 86, 0.8)',
                    'rgba(75, 192, 192, 0.8)',
                    'rgba(153, 102, 255, 0.8)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 205, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)'
                ],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Number of Assets'
                    }
                }
            }
        }
    });

    // Cell Therapies Chart
    const cellTherapiesCtx = document.getElementById('cellTherapiesChart').getContext('2d');
    new Chart(cellTherapiesCtx, {
        type: 'bar',
        data: {
            labels: ['Preclinical', 'Phase I', 'Phase II', 'Phase III', 'Approved'],
            datasets: [{
                label: 'Number of Assets',
                data: [234, 156, 98, 45, 15],
                backgroundColor: [
                    'rgba(255, 159, 64, 0.8)',
                    'rgba(199, 199, 199, 0.8)',
                    'rgba(83, 102, 255, 0.8)',
                    'rgba(78, 252, 3, 0.8)',
                    'rgba(255, 99, 132, 0.8)'
                ],
                borderColor: [
                    'rgba(255, 159, 64, 1)',
                    'rgba(199, 199, 199, 1)',
                    'rgba(83, 102, 255, 1)',
                    'rgba(78, 252, 3, 1)',
                    'rgba(255, 99, 132, 1)'
                ],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Number of Assets'
                    }
                }
            }
        }
    });

    // ADCs Chart
    const adcsCtx = document.getElementById('adcsChart').getContext('2d');
    new Chart(adcsCtx, {
        type: 'bar',
        data: {
            labels: ['Preclinical', 'Phase I', 'Phase II', 'Phase III', 'Approved'],
            datasets: [{
                label: 'Number of Assets',
                data: [189, 112, 76, 34, 11],
                backgroundColor: [
                    'rgba(255, 206, 86, 0.8)',
                    'rgba(54, 162, 235, 0.8)',
                    'rgba(255, 99, 132, 0.8)',
                    'rgba(75, 192, 192, 0.8)',
                    'rgba(153, 102, 255, 0.8)'
                ],
                borderColor: [
                    'rgba(255, 206, 86, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 99, 132, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)'
                ],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Number of Assets'
                    }
                }
            }
        }
    });
}

// Add smooth scrolling and animations
document.addEventListener('DOMContentLoaded', function() {
    // Add animation to metric cards
    const metricCards = document.querySelectorAll('.metric-card');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    });

    metricCards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(card);
    });

    // Add hover effects to news items
    const newsItems = document.querySelectorAll('.news-item');
    newsItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.transform = 'translateX(5px)';
            this.style.transition = 'transform 0.3s ease';
        });
        
        item.addEventListener('mouseleave', function() {
            this.style.transform = 'translateX(0)';
        });
    });
});

// Add export functionality (placeholder for future enhancement)
function exportDashboard() {
    // This could be implemented to export dashboard data to PDF or Excel
    console.log('Export functionality would be implemented here');
}

// Add real-time data update simulation (placeholder)
function updateData() {
    // This could be implemented to fetch real-time data from APIs
    console.log('Real-time data update would be implemented here');
}
