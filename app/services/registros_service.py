from app.database import db

#Nuevo Registro
def insert_registro(tipo_documento, nuip, nombre_completo, fecha_nacimiento, direccion, telefono, email,
                    depto, nom_depto, municipio, nom_municipio, sexo, etnia, puesto_votacion, direccion_puesto, 
                    mesa_votacion, camp_asignada, nicho, usuario_registro):
    
    conn = db.connection()
    operation = """ INSERT INTO registros (tipo_documento, nuip, nombre_completo, fecha_nacimiento, direccion, telefono, email,
                    depto, nom_depto, municipio, nom_municipio, sexo, etnia, puesto_votacion, direccion_puesto, 
                    mesa_votacion, camp_asignada, nicho, usuario_registro) 
                    VALUES 
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    params = (tipo_documento, nuip, nombre_completo, fecha_nacimiento, direccion, telefono, email,
              depto, nom_depto, municipio, nom_municipio, sexo, etnia, puesto_votacion, direccion_puesto, 
              mesa_votacion, camp_asignada, nicho, usuario_registro)
    
    with conn.cursor() as cursor:
        cursor.execute(operation, params)
        conn.commit()
        conn.close()

#Actualizar datos de Registro
def update_registro(tipo_documento, nuip, nombre_completo, fecha_nacimiento, direccion, telefono, email,
                    depto, nom_depto, municipio, nom_municipio, sexo, etnia, puesto_votacion, direccion_puesto,
                    mesa_votacion, camp_asignada, nicho, id_registro):
    
    conn = db.connection()
    operation = """ UPDATE registros SET tipo_documento = %s, nuip = %s, nombre_completo = %s, fecha_nacimiento = %s, direccion = %s, telefono = %s, email = %s,
                    depto = %s, nom_depto = %s, municipio = %s, nom_municipio = %s, sexo = %s, etnia = %s, puesto_votacion = %s, direccion_puesto = %s,
                    mesa_votacion = %s, camp_asignada = %s, nicho = %s WHERE id_registro = %s"""
    
    params = (tipo_documento, nuip, nombre_completo, fecha_nacimiento, direccion, telefono, email,
              depto, nom_depto, municipio, nom_municipio, sexo, etnia, puesto_votacion, direccion_puesto, 
              mesa_votacion, camp_asignada, nicho, id_registro)
    
    with conn.cursor() as cursor: 
        cursor.execute(operation, params)
        conn.commit()
        conn.close()

#Actulizar Datos de Voto en registro
def update_voto_registro(voto_ejercido, cert_voto, id_registro):
    conn = db.connection()
    operation = """ UPDATE registros SET voto_ejercido = %s, cert_voto = %s WHERE id_registro = %s """
    params = (voto_ejercido, cert_voto, id_registro)
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

#Listar todos los registros x nuip
def list_registros_nuip(nuip):
    registros = []
    nuip = f"{nuip}%"
    conn = db.connection()
    operation = """ SELECT rg.id_registro ID, rg.nuip NUIP, rg.nombre_completo VOTANTE, c.nom_camp CAMPAÑA, u.nombre_completo FUNCIONARIO, rg.usuario_registro USER_FUNCIONARIO, n.nom_nicho NICHO, rg.voto_ejercido VOTO
                    FROM registros rg 
                    LEFT JOIN usuarios u on rg.usuario_registro = u.usuario
                    LEFT JOIN camp_electoral c on c.id_camp = rg.camp_asignada
                    LEFT JOIN nichos n on n.cod_nicho = rg.nicho
                    WHERE rg.nuip LIKE %s """
    with conn.cursor() as cursor:
        cursor.execute(operation, (nuip, ))
        result = cursor.fetchall()
        for row in result:
            registros.append({'ID': row[0], 'nuip': row[1], 'votante': row[2], 'camp': row[3], 'funcionario': row[4], 'user_funcionario': row[5], 'nicho': row[6], 'voto': row[7]})

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

#Contar Todos los Registros X Campaña
def count_registros_camp(camp_asignada):
    conteo = None
    conn = db.connection()
    operation = """ SELECT FORMAT(COUNT(r.camp_asignada), 0) FROM registros r
                    WHERE r.camp_asignada = %s """
    with conn.cursor() as cursor:
        cursor.execute(operation, (camp_asignada, ))
        conteo = cursor.fetchone()

    conn.close()
    return conteo

#Contar Todos los Registros con Voto Confirmado x Campaña
def count_registros_positivos(camp_asignada):
    conteo = None
    conn = db.connection()
    operation = """ SELECT FORMAT(COUNT(r.voto_ejercido), 0) FROM registros r
                    WHERE r.voto_ejercido = 'SÍ' AND r.camp_asignada = %s """
    with conn.cursor() as cursor:
        cursor.execute(operation, (camp_asignada, ))
        conteo = cursor.fetchone()

    conn.close()
    return conteo    

#Contar Todos los Registros de Campaña x Depto.
def count_registros_x_depto(camp_asiganada):
    registros_depto = []
    conn = db.connection()
    operation = """ SELECT COUNT(r.nom_depto), r.nom_depto FROM registros r
                    WHERE r.camp_asignada = %s
                    GROUP BY r.nom_depto """
    
    with conn.cursor() as cursor:
        cursor.execute(operation, (camp_asiganada, ))
        result = cursor.fetchall()
        for row in result:
            registros_depto.append({'numero': row[0], 'depto': row[1]})
    
    conn.close()
    return registros_depto