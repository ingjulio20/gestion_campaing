/* Constantes Globales */
const profile = document.getElementById("profile");
const menu1 = document.getElementById("menu1");
const menu2 = document.getElementById("menu2");
const registrosLink = document.getElementById("registrosLink");

const verificarPerfil = () => {
    let perfil = profile.value;
    if(perfil === "1"){
        menu1.classList.remove('is-hidden');
        menu2.classList.remove('is-hidden');
        registrosLink.classList.remove('is-hidden');
    }else if(perfil === "2"){
        menu2.classList.remove('is-hidden');
        registrosLink.classList.remove('is-hidden');
    }else if(perfil === "3"){
        registrosLink.classList.remove('is-hidden');
    }
}

document.addEventListener("DOMContentLoaded", verificarPerfil);