document.addEventListener("DOMContentLoaded", function() {
    // Bar Chart for Realized vs Unrealized Profit
    var ctxCustomBar = document.getElementById("customBarChart").getContext('2d');
    var barLabels = ctxCustomBar.canvas.dataset.labels.split(', ');
    var barValues = ctxCustomBar.canvas.dataset.values.split(', ').map(Number);

    var customBarChart = new Chart(ctxCustomBar, {
        type: 'bar',
        data: {
            labels: barLabels,
            datasets: [{
                label: 'Profit in USD',
                data: barValues,
                backgroundColor: barValues.map(value => value >= 0 ? 'rgba(54, 162, 235, 0.6)' : 'rgba(255, 99, 132, 0.6)'),
                borderColor: barValues.map(value => value >= 0 ? 'rgba(54, 162, 235, 1)' : 'rgba(255, 99, 132, 1)'),
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    suggestedMin: Math.min(...barValues) < 0 ? Math.min(...barValues) - 10 : 0
                }
            }
        }
    });

    // Pie Chart for Percentage Distribution in Cash
    var ctxCustomPie = document.getElementById("customPieChart").getContext('2d');
    var pieLabels = ctxCustomPie.canvas.dataset.labels.split(', ');
    var pieValues = ctxCustomPie.canvas.dataset.values.split(', ').map(Number);

    var customPieChart = new Chart(ctxCustomPie, {
        type: 'pie',
        data: {
            labels: pieLabels,
            datasets: [{
                data: pieValues,
                backgroundColor: pieLabels.map((label, index) => {
                    // Generate colors dynamically for each slice
                    var colors = [
                        'rgba(54, 162, 235, 0.6)',
                        'rgba(255, 99, 132, 0.6)',
                        'rgba(255, 205, 86, 0.6)',
                        'rgba(75, 192, 192, 0.6)',
                        'rgba(153, 102, 255, 0.6)',
                        'rgba(255, 159, 64, 0.6)'
                    ];
                    return colors[index % colors.length]; // Cycle through colors if more labels than colors
                }),
                hoverOffset: 4
            }]
        },
        options: {
            responsive: true,
        }
    });
});
