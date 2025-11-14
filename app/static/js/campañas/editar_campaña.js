/* Constantes Globales */
const formUpdateCampaña = document.getElementById("formUpdateCampaña");
const id_camp = document.getElementById("id_camp");
const nom_camp = document.getElementById("nom_camp");
const meta_votantes = document.getElementById("meta_votantes");
const meta_votos = document.getElementById("meta_votos");
const btn_cancelar = document.getElementById("btn_cancelar");

/* UpperCase */
nom_camp.addEventListener("keyup", () => {
    nom_camp.value = nom_camp.value.toUpperCase();
});

/* Cancelar */
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
            window.location.href = "/campañas"
        }
    });
});

/* Validar Formulario */
formUpdateCampaña.addEventListener("submit", (e) => {
    /* Variables */
    let nomCamp = nom_camp.value;
    let metaVotantes = meta_votantes.value;
    let metaVotos = meta_votos.value;
    if(!nomCamp || !metaVotantes || !metaVotos){
        e.preventDefault();
        Swal.fire({
            title: "Advertencia!",
            text: "Debe diligenciar todos los campos obligatorios (*).",
            icon: "warning"
        });
        return;
    }

    /* Loading */
    Swal.fire({
        allowOutsideClick: false,
        allowEscapeKey: false,
        showConfirmButton: false,
        didOpen: () => Swal.showLoading()
    });
});