from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.services import documentos_service, deptos_service, etnias_service, registros_service
import mysql.connector.errors as error

#Blueprint
bp_registros = Blueprint('registros', __name__)

#Rutas
@bp_registros.get('/registros')
def registros():
    registros = registros_service.list_registros()
    return render_template('tmp_registros/registros.html', registros = registros)

@bp_registros.get('/nuevo_registro')
def nuevo_registro():
    tipos = documentos_service.list_tipoDocumentos()
    deptos = deptos_service.list_departamentos()
    etnias = etnias_service.list_etnias()
    return render_template('tmp_registros/nuevo_registro.html', tipos = tipos, deptos = deptos, etnias = etnias)

@bp_registros.post('/add_registro')
def add_registro():
    try:
        tipo_documento = request.form["tipo_documento"]
        nuip = request.form["nuip"]
        nombre_completo = request.form["nombre_completo"]
        fecha_nacimiento = request.form["fecha_nacimiento"]
        direccion = request.form["direccion"]
        telefono = request.form["telefono"]
        email = request.form["email"]
        depto = request.form["depto"]
        nom_depto = request.form["nom_depto"]
        municipio = request.form["municipio"]
        nom_municipio = request.form["nom_municipio"]
        sexo = request.form["sexo"]
        etnia = request.form["etnia"]
        usuario_registro = request.form["usuario_registro"]

        registros_service.insert_registro(tipo_documento, nuip, nombre_completo, fecha_nacimiento, direccion, telefono,
                                          email, depto, nom_depto, municipio, nom_municipio, sexo, etnia, usuario_registro)
        
        flash("Registro Guardado Exitosamente!", "success")
        return redirect(url_for('registros.registros'))
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('registros.registros'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('registros.registros'))

@bp_registros.get('/editar_registro/<int:id>')
def editar_registro(id):
    registro = registros_service.list_registro_id(id)
    tipos = documentos_service.list_tipoDocumentos()
    deptos = deptos_service.list_departamentos()
    etnias = etnias_service.list_etnias()
    return render_template('tmp_registros/editar_registro.html', registro = registro, tipos = tipos, deptos = deptos, etnias = etnias)

@bp_registros.post('/update_registro')
def update_registro():
    try:
        tipo_documento = request.form["tipo_documento"]
        nuip = request.form["nuip"]
        nombre_completo = request.form["nombre_completo"]
        fecha_nacimiento = request.form["fecha_nacimiento"]
        direccion = request.form["direccion"]
        telefono = request.form["telefono"]
        email = request.form["email"]
        depto = request.form["depto"]
        nom_depto = request.form["nom_depto"]
        municipio = request.form["municipio"]
        nom_municipio = request.form["nom_municipio"]
        sexo = request.form["sexo"]
        etnia = request.form["etnia"]
        id_registro = request.form["id_registro"]

        registros_service.update_registro(tipo_documento, nuip, nombre_completo, fecha_nacimiento, direccion, telefono,
                                          email, depto, nom_depto, municipio, nom_municipio, sexo, etnia, id_registro)
        
        flash("Datos de Registro Actualizados Exitosamente", "success")
        return redirect(url_for('registros.registros'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('registros.registros'))

    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('registros.registros'))
 
@bp_registros.get('/getRegistrosDepto')
def getRegistrosDepto():
    try:
        registros_depto = registros_service.count_registros_x_depto()
        if registros_depto:
            return jsonify(registros_depto)

    except Exception as ex:
        return jsonify(ex)        