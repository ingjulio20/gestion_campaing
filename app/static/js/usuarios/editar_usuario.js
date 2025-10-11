/* Constantes */
const doc_usuario = document.getElementById("doc_usuario");
const nombre_completo = document.getElementById("nombre_completo");
const usuario = document.getElementById("usuario");
const password = document.getElementById("password");
const perfil = document.getElementById("perfil");
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
            window.location.href = "/usuarios"
        }
    });
});

/* Validar Formulario */
const formUpdateUsuario = document.getElementById("formUpdateUsuario");
formUpdateUsuario.addEventListener("submit", (e) => {
    let docUsuario = doc_usuario.value;
    let nombreCompleto = nombre_completo.value;
    let user = usuario.value;
    let pass = password.value;
    let perfilUsuario = perfil.value;
    if(!docUsuario || !nombreCompleto || !user || !pass || !perfilUsuario){
        e.preventDefault();
        Swal.fire({
            title: "Advertencia!",
            text: "Todos los campos con (*) son obligatorios",
            icon: "warning"
        });
        return;
    };

    /* Loading */
    Swal.fire({
        allowOutsideClick: false,
        allowEscapeKey: false,
        showConfirmButton: false,
        didOpen: () => {
            Swal.showLoading();
        }
    });
});