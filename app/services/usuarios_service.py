from app.database import db

#Función para listar todos los usuarios de la bd
def listar_usuarios():
    usuarios = []
    conn = db.connection()
    query = "SELECT nombre_completo, usuario, perfil FROM usuarios where usuario not in ('superuser')"
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            usuarios.append({'nombre_completo': row[0], 'usuario': row[1], 'perfil': row[2]})

    conn.close()
    return usuarios

#Función para listar un usuario por nombre para actualizar
def listar_usuario_nombre(nombre):
    usuario = None
    conn = db.connection()
    query = "SELECT * FROM usuarios WHERE usuario = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (nombre,))
        result = cursor.fetchone()
        usuario = result

    conn.close()
    return usuario

# Función para listar todos perfiles de usuarios para insertar
def listar_perfiles_usuario():
    perfiles = []
    conn = db.connection()
    query = "SELECT * FROM perfiles_usuarios"
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            perfiles.append({'id_perfil': row[0], 'nom_perfil': row[1]})

    conn.close()
    return perfiles

#Función para insertar usuarios en bd
def insert_usuario(doc_usuario, nombre_completo, usuario, password, perfil):
    conn = db.connection()
    query = "INSERT INTO usuarios (doc_usuario, nombre_completo, usuario, password, perfil) VALUES (%s, %s, %s, %s, %s)"
    params = (doc_usuario, nombre_completo, usuario, password, perfil)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Función para eliminar usuarios de bd       
def delete_usuario(usuario):
    conn = db.connection()
    query = "DELETE FROM usuarios WHERE usuario = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (usuario,))
        conn.commit()
        conn.close()

#Función para actualizar usuario en bd
def update_usuario(doc_usuario, nombre_completo, usuario, password, perfil):
    conn = db.connection()
    query = "UPDATE usuarios SET doc_usuario= %s, nombre_completo= %s, usuario= %s, password= %s, perfil= %s WHERE usuario= %s"
    params = (doc_usuario, nombre_completo, usuario, password, perfil, usuario)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

                    
