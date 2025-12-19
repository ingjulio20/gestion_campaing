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
      };

      data.forEach(registro => {
        tablaRegistros.insertRow().innerHTML = `
          <td style="font-size: small; width: 5%;">${registro.ID}</td>
          <td style="font-size: small; width: 10%;">${registro.nuip}</td>
          <td style="font-size: small; width: 20%;">${registro.votante}</td>
          <td style="font-size: small; width: 20%;">${registro.camp}</td>
          <td style="font-size: small; width: 20%;">${registro.funcionario}</td>
          <td style="font-size: small; width: 5%;">${registro.user_funcionario}</td>
          <td style="font-size: small; width: 5%;">${registro.nicho}</td>
          <td style="font-size: small; width: 5%;">${registro.voto}</td>
          <td style="font-size: small; width: 10%;">
            <a href="/editar_registro/${registro.ID}" class="button is-small is-info has-tooltip-bottom" data-tooltip="Editar" style="padding: 0em 1.0em;">
                <span class="icon is-small"><i aria-hidden="true"><img src="./static/img/icons/editar.png" alt="icon-editar"></i></span>
            </a>
            <a onclick="activarModalCargueCert(${registro.ID}, '${registro.nuip}', '${registro.votante}')" class="link_cert button is-small is-info has-tooltip-bottom" data-tooltip="Confirmar Voto y Cargar Cert. Electoral" style="padding: 0em 1.0em;">
                <span class="icon is-small"><i aria-hidden="true"><img src="./static/img/icons/voto.png" alt="icon-voto"></i></span>
            </a>
            <a onclick="activarModalVerCert('${registro.base64}')" class="link_ver_cert button is-small is-info has-tooltip-bottom" data-tooltip="Ver Certificado" style="padding: 0em 1.0em;">
                <span class="icon is-small"><i aria-hidden="true"><img src="./static/img/icons/vista.png" alt="icon-vista"></i></span>
            </a>
          </td>
        `;
      });
      desactivarEnlaces();
  })
  .catch(error => console.error("error: ", error))
}

btn_buscar.addEventListener("click", (e) => {
  e.preventDefault();
  getRegistrosNuip();
});

/* Activar Modal Cargue Certificado */
const modalCargueCertificado = document.getElementById("modalCargueCertificado");
const id_registro = document.getElementById("id_registro");
const nuip_registro = document.getElementById("nuip_registro");
const nombre_registro = document.getElementById("nombre_registro");
const btn_modal_cancelar_cert = document.getElementById("btn_modal_cancelar_cert");
const activarModalCargueCert = (id, nuip, nombre) => {
  modalCargueCertificado.classList.remove('is-hidden');
  modalCargueCertificado.classList.add('is-active');

  /* Cargar Datos  */
  id_registro.value = id
  nuip_registro.value = nuip
  nombre_registro.value = nombre
}

/* Cerrar Modal */
btn_modal_cancelar_cert.addEventListener("click", (e) => {
  e.preventDefault();
  modalCargueCertificado.classList.remove('is-active');
})

/* Cargue de PDF */
const fileInputCert = document.querySelector("#file-certificado input[type=file]");
fileInputCert.onchange = () => {
  if (fileInputCert.files.length > 0) {
    const fileName = document.querySelector("#file-certificado .file-name");
    fileName.textContent = fileInputCert.files[0].name;
  }

  /* Validar tamaño del pdf */
  if(fileInputCert.files[0].size > 1048576){
    Swal.fire({
      title: "Advertencia!",
      text: "el archivo excede el tamaño permitido (1 MB).",
      icon: "warning"
    });
    const fileName = document.querySelector("#file-certificado .file-name");
    fileName.textContent = "No hay PDF cargado";
    return;
  }
};

/* Validar Formulario Modal Cargue Cert */
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

/* Activar Modal Cargue Masivo Registros */
const modalCargueRegistrosMasivos = document.getElementById("modalCargueRegistrosMasivos");
const btn_activarModalCargueRegistros = document.getElementById("btn_activarModalCargueRegistros");
const btn_modal_cancelar_reg = document.getElementById("btn_modal_cancelar_reg");
const activarModalCargueRegistros = () => {
  modalCargueRegistrosMasivos.classList.remove('is-hidden');
  modalCargueRegistrosMasivos.classList.add('is-active');
}

/* Activar Modal Registros Masivos */
btn_activarModalCargueRegistros.addEventListener("click", (e) => {
  e.preventDefault();
  activarModalCargueRegistros();
})

/* Cargue de CSV */
const fileInputRegistros = document.querySelector("#file-registros input[type=file]");
fileInputRegistros.onchange = () => {
  if (fileInputRegistros.files.length > 0) {
    const fileName = document.querySelector("#file-registros .file-name");
    fileName.textContent = fileInputRegistros.files[0].name;
  }
};

/* Cerrar Modal Registros Masivos */
btn_modal_cancelar_reg.addEventListener("click", (e) => {
  e.preventDefault();
  modalCargueRegistrosMasivos.classList.remove('is-active');
})

/* Validar Formulario Modal Cargue Masivo Registros */
const formCargueRegistrosMasivos = document.getElementById("formCargueRegistrosMasivos");
formCargueRegistrosMasivos.addEventListener("submit", (e) => {
  /* Loading */
  Swal.fire({
    allowOutsideClick: false,
    allowEscapeKey: false,
    showConfirmButton: false,
    didOpen: () => Swal.showLoading()
  })
});

/* Activar Modal ver Certificados */
const modalVerCertificado = document.getElementById("modalVerCertificado");
const btn_cerrarModalVerCert = document.getElementById("btn_cerrarModalVerCert");
const iframeCert = document.getElementById("iframeCert");
const activarModalVerCert = (base64) => {
  modalVerCertificado.classList.remove("is-hidden");
  modalVerCertificado.classList.add("is-active");
  

  // 1. Decodificar la cadena Base64
    const byteCharacters = atob(base64);
    
    // 2. Crear un array de bytes
    const byteNumbers = new Array(byteCharacters.length);
    for (let i = 0; i < byteCharacters.length; i++) {
        byteNumbers[i] = byteCharacters.charCodeAt(i);
    }
    
    // 3. Convertir a Uint8Array
    const byteArray = new Uint8Array(byteNumbers);
    
    // 4. Crear el objeto Blob (Binary Large Object)
    const blob = new Blob([byteArray], { type: 'application/pdf' });
    
    // 5. Crear una URL interna temporal que apunta a ese Blob
    const blobUrl = URL.createObjectURL(blob);
    iframeCert.src = blobUrl;
}

btn_cerrarModalVerCert.addEventListener("click", (e) => {
  e.preventDefault();
  modalVerCertificado.classList.remove("is-active");

  // Liberar la URL para ahorrar memoria y limpiar el iframe
    if (iframeCert.src.startsWith('blob:')) {
        URL.revokeObjectURL(iframeCert.src);
        iframeCert.src = ""; 
    }
})

/* Activar y Desactivar Botones */
const desactivarEnlaces = () => {
  let filas = document.querySelectorAll("#tablaRegistros tr");
  filas.forEach(fila => {
      const valor_voto = fila.cells[7].innerText.trim();
      /* Desactivar Cargar Certificado */
      if(valor_voto === "SÍ"){
        const link_cert = fila.querySelector(".link_cert");
        if(link_cert){
          link_cert.classList.add("enlace-desactivado");
          link_cert.removeAttribute("onclick");
        }  
      };
      /* Desactivar Ver Certificado */
      if(valor_voto === "NO"){
        const link_ver_cert = fila.querySelector(".link_ver_cert");
        if(link_ver_cert){
          link_ver_cert.classList.add("enlace-desactivado");
          link_ver_cert.removeAttribute("onclick");
        }
      };
  });
};