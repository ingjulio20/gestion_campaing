/* DataTable */
let tableUsuarios = new DataTable('#tablaUsuarios', {
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