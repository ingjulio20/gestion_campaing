/* Constantes Globales */
const buscar_registro = document.getElementById("buscar_registro");
const btn_buscar = document.getElementById("btn_buscar");
const tablaRegistros = document.getElementById("tablaRegistros");

/* Fetch Obtener los registros por nuip */
const getRegistrosNuip = () => {
  let nuip = buscar_registro.value;
  /* Limpiar la tabla */
  while (tablaRegistros.rows.length > 1) {
    tablaRegistros.deleteRow(1);
  }
  fetch("/getRegistros", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ nuip })
  })
  .then(response => response.json())
  .then(data => {
    if(!Array.isArray(data) || data.length === 0){
        Swal.fire({
          title: "Advertencia!",
          text: "No se encontraron registros asociados.",
          icon: "warning",
          allowOutsideClick: false
        })
        return;
      }

      data.forEach(registro => {
        tablaRegistros.insertRow().innerHTML = `
          <td style="font-size: small; width: 5%;">${registro.ID}</td>
          <td style="font-size: small; width: 10%;">${registro.nuip}</td>
          <td style="font-size: small; width: 20%;">${registro.votante}</td>
          <td style="font-size: small; width: 20%;">${registro.camp}</td>
          <td style="font-size: small; width: 20%;">${registro.funcionario}</td>
          <td style="font-size: small; width: 10%;">${registro.user_funcionario}</td>
          <td style="font-size: small; width: 5%;">${registro.voto}</td>
          <td style="font-size: small; width: 10%;">
            <a href="/editar_registro/${registro.ID}" class="button is-small is-info has-tooltip-bottom" data-tooltip="Editar" style="padding: 0em 1.0em;">
                <span class="icon is-small"><i aria-hidden="true"><img src="./static/img/icons/editar.png" alt="icon-editar"></i></span>
            </a>
            <a onclick="activarModal(${registro.ID}, '${registro.nuip}', '${registro.votante}')" class="button is-small is-info has-tooltip-bottom" data-tooltip="Confirmar Voto y Cargar Cert. Electoral" style="padding: 0em 1.0em;">
                <span class="icon is-small"><i aria-hidden="true"><img src="./static/img/icons/voto.png" alt="icon-voto"></i></span>
            </a>
          </td>
        `
      });
  })
  .catch(error => console.error("error: ", error))
}

btn_buscar.addEventListener("click", (e) => {
  e.preventDefault();
  getRegistrosNuip();
});

/* Activar Modal */
const modalCargueCertificado = document.getElementById("modalCargueCertificado");
const id_registro = document.getElementById("id_registro");
const nuip_registro = document.getElementById("nuip_registro");
const nombre_registro = document.getElementById("nombre_registro");
const btn_modal_cancelar = document.getElementById("btn_modal_cancelar");
const activarModal = (id, nuip, nombre) => {
  modalCargueCertificado.classList.remove('is-hidden');
  modalCargueCertificado.classList.add('is-active');

  /* Cargar Datos  */
  id_registro.value = id
  nuip_registro.value = nuip
  nombre_registro.value = nombre
}

/* Cerrar Modal */
btn_modal_cancelar.addEventListener("click", (e) => {
  e.preventDefault();
  modalCargueCertificado.classList.remove('is-active');
})

/* Cargue de PDF */
const fileInput = document.querySelector("#file-certificado input[type=file]");
fileInput.onchange = () => {
  if (fileInput.files.length > 0) {
    const fileName = document.querySelector("#file-certificado .file-name");
    fileName.textContent = fileInput.files[0].name;
  }
};

/* Validar Formulario Modal Cargue */
const formCargueCertificado = document.getElementById("formCargueCertificado");
formCargueCertificado.addEventListener("submit", (e) => {
  /* Loading */
  Swal.fire({
    allowOutsideClick: false,
    allowEscapeKey: false,
    showConfirmButton: false,
    didOpen: () => Swal.showLoading()
  })
})