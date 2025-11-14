/* Constantes */
const doc_usuario = document.getElementById("doc_usuario");
const nombre_completo = document.getElementById("nombre_completo");
const usuario = document.getElementById("usuario");
const password = document.getElementById("password");
const perfil = document.getElementById("perfil");
const btn_cancelar = document.getElementById("btn_cancelar");

/* UpperCase */
nombre_completo.addEventListener("keyup", () => {
    nombre_completo.value = nombre_completo.value.toUpperCase();
});

/* DataTable */
const tablaBusquedaFuncionarios = document.getElementById("tablaBusquedaFuncionarios");
let tableBusquedaFuncionarios = new DataTable('#tablaBusquedaFuncionarios', {
  language: {
    lengthMenu: "Mostrar _MENU_ registros por pagina",
    zeroRecords: "Sin registros encontrados",
    info: "Mostrando pagina _PAGE_ de _PAGES_",
    infoEmpty: "No hay registros disponibles",
    infoFiltered: "(filtrado de _MAX_ registros)",
    search: "Filtrar:",
    paginate: {
      first: "Primera",
      last: "Última",
      next: "Siguiente",
      previous: "Anterior"
    }
  }
});

tablaBusquedaFuncionarios.addEventListener("click", (e) => {
    e.preventDefault();
    let data = e.target.parentElement.children;
    doc_usuario.value = data[0].innerText;
    nombre_completo.value = data[1].innerText;
    closeAllModals();
});

/* Cerrar Modal */
function closeModal($el) {
    $el.classList.remove('is-active');
}

function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
        closeModal($modal);
    });
}

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
const formAddUsuario = document.getElementById("formAddUsuario");
formAddUsuario.addEventListener("submit", (e) => {
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