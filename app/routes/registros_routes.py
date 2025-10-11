from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services import documentos_service, deptos_service, registros_service
import mysql.connector.errors as error

#Blueprint
bp_registros = Blueprint('registros', __name__)

#Rutas
@bp_registros.get('/registros')
def registros():
    return render_template('tmp_registros/registros.html')

@bp_registros.get('/nuevo_registro')
def nuevo_registro():
    tipos = documentos_service.list_tipoDocumentos()
    deptos = deptos_service.list_departamentos()
    return render_template('tmp_registros/nuevo_registro.html', tipos = tipos, deptos = deptos)