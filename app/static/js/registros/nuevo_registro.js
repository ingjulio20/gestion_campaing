/* Constantes */
const depto = document.getElementById("depto");
const nom_depto = document.getElementById("nom_depto");
const municipio = document.getElementById("municipio");
const nom_municipio = document.getElementById("nom_municipio");

/* Obtener Departamentos Fetch */
/* const getDeptos = () => {
    depto.innerHTML = `<option value=""></option>`
    fetch("/getDeptos", {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        data.forEach(depto => {
            depto.innerHTML += `<option value="${depto.cod_depto}">${depto.nom_depto}</option>`
        });
    })
    .catch(error => console.error("error: ", error))
} */


/* Obtener Municipios Fetch */
const getMunicipios = () => {
    let codDepto = depto.value;
    municipio.innerHTML = `<option value=""></option>`
    fetch("/getMunicipios", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ "codDepto": codDepto })
    })
    .then(response => response.json())
    .then(data => {
        data.forEach(municipio => {
             municipio.innerHTML += `<option value="${municipio.cod_municipio}">${municipio.nom_municipio}</option>`
        });
    })
    .catch(error => console.error("error: ", error))
}

/* Obtener Nombre Departamento */
depto.addEventListener("change", (e) => {
    e.preventDefault();
    getMunicipios();
    nom_depto.value = depto.options[depto.selectedIndex].text;
})

/* Obtener Nombre de Municipio */
municipio.addEventListener("change", (e) => {
    e.preventDefault();
    nom_municipio.value = municipio.options[municipio.selectedIndex].text;
});