from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.services import documentos_service, deptos_service, etnias_service, campaña_service, nichos_service, registros_service
import mysql.connector.errors as error
import tempfile, os #Librerias para Cargue Masivo de Tuplas
from io import BytesIO
import base64

#Blueprint
bp_registros = Blueprint('registros', __name__)

#Rutas
@bp_registros.get('/registros')
def registros():
    return render_template('tmp_registros/registros.html', registros = registros)

#Ruta Ajax para Listas todos los registros por Documento
@bp_registros.post('/getRegistros')
def getRegistros():
    try: 
        data = request.get_json()
        nuip = data.get("nuip")
        registros = registros_service.list_registros_nuip(nuip)

        if registros:
            return jsonify(registros)
        else:
            return jsonify({"Error": "No se encontraron registros."})

    except error.Error as e:
        return jsonify({"Error": f"{e.msg}"})
    
    except Exception as ex:
        return jsonify({"Error": f"{ex}"})

#Ruta Ventana Nuevo Registro
@bp_registros.get('/nuevo_registro')
def nuevo_registro():
    tipos = documentos_service.list_tipoDocumentos()
    deptos = deptos_service.list_departamentos()
    etnias = etnias_service.list_etnias()
    camps = campaña_service.list_camp_electorales()
    nichos = nichos_service.list_nichos()
    return render_template('tmp_registros/nuevo_registro.html', tipos = tipos, deptos = deptos, etnias = etnias, camps = camps, nichos = nichos)

#Ruta Metodo Nuevo Registro
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
        puesto_votacion = request.form["puesto_votacion"]
        direccion_puesto = request.form["direccion_puesto"]
        mesa_votacion = request.form["mesa_votacion"]
        camp_asignada = request.form["camp_asignada"]
        nicho = request.form["nicho"]
        usuario_registro = request.form["usuario_registro"]

        registros_service.insert_registro(tipo_documento, nuip, nombre_completo, fecha_nacimiento, direccion, telefono,
                                          email, depto, nom_depto, municipio, nom_municipio, sexo, etnia, puesto_votacion,
                                          direccion_puesto, mesa_votacion, camp_asignada, nicho, usuario_registro)
        
        flash("Registro Guardado Exitosamente!", "success")
        return redirect(url_for('registros.registros'))
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('registros.registros'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('registros.registros'))

#Ruta para Insert/Cargue Masivo de Registros
@bp_registros.post('/uploadRegistrosMasivos')
def uploadRegistrosMasivos():
    try:
        registrosMasivos = request.files["registrosMasivos"]
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
        registrosMasivos.save(tmp.name)

        registros_service.insert_masivo_registros(tmp.name)
        flash("Registros Cargados Exitosamente", "success")
        return redirect(url_for('registros.registros'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('registros.registros'))

    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('registros.registros')) 

#Ruta Ventana Editar Registro
@bp_registros.get('/editar_registro/<int:id>')
def editar_registro(id):
    registro = registros_service.list_registro_id(id)
    tipos = documentos_service.list_tipoDocumentos()
    deptos = deptos_service.list_departamentos()
    etnias = etnias_service.list_etnias()
    camps = campaña_service.list_camp_electorales()
    nichos = nichos_service.list_nichos()
    return render_template('tmp_registros/editar_registro.html', registro = registro, tipos = tipos, deptos = deptos, etnias = etnias, camps = camps, nichos = nichos)

#Ruta Metodo Modificar datos de Registro
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
        puesto_votacion = request.form["puesto_votacion"]
        direccion_puesto = request.form["direccion_puesto"]
        mesa_votacion = request.form["mesa_votacion"]
        camp_asignada = request.form["camp_asignada"]
        nicho = request.form["nicho"]
        id_registro = request.form["id_registro"]

        registros_service.update_registro(tipo_documento, nuip, nombre_completo, fecha_nacimiento, direccion, telefono,
                                          email, depto, nom_depto, municipio, nom_municipio, sexo, etnia, 
                                          puesto_votacion, direccion_puesto, mesa_votacion, camp_asignada, nicho, id_registro)
        
        flash("Datos de Registro Actualizados Exitosamente", "success")
        return redirect(url_for('registros.registros'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('registros.registros'))

    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('registros.registros'))
    
#Ruta Metodo Actualizar Voto en Registro Simpatizante
@bp_registros.post('/update_registro_voto')
def update_registro_voto():
    try:
        voto_ejercido = request.form["voto_ejercido"]
        cert_voto = request.files["cert_voto"]
        id_registro = request.form["id_registro"]
        if cert_voto:
            certVoto_data = cert_voto.read()

        registros_service.update_voto_registro(voto_ejercido, certVoto_data, id_registro)
        flash("Voto Confirmado y Certificado Cargado Exitosamente", "success")
        return redirect(url_for('registros.registros'))    

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('registros.registros'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('registros.registros'))

#Ruta Ajax para Obtener Total de Registros x Campaña
@bp_registros.post('/getRegistrosCamp')
def getRegistrosCamp():
    try:
        data = request.get_json()
        id_camp = data.get("id_camp")
        registros_camp = registros_service.count_registros_camp(id_camp)
        if registros_camp:
            return jsonify(registros_camp)
        else: 
            return jsonify({"Error": "No se encontraron registros."})

    except error.Error as e: 
        return jsonify({"Error": f"{e.msg}"}), 500
    
    except Exception as ex:
        return jsonify({"Error": f"{ex}"}), 500

#Ruta Ajax para obtener los Registros con Voto Confirmado x Campaña
@bp_registros.post('/getRegistrosVotosConfirmados')
def getRegistrosVotosConfirmados():
    try:
        data = request.get_json()
        id_camp = data.get("id_camp")
        registros_voto_confirmado = registros_service.count_registros_positivos(id_camp)
        if registros_voto_confirmado:
            return jsonify(registros_voto_confirmado)
        else:
            return jsonify({"Error": "No se encontraron registros."})

    except error.Error as e:
        return jsonify({"Error": f"{e.msg}"}), 500
    
    except Exception as ex:
        return jsonify({"Error": f"{ex}"}), 500

#Ruta Ajax para Obtener Registros de Campaña x Depto.
@bp_registros.post('/getRegistrosDepto')
def getRegistrosDepto():
    try:
        data = request.get_json()
        id_camp = data.get("id_camp")
        registros_depto = registros_service.count_registros_x_depto(id_camp)
        if registros_depto:
            return jsonify(registros_depto)
        else:
            return jsonify(0)

    except Exception as ex:
        return jsonify(ex), 500     