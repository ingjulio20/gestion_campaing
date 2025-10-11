from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_bcrypt import Bcrypt
import mysql.connector.errors as error
from app.services import usuarios_service

#Blueprint
bp_usuarios = Blueprint('usuarios', __name__)
bcrypt = Bcrypt()

#Rutas
@bp_usuarios.get('/usuarios')
def usuarios():
    return render_template('tmp_usuarios/usuarios.html')

@bp_usuarios.get('/nuevo_usuario')
def nuevo_usuario():
    perfil = usuarios_service.listar_perfiles_usuario()
    return render_template('tmp_usuarios/nuevo_usuario.html', perfil = perfil)