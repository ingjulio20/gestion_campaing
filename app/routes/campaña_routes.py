from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.services import campaña_service
import mysql.connector.errors as error

bp_campañas = Blueprint('campañas', __name__)

#Ruta Ventana Principal Campañas
@bp_campañas.get('/campañas')
def campañas():
    camps = campaña_service.list_camp_electorales()
    return render_template('tmp_campañas/campañas.html', camps = camps)

#Ruta Ventana Nueva Campaña
@bp_campañas.get('/nueva_campaña')
def nueva_campaña():
    return render_template('tmp_campañas/nueva_campaña.html')

#Ruta Metodo Nueva Campaña BD
@bp_campañas.post('/add_campaña')
def add_campaña():
    try:
        nom_camp = request.form["nom_camp"]
        meta_votantes = request.form["meta_votantes"]
        meta_votos = request.form["meta_votos"]

        campaña_service.insert_camp_electoral(nom_camp, meta_votantes, meta_votos)
        flash("Campaña Creada Exitosamente.", "success")
        return redirect(url_for('campañas.campañas'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('campañas.campañas'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('campañas.campañas'))

#Ruta Ventana Editar Campaña
@bp_campañas.get('/editar_campaña/<int:id>')
def editar_campaña(id):
    camp = campaña_service.list_camp_id(id)
    return render_template('tmp_campañas/editar_campaña.html', camp = camp)

#Ruta Metodo Modificar Campaña BD
@bp_campañas.post('/update_campaña')
def update_campaña():
    try:
        nom_camp = request.form["nom_camp"]
        meta_votantes = request.form["meta_votantes"]
        meta_votos = request.form["meta_votos"]
        id_camp = request.form["id_camp"]

        campaña_service.update_camp_electoral(nom_camp, meta_votantes, meta_votos, id_camp)
        flash("Datos de Campaña Modificados Exitosamente", "success")
        return redirect(url_for('campañas.campañas'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('campañas.campañas'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('campañas.campañas'))

#Ruta Metodo Eliminar Campaña
@bp_campañas.get('/delete_campaña/<int:id>')
def delete_campaña(id):
    try:
        campaña_service.delete_camp_electoral(id)
        flash("Campaña Eliminada Exitosamente", "success")
        return redirect(url_for('campañas.campañas'))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('campañas.campañas'))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('campañas.campañas'))