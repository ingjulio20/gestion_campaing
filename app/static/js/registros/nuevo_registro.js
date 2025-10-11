/* Obtener Nombre de Departamento */
const depto = document.getElementById("depto");
const nom_depto = document.getElementById("nom_depto");

depto.addEventListener("change", (e) => {
    e.preventDefault();
    nom_depto.value = depto.options[depto.selectedIndex].text;
})