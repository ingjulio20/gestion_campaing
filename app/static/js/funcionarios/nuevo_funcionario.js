/* Constantes Globales Inputs y Selects */
const formAddFuncionario = document.getElementById("formAddFuncionario");
const nuip_funcionario = document.getElementById("nuip_funcionario");
const nom_funcionario = document.getElementById("nom_funcionario");
const dir_funcionario = document.getElementById("dir_funcionario");
const tel_funcionario = document.getElementById("tel_funcionario");
const rol_funcionario = document.getElementById("rol_funcionario");
const admin_asociado = document.getElementById("admin_asociado");
const enlace_asociado = document.getElementById("enlace_asociado");

/* Constantes Paneles y Botones */
const panelAdminAsociado = document.getElementById("panelAdminAsociado");
const panelEnlaceAsociado = document.getElementById("panelEnlaceAsociado");
const btn_cancelar = document.getElementById("btn_cancelar");

/* UpperCase */
nom_funcionario.addEventListener("keyup", () => {
    nom_funcionario.value = nom_funcionario.value.toUpperCase();
});

dir_funcionario.addEventListener("keyup", () => {
    dir_funcionario.value = dir_funcionario.value.toUpperCase();
});

/* Habilitar Paneles */
const habilitarPaneles = () => {
    let valor = rol_funcionario.value;
    if(valor === "2"){
        panelAdminAsociado.classList.remove('is-hidden');
        panelEnlaceAsociado.classList.add('is-hidden');
        admin_asociado.required = true;
        enlace_asociado.required = false;
        getFuncionariosAdmin();
    }else if(valor === "3"){
        panelAdminAsociado.classList.add('is-hidden');
        panelEnlaceAsociado.classList.remove('is-hidden');
        admin_asociado.required = false;
        enlace_asociado.required = true;
        getFuncionariosEnlace();
    }else if(valor === "1"){
        panelAdminAsociado.classList.add('is-hidden');
        panelEnlaceAsociado.classList.add('is-hidden');
        admin_asociado.required = false;
        enlace_asociado.required = false;
    }
};
rol_funcionario.addEventListener("change", habilitarPaneles);

/* Fetch Obtener los Funcionarios Admin */
const getFuncionariosAdmin = () => {
    let rol = rol_funcionario.value;
    admin_asociado.innerHTML = `<option value=""></option>`
    fetch("/getFuncionariosAdmin", {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        data.forEach(funcionario => {
            /* Datos para select administrador */
            admin_asociado.innerHTML += `<option value="${funcionario.documento}">${funcionario.nombre}</option>`;
        });
    })
    .catch(error => console.error("error: ", error))
}

/* Fetch Obtener los Funcionarios Enlace */
const getFuncionariosEnlace = () => {
    let rol = rol_funcionario.value;
    enlace_asociado.innerHTML = `<option value=""></option>`
    fetch("/getFuncionariosEnlace", {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        data.forEach(funcionario => {
            /* Datos para select Enlace */
            enlace_asociado.innerHTML += `<option value="${funcionario.documento}">${funcionario.nombre}</option>`;
        });
    })
    .catch(error => console.error("error: ", error))
}

/* Modo Cancelar */
btn_cancelar.addEventListener("click", (e) => {
    e.preventDefault();
    Swal.fire({
        title: "Estas Seguro(a)?",
        text: "Los cambios no se guardaran.",
        icon: "question",
        confirmButtonText: "Si, Cancelar!",
        confirmButtonColor: "#48c78e",
        cancelButtonText: "No, Continuar",
        cancelButtonColor: "#f14668",
        showCancelButton: true,
        allowOutsideClick: false
    })
    .then((result) => {
        if(result.isConfirmed){
            window.location.href = "/funcionarios"
        }
    });
});

/* Validar Formulario */
formAddFuncionario.addEventListener("submit", (e) => {
    /* Variables */
    let nuipFuncionario = nuip_funcionario.value;
    let nomFuncionario = nom_funcionario.value;
    let dirFuncionario = dir_funcionario.value;
    let telFuncionario = tel_funcionario.value;
    let rolFuncionario = rol_funcionario.value;

    if(!nuipFuncionario || !nomFuncionario || !dirFuncionario || !telFuncionario || !rolFuncionario){
        e.preventDefault();
        Swal.fire({
            title: "Advertencia!",
            text: "Debe diligenciar todos los campos obligatorios (*).",
            icon: "warning"
        });
        return;
    }

    /* loading */
    Swal.fire({
        allowOutsideClick: false,
        allowEscapeKey: false,
        showConfirmButton: false,
        didOpen: () => Swal.showLoading()
    });
})