const ctx = document.getElementById('chartRegistros');
const datos = []
const chart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [{
            label: 'No. de Registros',
            data: [],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});


window.onload = () => {
    getRegistrosDepto();
}

const getRegistrosDepto = () => {
    fetch("/getRegistrosDepto", {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        const labels = [];
        const valores = [];
        
        data.forEach(registro => {
            labels.push(registro.depto)
            valores.push(Number(registro.numero))
            datos.push({numero: Number(registro.numero), depto:registro.depto})
        });

        // asignar al chart y actualizarlo
        chart.data.labels = labels;
        chart.data.datasets[0].data = valores;
        chart.update();
    })
    .catch(error => console.error("error: ", error))
}

