from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_bcrypt import Bcrypt
import mysql.connector.errors as error

#Blueprint
bp_usuarios = Blueprint('usuarios', __name__)
bcrypt = Bcrypt()

#Rutas
@bp_usuarios.get('/usuarios')
def usuarios():
    return render_template('tmp_usuarios/usuarios.html')