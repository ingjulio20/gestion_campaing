import mysql.connector

def connection():
    #Variables
    user = 'root'
    password = ''
    host = 'localhost'
    database = 'gestion_camp'
    port = 3306

    #Cadena de Conexión
    conexion = mysql.connector.connect(
        user = user,
        password = password,
        host = host,
        database = database,
        port = port
    )
    
    #Devolver Conexión
    return conexion