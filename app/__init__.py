from flask import Flask
from flask_bcrypt import Bcrypt

#Blueprints
from app.routes.index_routes import bp_index

#Inicialización
app = Flask(__name__)

#Configuración
app.secret_key = "M&_S3cr3t_K3&"
bcrypt = Bcrypt(app)

#Registro de Blueprints
app.register_blueprint(bp_index)

#Instancia
if __name__ == '__main__':
    app.run(debug=True, port=3000)