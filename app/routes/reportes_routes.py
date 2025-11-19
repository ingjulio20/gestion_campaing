from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services import campaña_service, registros_service
import mysql.connector.errors as error

bp_reportes = Blueprint('reportes', __name__)

@bp_reportes.get('/dashboard')
def dashboard():
    camps = campaña_service.list_camp_electorales()
    return render_template('tmp_reportes/dashboard.html', camps = camps)