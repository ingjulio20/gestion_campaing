from flask import Blueprint, render_template, request, redirect, url_for, flash, send_file, jsonify
from app.services import campaña_service, registros_service
from io import BytesIO
import mysql.connector.errors as error
import pandas as pd

bp_reportes = Blueprint('reportes', __name__)

@bp_reportes.get('/reportes')
def reportes():
    return render_template('tmp_reportes/reportes.html')

@bp_reportes.get('/listado_registros')
def listado_registros():
    try:
        registros = registros_service.listar_registros_reporte()
        df = pd.DataFrame(registros)
        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Registros')

        buffer.seek(0)    
        return send_file(buffer, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", as_attachment=True, download_name="listado_registros.xlsx")

    except Exception as ex:
       return jsonify({"Error": f"{ex}"}), 500

@bp_reportes.get('/dashboard')
def dashboard():
    camps = campaña_service.list_camp_electorales()
    return render_template('tmp_reportes/dashboard.html', camps = camps)

