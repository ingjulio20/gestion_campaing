from flask import Blueprint, request, jsonify
from app.services import deptos_service
import mysql.connector.errors as error

#Blueprint
bp_deptos = Blueprint('deptos', __name__)

#Rutas
@bp_deptos.get('/getDeptos')
def detDeptos():
    try:
        deptos = deptos_service.list_departamentos()
        if deptos:
            return jsonify(deptos)

    except error.Error as e:
        return jsonify(e)
    
    except Exception as ex:
        return jsonify(ex)


@bp_deptos.post('/getMunicipios')
def getMunicipios():
    try: 
        data = request.get_json()
        cod_depto = data.get("codDepto")
        municipios = deptos_service.list_municipios(cod_depto)
        if municipios:
            return jsonify(municipios)
        
    except error.Error as e:
        return jsonify(e)
    
    except Exception as ex:
        return jsonify(ex)