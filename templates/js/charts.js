// Bar Chart for Realized vs Unrealized Profit
var ctxCustomBar = document.getElementById("customBarChart").getContext('2d');
var customBarChart = new Chart(ctxCustomBar, {
    type: 'bar',
    data: {
        labels: ["Realized Profit", "Unrealized Profit"],
        datasets: [{
            label: 'Profit in USD',
            data: [50000, 30000], // Update these values as needed
            backgroundColor: [
                'rgba(54, 162, 235, 0.6)',  // Realized Profit color
                'rgba(75, 192, 192, 0.6)'   // Unrealized Profit color
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)',
                'rgba(75, 192, 192, 1)'
            ],
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

// Pie Chart for Percentage Distribution in Cash
var ctxCustomPie = document.getElementById("customPieChart").getContext('2d');
var customPieChart = new Chart(ctxCustomPie, {
    type: 'pie',
    data: {
        labels: ["Savings", "Investments", "Emergency Fund"],
        datasets: [{
            data: [40, 35, 25], // Update these values as needed (in percentages)
            backgroundColor: [
                'rgba(54, 162, 235, 0.6)',  // Savings color
                'rgba(255, 99, 132, 0.6)',  // Investments color
                'rgba(255, 205, 86, 0.6)'   // Emergency Fund color
            ],
            hoverOffset: 4
        }]
    },
    options: {
        responsive: true,
    }
});




