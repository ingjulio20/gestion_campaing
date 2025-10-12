from app.database import db

#Nuevo Registro
def insert_registro(tipo_documento, nuip, nombre_completo, fecha_nacimiento, direccion, telefono, email,
                    depto, nom_depto, municipio, nom_municipio, sexo, etnia, usuario_registro):
    
    conn = db.connection()
    operation = """ INSERT INTO registros (tipo_documento, nuip, nombre_completo, fecha_nacimiento, direccion, telefono, email,
                    depto, nom_depto, municipio, nom_municipio, sexo, etnia, usuario_registro) 
                    VALUES 
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    params = (tipo_documento, nuip, nombre_completo, fecha_nacimiento, direccion, telefono, email,
              depto, nom_depto, municipio, nom_municipio, sexo, etnia, usuario_registro)
    
    with conn.cursor() as cursor:
        cursor.execute(operation, params)
        conn.commit()
        conn.close()

#Actualizar datos de Registro
def update_registro(tipo_documento, nuip, nombre_completo, fecha_nacimiento, direccion, telefono, email,
                    depto, nom_depto, municipio, nom_municipio, sexo, etnia, id_registro):
    
    conn = db.connection()
    operation = """ UPDATE registros SET tipo_documento = %s, nuip = %s, nombre_completo = %s, fecha_nacimiento = %s, direccion = %s, telefono = %s, email = %s,
                    depto = %s, nom_depto = %s, municipio = %s, nom_municipio = %s, sexo = %s, etnia = %s
                    WHERE id_registro = %s"""
    
    params = (tipo_documento, nuip, nombre_completo, fecha_nacimiento, direccion, telefono, email,
              depto, nom_depto, municipio, nom_municipio, sexo, etnia, id_registro)
    
    with conn.cursor() as cursor: 
        cursor.execute(operation, params)
        conn.commit()
        conn.close()

#Eliminar Registro
def delete_registro(id_registro):
    conn = db.connection()
    operation = """ DELETE FROM registros WHERE id_registro = %s """
    with conn.cursor() as cursor:
        cursor.execute(operation, (id_registro, ))
        conn.commit()
        conn.close()

#Listar todos los registros
def list_registros():
    registros = []
    conn = db.connection()
    operation = """ SELECT id_registro, nuip, nombre_completo, usuario_registro FROM registros """
    with conn.cursor() as cursor:
        cursor.execute(operation)
        result = cursor.fetchall()
        for row in result:
            registros.append({'ID': row[0], 'nuip': row[1], 'nombre': row[2], 'usuario': row[3]})

    conn.close()
    return registros

#Listar Registro por ID
def list_registro_id(id_registro):
    registro = None
    conn = db.connection()
    operation = """ SELECT * FROM registros where id_registro = %s """
    with conn.cursor() as cursor:
        cursor.execute(operation, (id_registro, ))
        result = cursor.fetchone()
        registro = result

    conn.close()
    return registro

#Contar Todos los Registros
def count_registros():
    conteo = None
    conn = db.connection()
    operation = """ SELECT COUNT(*) FROM registros """
    with conn.cursor() as cursor:
        cursor.execute(operation)
        conteo = cursor.fetchone()

    conn.close()
    return conteo

#Contar Todos los Registros por Departamento
def count_registros_x_depto():
    registros_depto = []
    conn = db.connection()
    operation = """ SELECT COUNT(nom_depto), nom_depto FROM registros 
                    GROUP BY nom_depto """
    
    with conn.cursor() as cursor:
        cursor.execute(operation)
        result = cursor.fetchall()
        for row in result:
            registros_depto.append({'numero': row[0], 'depto': row[1]})
    
    conn.close()
    return registros_depto