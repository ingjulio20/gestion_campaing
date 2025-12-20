from app.database import db
import base64

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
    #nuip = f"{nuip}%"
    conn = db.connection()
    operation = """ SELECT rg.id_registro ID, rg.nuip NUIP, rg.nombre_completo VOTANTE, c.nom_camp CAMPAÑA, u.nombre_completo FUNCIONARIO, rg.usuario_registro USER_FUNCIONARIO, n.nom_nicho NICHO, 
                    rg.voto_ejercido VOTO, rg.cert_voto CERT
                    FROM registros rg 
                    LEFT JOIN usuarios u on rg.usuario_registro = u.usuario
                    LEFT JOIN camp_electoral c on c.id_camp = rg.camp_asignada
                    LEFT JOIN nichos n on n.cod_nicho = rg.nicho
                    WHERE rg.nuip = %s """
    with conn.cursor() as cursor:
        cursor.execute(operation, (nuip, ))
        result = cursor.fetchall()
        for row in result:
            certificado = row[8]
            encode_cert = None
            
            if certificado:
                encode_cert = base64.b64encode(certificado).decode('utf-8')

            registros.append({'ID': row[0], 'nuip': row[1], 'votante': row[2], 'camp': row[3], 'funcionario': row[4], 'user_funcionario': row[5], 'nicho': row[6], 'voto': row[7], 'base64': encode_cert})

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

#Carga Masiva de Registros
def insert_masivo_registros(archivo):
    conn = db.connection()
    try:
        operation = """ LOAD DATA LOCAL INFILE %s
                        INTO TABLE registros 
                        CHARACTER SET utf8mb4
                        FIELDS TERMINATED BY ',' 
                        ENCLOSED BY '"'
                        LINES TERMINATED BY '\n'
                        IGNORE 1 LINES
                        (tipo_documento, nuip, nombre_completo, direccion, telefono, email, depto,nom_depto, municipio,nom_municipio, sexo, etnia, camp_asignada, nicho, @usuario_registro)
                        SET usuario_registro = TRIM(@usuario_registro);"""
        
        with conn.cursor() as cursor:
            cursor.execute(operation, (archivo, ))
            conn.commit()
    
    except Exception as ex:
        conn.rollback()
        raise ex

    finally:
        conn.close()

#Metodo para obtener todos los registros para reporte excel
def listar_registros_reporte():
    registros = []
    conn = db.connection()
    query = """ SELECT 
                    r.nuip NUIP, 
                    r.nombre_completo NOMBRE,
                    r.direccion DIRECCION,
                    r.telefono TELEFONOS,
                    r.nom_depto DEPARTAMENTO,
                    r.nom_municipio MUNICIPIO,
                    r.puesto_votacion PUESTO, 
                    r.mesa_votacion MESA,
                    r.voto_ejercido VOTO_CONFIRMADO,
                    f.nom_funcionario FUNCIONARIO_REGISTRO, 
                    rf.nom_rol ROL_FUNCIONARIO,
                    -- Obtenemos el Enlace (si existe)
                    COALESCE(elc.nom_funcionario, 'N/A') as ENLACE_FUNCIONARIO,
                    -- LÓGICA DE ADMINISTRADOR MEJORADA:
                    -- 1. Intenta obtener el admin directo.
                    -- 2. Si es nulo, intenta obtener el admin asociado al enlace.
                    -- 3. Si ambos son nulos, pon 'N/A'.
                    COALESCE(adm.nom_funcionario, adm_via_enlace.nom_funcionario, 'N/A') as ADMINISTRADOR_FUNCIONARIO
                FROM registros r
                LEFT JOIN usuarios u on u.usuario = r.usuario_registro
                LEFT JOIN funcionarios f on f.nuip_funcionario = u.doc_usuario
                LEFT JOIN roles_funcionarios rf on rf.cod_rol = f.rol_funcionario

                -- 1. Busca el Enlace del funcionario actual
                LEFT JOIN funcionarios elc on elc.nuip_funcionario = f.enlace_asociado

                -- 2. Busca el Admin directo del funcionario actual
                LEFT JOIN funcionarios adm on adm.nuip_funcionario = f.admin_asociado

                -- 3. (NUEVO) Busca el Admin del Enlace encontrado en el paso 1
                LEFT JOIN funcionarios adm_via_enlace on adm_via_enlace.nuip_funcionario = elc.admin_asociado;

                SELECT r.nuip, r.nombre_completo, r.puesto_votacion, r.mesa_votacion, f.nom_funcionario, rf.nom_rol,
                COALESCE(elc.nom_funcionario, 'N/A') as enlace,
                COALESCE(adm.nom_funcionario, 'N/A') as administrador
                FROM registros r
                LEFT JOIN usuarios u on u.usuario = r.usuario_registro
                LEFT JOIN funcionarios f on f.nuip_funcionario = u.doc_usuario
                LEFT JOIN funcionarios adm on adm.nuip_funcionario = f.admin_asociado
                LEFT JOIN funcionarios elc on elc.nuip_funcionario= f.enlace_asociado
                LEFT JOIN roles_funcionarios rf on rf.cod_rol = f.rol_funcionario """
    
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                registros.append({'NUIP': row[0], 
                                  'NOMBRE': row[1], 
                                  'DIRECCION': row[2], 
                                  'TELEFONOS': row[3], 
                                  'DEPARTAMENTO': row[4],
                                  'MUNICIPIO': row[5],
                                  'PUESTO': row[6],
                                  'MESA': row[7],
                                  'VOTO_CONFIRMADO': row[8],
                                  'FUNCIONARIO_REGISTRO': row[9],
                                  'ROL_FUNCIONARIO': row[10],
                                  'ENLACE_FUNCIONARIO': row[11],
                                  'ADMINISTRADOR_FUNCIONARIO': row[12]})

        return registros        

    except Exception as ex:
        conn.rollback()
        raise ex
    
    finally:
        conn.close()