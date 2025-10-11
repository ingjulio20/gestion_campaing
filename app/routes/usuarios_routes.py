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
    usu = usuarios_service.listar_usuarios()
    return render_template('tmp_usuarios/usuarios.html', usu = usu)

@bp_usuarios.get('/nuevo_usuario')
def nuevo_usuario():
    perfil = usuarios_service.listar_perfiles_usuario()
    return render_template('tmp_usuarios/nuevo_usuario.html', perfil = perfil)

@bp_usuarios.post('/add_usuario')
def add_usuario():
    try:
        doc_usuario = request.form["doc_usuario"]
        nombre_completo = request.form["nombre_completo"]
        usuario = request.form["usuario"]
        password = bcrypt.generate_password_hash(request.form["password"])
        perfil = request.form["perfil"]

        usuarios_service.insert_usuario(doc_usuario,nombre_completo, usuario, password, perfil)
        flash("Usuario Creado Exitosamente", "success")
        return redirect(url_for('usuarios.usuarios'))
        
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('usuarios.usuarios'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('usuarios.usuarios'))

@bp_usuarios.route('/drop_Usuario/<usuario>')
def drop_usuario(usuario):
    try:
        usuarios_service.delete_usuario(usuario)
        flash("Usuario Eliminado Exitosamente", "success")
        return redirect(url_for('usuarios.usuarios'))
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('usuarios.usuarios'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('usuarios.usuarios'))
    
@bp_usuarios.get('/edit_usuario/<usuario>')
def edit_usuario(usuario):
    try:
        usu = usuarios_service.listar_usuario_nombre(usuario)
        perfil = usuarios_service.listar_perfiles_usuario()
        return render_template('temp_usuarios/edit_usuario.html', usu = usu , perfil = perfil)

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('usuarios.usuarios'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('usuarios.usuarios'))

@bp_usuarios.post('/f_updateUsuario')
def f_updateUsuario():
    try:
        doc_usuario = request.form["doc_usuario"]
        nombre_completo = request.form["nombre_completo"]
        usuario = request.form["usuario"]
        password = bcrypt.generate_password_hash(request.form["password"])
        perfil = request.form["perfil"]

        usuarios_service.update_usuario(doc_usuario,nombre_completo, usuario, password, perfil)
        flash("Usuario Actualizado Exitosamente", "success")
        return redirect(url_for('usuarios.usuarios'))
        
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('usuarios.usuarios'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('usuarios.usuarios'))    