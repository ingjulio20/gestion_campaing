/* Constantes Globales */
const select_camp = document.getElementById("select_camp");
const printDashboard = document.getElementById("printDashboard");
const registrosCamp = document.getElementById("registrosCamp");
const registrosVotoPositivo = document.getElementById("registrosVotoPositivo");
const tablaMetas = document.getElementById("tablaMetas");

/* Imprimir DashBoard */
printDashboard.addEventListener("click", (e) => {
    e.preventDefault();
    window.print()
})


/* Fetch Obtener Datos de Campaña */
const getDatosCamp = () => {
    let id_camp = select_camp.value;
    while (tablaMetas.rows.length > 1 ) {
        tablaMetas.deleteRow(1);
    }
    fetch("/getDatosCamp", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ id_camp })
    })
    .then(response => response.json())
    .then(data => {
    
        tablaMetas.insertRow().innerHTML = `
                <td>${data[2]}</td>
                <td>${data[3]}</td>
            ` 
    })
    .catch(error => console.error("error: ", error))
}

/* Fetch Obtener Registros x Campaña */
const getRegistrosCamp = () => {
    let id_camp = select_camp.value;
    registrosCamp.innerHTML = ``
    fetch("/getRegistrosCamp", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ id_camp })
    })
    .then(response => response.json())
    .then(data => {
         registrosCamp.innerHTML = data[0]
    })
    .catch(error => console.error("error: ", error))
}

/* Fetch Obtener Registros con voto positivo x Campaña */
const getRegistrosVotosConfirmados = () => {
    let id_camp = select_camp.value;
    registrosVotoPositivo.innerHTML = ``
    fetch("/getRegistrosVotosConfirmados", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ id_camp })
    })
    .then(response => response.json())
    .then(data => {
         registrosVotoPositivo.innerHTML = data[0]
    })
    .catch(error => console.error("error: ", error))
}

/* Graficos */
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

const getRegistrosDepto = () => {
    let id_camp = select_camp.value;
    fetch("/getRegistrosDepto", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ id_camp })
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

select_camp.addEventListener("change", (e) => {
    e.preventDefault();
    getDatosCamp();
    getRegistrosCamp();
    getRegistrosVotosConfirmados();
    getRegistrosDepto();
})