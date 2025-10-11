from flask import Flask, request, session, flash, render_template
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

#Ruta Metodo para verificar las URL y Redireccionar al Login
@app.before_request
def verificar_peticion():
    ruta = request.path
    if not 'name' in session and ruta != "/" and ruta != "/login_access" and not ruta.startswith("/static"):
        flash("Debe Iniciar Sesión","warning")
        return render_template(('login.html'))
    
#Instancia
if __name__ == '__main__':
    app.run(debug=True, port=3000)