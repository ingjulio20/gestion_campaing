from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.services import funcionarios_services
import mysql.connector.errors as error

bp_funcionarios = Blueprint('funcionarios', __name__)

#Ruta Ventana Principal Funcionarios
@bp_funcionarios.get('/funcionarios')
def funcionarios():
    return render_template('tmp_funcionarios/funcionarios.html')

#Ruta Ventana Nuevo Funcionario
@bp_funcionarios.get('/nuevo_funcionario')
def nuevo_funcionario():
    roles = funcionarios_services.list_roles_funcionarios()
    return render_template('tmp_funcionarios/nuevo_funcionario.html', roles = roles)

#Ruta AJAX Obtener Funcionarios Administradores
@bp_funcionarios.get('/getFuncionariosAdmin')
def getFuncionariosAdmin():
    try:
        funcionarios = funcionarios_services.list_funcionarios_admin()
        if funcionarios:
            return jsonify(funcionarios)
        else:
            return jsonify({"Error": "No se encontraron funcionarios."})
        
    except error.Error as e:
        return jsonify({"Error": f"{e.msg}"})

    except Exception as ex:
        return jsonify({"Error": f"{ex}"})
    
#Ruta AJAX Obtener Funcionarios Enlace
@bp_funcionarios.get('/getFuncionariosEnlace')
def getFuncionariosEnlace():
    try:
        funcionarios = funcionarios_services.list_funcionarios_enlace()
        if funcionarios:
            return jsonify(funcionarios)
        else:
            return jsonify({"Error": "No se encontraron funcionarios."})
        
    except error.Error as e:
        return jsonify({"Error": f"{e.msg}"})

    except Exception as ex:
        return jsonify({"Error": f"{ex}"})    

#Ruta Metodo Nuevo Funcionario en BD
@bp_funcionarios.post('/add_funcionario')
def add_funcionario():
    try: 
        nuip_funcionario = request.form["nuip_funcionario"]
        nom_funcionario = request.form["nom_funcionario"]
        dir_funcionario = request.form["dir_funcionario"]
        tel_funcionario = request.form["tel_funcionario"]
        rol_funcionario = request.form["rol_funcionario"]
        admin_asociado = request.form["admin_asociado"]
        enlace_asociado = request.form["enlace_asociado"]

        funcionarios_services.insert_funcionario(nuip_funcionario, nom_funcionario, dir_funcionario, tel_funcionario, rol_funcionario,
                                                 admin_asociado, enlace_asociado)
        
        flash("Funcionario Registrado Exitosamente.", "success")
        return redirect(url_for('funcionarios.funcionarios'))
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('funcionarios.funcionarios'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('funcionarios.funcionarios'))

#Ruta AJAX Obtener Funcionarios por Nombre
@bp_funcionarios.post('/getFuncionarios')
def getFuncionarios():
    try:
        data = request.get_json()
        nombre = data.get("nombre")
        funcionarios = funcionarios_services.list_funcionarios(nombre)
        if funcionarios:
            return jsonify(funcionarios)
        else:
            return jsonify({"Error": "No se encontraron funcionarios."})
    
    except error.Error as e:
        return jsonify({"Error": f"{e.msg}"})
    
    except Exception as ex:
        return jsonify({"Error": f"{ex}"})

#Ruta Ventana Editar Funcionario
@bp_funcionarios.get('/editar_funcionario/<int:id>')
def editar_funcionario(id):
    funcionario = funcionarios_services.list_funcionario_id(id)
    roles = funcionarios_services.list_roles_funcionarios()
    return render_template('tmp_funcionarios/editar_funcionario.html', funcionario = funcionario, roles = roles)

#Ruta Metodo Editar Funcionario en BD
@bp_funcionarios.post('/update_funcionario')
def update_funcionario():
    try:
        nuip_funcionario = request.form["nuip_funcionario"]
        nom_funcionario = request.form["nom_funcionario"]
        dir_funcionario = request.form["dir_funcionario"]
        tel_funcionario = request.form["tel_funcionario"]
        rol_funcionario = request.form["rol_funcionario"]
        admin_asociado = request.form["admin_asociado"]
        enlace_asociado = request.form["enlace_asociado"]
        id_funcionario = request.form["id_funcionario"]

        funcionarios_services.update_funcionario(nuip_funcionario, nom_funcionario, dir_funcionario, tel_funcionario, rol_funcionario, 
                                                 admin_asociado, enlace_asociado, id_funcionario)
        
        flash("Datos de Funcionario Modificados Exitosamente.", "success")
        return redirect(url_for('funcionarios.funcionarios'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('funcionarios.funcionarios'))

    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('funcionarios.funcionarios'))

#Ruta Metodo para Eliminar Funcionario de BD
@bp_funcionarios.get('/delete_funcionario/<int:id>')
def delete_funcionario(id):
    try:
        funcionarios_services.delete_funcionario(id)
        flash("Funcionario Eliminado Exitosamente.", "success")
        return redirect(url_for('funcionarios.funcionarios'))
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('funcionarios.funcionarios'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('funcionarios.funcionarios'))
