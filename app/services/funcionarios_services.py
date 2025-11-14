from app.database import db

#Listar todos los roles de funcionarios
def list_roles_funcionarios():
    roles = []
    conn = db.connection()
    query = """ SELECT cod_rol, nom_rol FROM roles_funcionarios """
    with conn.cursor() as cursor: 
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            roles.append({'cod_rol': row[0], 'nom_rol': row[1]})

    conn.close()
    return roles

#Insertar Nuevo Funcionario
def insert_funcionario(nuip_funcionario, nom_funcionario, dir_funcionario, tel_funcionario, rol_funcionario, admin_asociado, enlace_asociado):
    conn = db.connection()
    query = """ INSERT INTO funcionarios (nuip_funcionario, nom_funcionario, dir_funcionario, tel_funcionario, rol_funcionario, admin_asociado, enlace_asociado) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    
    params = (nuip_funcionario, nom_funcionario, dir_funcionario, tel_funcionario, rol_funcionario, admin_asociado, enlace_asociado)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Modificar Funcionario
def update_funcionario(nuip_funcionario, nom_funcionario, dir_funcionario, tel_funcionario, rol_funcionario, admin_asociado, enlace_asociado, id_funcionario):
    conn = db.connection()
    query = """ UPDATE funcionarios SET nuip_funcionario = %s, nom_funcionario = %s, dir_funcionario = %s, tel_funcionario = %s, rol_funcionario = %s,
                admin_asociado = %s, enlace_asociado = %s WHERE id_funcionario = %s """
    
    params = (nuip_funcionario, nom_funcionario, dir_funcionario, tel_funcionario, rol_funcionario, admin_asociado, enlace_asociado, id_funcionario)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Eliminar Funcionario
def delete_funcionario(id_funcionario):
    conn = db.connection()
    query = """ DELETE FROM funcionarios WHERE id_funcionario = %s """
    with conn.cursor() as cursor:
        cursor.execute(query, (id_funcionario, ))
        conn.commit()
        conn.close()

#Listar todos los funcionarios Administradores
def list_funcionarios_admin():
    funcionarios = []
    conn = db.connection()
    query = """ SELECT nuip_funcionario, nom_funcionario FROM funcionarios WHERE rol_funcionario = 1 """
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            funcionarios.append({'documento': row[0], 'nombre': row[1]})

    conn.close()
    return funcionarios

#Listar todos los funcionarios Enlaces
def list_funcionarios_enlace():
    funcionarios = []
    conn = db.connection()
    query = """ SELECT nuip_funcionario, nom_funcionario FROM funcionarios WHERE rol_funcionario = 2 """
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            funcionarios.append({'documento': row[0], 'nombre': row[1]})

    conn.close()
    return funcionarios

#Listar Funcionarios
def list_funcionarios():
    funcionarios = []
    conn = db.connection()
    query = """ SELECT f.nuip_funcionario, f.nom_funcionario, rf.nom_rol FROM 
                funcionarios f
                LEFT JOIN roles_funcionarios rf ON f.rol_funcionario = rf.cod_rol """
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            funcionarios.append({'nuip': row[0], 'nombre': row[1], 'rol': row[2]})

    conn.close()
    return funcionarios        

#Listar Funcionarios por Nombre
def list_funcionarios_nombre(nombre):
    funcionarios = []
    conn = db.connection()
    nombre = f"{nombre}%"
    query = """ SELECT f.id_funcionario, f.nuip_funcionario, f.nom_funcionario, rf.nom_rol,
                COALESCE(adm.nom_funcionario, 'N/A') as administrador,
                COALESCE(elc.nom_funcionario, 'N/A') as enlace
                FROM funcionarios f
                LEFT JOIN roles_funcionarios rf on f.rol_funcionario = rf.cod_rol
                LEFT JOIN funcionarios adm on adm.nuip_funcionario = f.admin_asociado
                LEFT JOIN funcionarios elc on elc.nuip_funcionario= f.enlace_asociado
                WHERE f.nom_funcionario LIKE %s """
    
    with conn.cursor() as cursor:
        cursor.execute(query, (nombre, ))
        result = cursor.fetchall()
        for row in result:
            funcionarios.append({'ID': row[0], 'nuip': row[1], 'nombre': row[2], 'rol': row[3], 'administrador': row[4], 'enlace': row[5]})

    conn.close()
    return funcionarios

#Listar Funcionario por ID
def list_funcionario_id(id_funcionario):
    funcionario = None
    conn = db.connection()
    query = """ SELECT * FROM funcionarios WHERE id_funcionario = %s """
    with conn.cursor() as cursor:
        cursor.execute(query, (id_funcionario, ))
        result = cursor.fetchone()
        funcionario = result

    conn.close()
    return funcionario 