/* Constantes Globales */
const formUpdateNicho = document.getElementById("formUpdateNicho");
const cod_nicho = document.getElementById("cod_nicho");
const nom_nicho = document.getElementById("nom_nicho");
const btn_cancelar = document.getElementById("btn_cancelar");

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
            window.location.href = "/nichos"
        }
    });
});

/* Loading */
formUpdateNicho.addEventListener("submit", (e) => {
    Swal.fire({
        allowOutsideClick: false,
        allowEscapeKey: false,
        showConfirmButton: false,
        didOpen: () => Swal.showLoading()
    })
})