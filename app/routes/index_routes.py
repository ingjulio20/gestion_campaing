from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt

#Blueprint
bp_index = Blueprint('index', __name__)

#Rutas
@bp_index.get('/')
def index():
    return render_template('login.html')