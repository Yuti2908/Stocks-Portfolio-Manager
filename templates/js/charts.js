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

document.getElementById('sellButton').addEventListener('click', function() {
    const quantity = parseInt(document.getElementById('stockquantity').value, 10);
    const currentHolding = 100; // This value will be dynamic in the future

    if (isNaN(quantity) || quantity <= 0) {
        alert('Please enter a valid quantity.');
    } else if (quantity > currentHolding) {
        alert('Quantity exceeds current holding. Please enter a valid amount.');
    } else {
        // Quantity is valid and within the holding limit
        alert('Stock sold successfully!');
        // You can trigger the form submission or AJAX call here
    }
});


