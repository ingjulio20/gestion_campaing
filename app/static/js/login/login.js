/* Constantes */
const userId = document.getElementById("userId");
const userPass = document.getElementById("userPass");

/* Validar Formulario */
const formLoginAccess = document.getElementById("formLoginAccess");
formLoginAccess.addEventListener("submit", (e) => {
    let usuario = userId.value;
    let contraseña = userPass.value;
    if(!usuario || !contraseña){
        e.preventDefault();
        Swal.fire({
            title: "Notificación",
            text: "Debe diligenciar su usuario y/o contraseña.",
            icon: "info"
        });
        return;
    };

    /* Loading */
    Swal.fire({
        allowOutsideClick: false,
        allowEscapeClick: false,
        showConfirmButton: false,
        didOpen: () => {
            Swal.showLoading();
        }
    });
});