/* Constantes Globales */
const buscar_funcionario = document.getElementById("buscar_funcionario");
const btn_buscar = document.getElementById("btn_buscar");
const tablaFuncionarios = document.getElementById("tablaFuncionarios");

/* Uppercase */
buscar_funcionario.addEventListener("keyup", () => {
    buscar_funcionario.value = buscar_funcionario.value.toUpperCase();
});

/* Fetch Obtener Funcionarios por Nombre */
const getFuncionarios = () => {
    let nombre = buscar_funcionario.value;
    /* Limpiar la tabla */
    while (tablaFuncionarios.rows.length > 1) {
        tablaFuncionarios.deleteRow(1)
    }
    fetch("/getFuncionarios", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ nombre })
    })
    .then(response => response.json())
    .then(data => {
        if(!Array.isArray(data) || data.length === 0){
            Swal.fire({
                title: "Advertencia!",
                text: "No se encontraron datos relacionados.",
                icon: "warning",
                allowOutsideClick: false
            })
            return;
        }

        data.forEach(funcionario => {
            tablaFuncionarios.insertRow().innerHTML = `
            <td style="font-size: small; width: 5%;">${funcionario.ID}</td>
            <td style="font-size: small; width: 10%;">${funcionario.nuip}</td>
            <td style="font-size: small; width: 20%;">${funcionario.nombre}</td>
            <td style="font-size: small; width: 10%;">${funcionario.rol}</td>
            <td style="font-size: small; width: 20%;">${funcionario.administrador}</td>
            <td style="font-size: small; width: 20%;">${funcionario.enlace}</td>
            <td style="font-size: small; width: 10%;">
                <a href="/editar_funcionario/${funcionario.ID}" class="button is-small is-info has-tooltip-bottom" data-tooltip="Editar" style="padding: 0em 1.0em;">
                    <span class="icon is-small"><i aria-hidden="true"><img src="./static/img/icons/editar.png" alt="icon-editar"></i></span>
                </a>
                <a onclick="eliminarFuncionario(${funcionario.ID})" class="button is-small is-danger has-tooltip-bottom" data-tooltip="Eliminar" style="padding: 0em 1.0em;">
                    <span class="icon is-small"><i aria-hidden="true"><img src="./static/img/icons/basura.png" alt="icon-basura"></i></span>
                </a>
            </td>
            `
        });
    })
    .catch(error => console.error("error: ", error))
};

/* Eliminar */
const eliminarFuncionario = (id_funcionario) => {
    Swal.fire({
        title: "Estas Seguro(a)?",
        text: "Este proceso no se puede revertir.",
        icon: "question",
        confirmButtonText: "Si, Eliminar!",
        confirmButtonColor: "#48c78e",
        cancelButtonText: "No, Cancelar",
        cancelButtonColor: "#f14668",
        showCancelButton: true,
        allowOutsideClick: false
    })
    .then((result) => {
        if(result.isConfirmed){
            window.location.href = `/delete_funcionario/${id_funcionario}`
        }
    });
}

btn_buscar.addEventListener("click", (e) => {
    e.preventDefault();
    getFuncionarios();
})