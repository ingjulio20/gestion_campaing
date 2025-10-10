from flask import Flask

#Inicialización
app = Flask(__name__)

#Configuración
app.secret_key = "M&_S3cr3t_K3&"

#Instancia
if __name__ == '__main__':
    app.run(debug=True)