from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt

#Blueprint
bp_index = Blueprint('index', __name__)
bcrypt = Bcrypt()

#Rutas
@bp_index.get('/')
def index():
    session.clear()
    return render_template('login.html')

@bp_index.get('/main')
def main():
    return render_template('main.html')