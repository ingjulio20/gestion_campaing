/* Constantes */
const tipo_documento = document.getElementById("tipo_documento");
const nuip = document.getElementById("nuip");
const nombre_completo = document.getElementById("nombre_completo");
const fecha_nacimiento = document.getElementById("fecha_nacimiento");
const direccion = document.getElementById("direccion");
const telefono = document.getElementById("telefono");
const email = document.getElementById("email");
const depto = document.getElementById("depto");
const nom_depto = document.getElementById("nom_depto");
const municipio = document.getElementById("municipio");
const nom_municipio = document.getElementById("nom_municipio");
const sexo = document.getElementById("sexo");
const etnia = document.getElementById("etnia");
const puesto_votacion = document.getElementById("puesto_votacion");
const direccion_puesto = document.getElementById("direccion_puesto");
const mesa_votacion = document.getElementById("mesa_votacion");

/* Const Botones */
const copiar_nuip = document.getElementById("copiar_nuip");
copiar_nuip.addEventListener("click", (e) => {
    e.preventDefault();
    navigator.clipboard.writeText(nuip.value).then(() => {
        alert("Nro. Documento Copiado. Pegueló en los portales de consulta (BDUA, RNEC).");
    });
});

/* Upper Case */
nombre_completo.addEventListener("keyup", () => {
    nombre_completo.value = nombre_completo.value.toUpperCase();
});

direccion.addEventListener("keyup", () => {
    direccion.value = direccion.value.toUpperCase();
});

puesto_votacion.addEventListener("keyup", () => {
    puesto_votacion.value = puesto_votacion.value.toUpperCase();
});

direccion_puesto.addEventListener("keyup", () => {
    direccion_puesto.value = direccion_puesto.value.toUpperCase();
});

/* Obtener Nombre Departamento */
depto.addEventListener("change", () => {
    get_Municipios();
    nom_depto.value = depto.options[depto.selectedIndex].text;
})

/* Obtener Municipios Fetch */
const get_Municipios = () => {
    let codDepto = depto.value;
    municipio.innerHTML = `<option value=""></option>`
    fetch("/getMunicipios", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({"codDepto": codDepto})
    })
    .then(response => response.json())
    .then(data => {
        data.forEach(mun => {
            municipio.innerHTML += `<option value="${mun.cod_municipio}">${mun.nom_municipio}</option>`
        })
    })
    .catch(error => console.error("error: ", error))
}

/* Obtener Nombre de Municipio */
municipio.addEventListener("change", () => {
    nom_municipio.value = municipio.options[municipio.selectedIndex].text;
});

/* Modo Cancelar */
const btn_cancelar = document.getElementById("btn_cancelar");
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
            window.location.href = "/registros"
        }
    });
});

/* Validar Formulario */
const formAddRegistro = document.getElementById("formAddRegistro");
formAddRegistro.addEventListener("submit", (e) => {
    let regTipoDocumento = tipo_documento.value;
    let regNuip = nuip.value;
    let regNombreCompleto = nombre_completo.value;
    let regFechaNac = fecha_nacimiento.value;
    let regDireccion = direccion.value;
    let regTelefono = telefono.value;    
    let regEmail = email.value;
    let regDepto = depto.value;
    let regMunicipio = municipio.value;
    let regSexo = sexo.value;
    let regEtnia = etnia.value;
    let regPuestoVotacion = puesto_votacion.value;
    let regDirPuesto = direccion_puesto.value;
    let regMesaVotacion = mesa_votacion.value;

    if (!regTipoDocumento || !regNuip || !regNombreCompleto || !regFechaNac || !regDireccion || !regTelefono
        || !regEmail || !regDepto || !regMunicipio || !regSexo || !regEtnia || !regPuestoVotacion || !regDirPuesto || !regMesaVotacion
    ){
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

/* Ventanas Externas */
const popup_adres = document.getElementById("popup_adres");
const popup_registraduria = document.getElementById("popup_registraduria");

popup_adres.addEventListener("click", () => {
    window.open('https://servicios.adres.gov.co/BDUA/Consulta-Afiliados-BDUA', '_blank', 'width=600,height=600')
});

popup_registraduria.addEventListener("click", () => {
    window.open('https://wsp.registraduria.gov.co/censo/consultar/', '_blank', 'width=600,height=600')
});

/* const myPopup = new Popup({
    id: "my-popup",
    title: "My First Popup",
    content: () => {
        
    },
}); */