from flask import Flask
from flask_bcrypt import Bcrypt

#Blueprints
from app.routes.index_routes import bp_index
from app.routes.usuarios_routes import bp_usuarios

#Inicialización
app = Flask(__name__)

#Configuración
app.secret_key = "M&_S3cr3t_K3&"
bcrypt = Bcrypt(app)

#Registro de Blueprints
app.register_blueprint(bp_index)
app.register_blueprint(bp_usuarios)

#Instancia
if __name__ == '__main__':
    app.run(debug=True, port=3000)