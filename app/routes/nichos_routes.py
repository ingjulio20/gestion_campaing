from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.services import nichos_service
import mysql.connector.errors as error

bp_nichos = Blueprint('nichos', __name__)

#Ruta Ventana Principal Nichos
@bp_nichos.get('/nichos')
def nichos():
    nichos = nichos_service.list_nichos()
    return render_template ('tmp_nichos/nichos.html', nichos = nichos)

#Ruta Ventana Nuevo Nicho
@bp_nichos.get('/nuevo_nicho')
def nuevo_nicho():
    return render_template ('tmp_nichos/nuevo_nicho.html')

#Ruta Metodo Nuevo Nicho
@bp_nichos.post('/add_nicho')
def add_nicho():
    try:
        nom_nicho = request.form["nom_nicho"]
        nichos_service.insert_nicho(nom_nicho)

        flash("Nicho Creado Exitosamente", "success")
        return redirect(url_for('nichos.nichos'))
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('nichos.nichos'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('nichos.nichos'))

#Ruta Ventana Editar Nicho
@bp_nichos.get('/editar_nicho/<int:id>')
def editar_nicho(id):
    nicho = nichos_service.list_nicho_cod(id)
    return render_template('tmp_nichos/editar_nicho.html', nicho = nicho)

#Ruta Metodo Modificar Nicho
@bp_nichos.post('/update_nicho')
def update_nicho():
    try:
        nom_nicho = request.form["nom_nicho"]
        cod_nicho = request.form["cod_nicho"]

        nichos_service.update_nicho(nom_nicho, cod_nicho)
        flash("Datos de Nicho Modificados Exitosamente", "success")
        return redirect(url_for('nichos.nichos'))
    
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('nichos.nichos'))
    
    except Exception as ex: 
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('nichos.nichos'))

#Ruta Metodo Eliminar Nicho
@bp_nichos.get('/delete_nicho/<int:id>')
def delete_nicho(id):
    try:
        nichos_service.delete_nicho(id)
        flash("Nicho Eliminado Exitosamente", "success")
        return redirect(url_for('nichos.nichos'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('nichos.nichos'))
    
    except Exception as ex: 
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('nichos.nichos'))    