from app.database import db

def list_departamentos():
    departamentos = []
    conn = db.connection()
    operation = """ SELECT cod_depto, nom_depto FROM departamentos """
    with conn.cursor() as cursor:
        cursor.execute(operation)
        result = cursor.fetchall()
        for row in result:
            departamentos.append({'cod_depto': row[0], 'nom_depto': row[1]})

    conn.close()
    return departamentos

def list_municipios(cod_depto):
    municipios = []
    conn = db.connection()
    operation = """ SELECT cod_municipio, nom_municipio FROM municipios WHERE cod_depto = %s """
    with conn.cursor() as cursor:
        cursor.execute(operation, (cod_depto, ))
        result = cursor.fetchall()
        for row in result:
            municipios.append({'cod_municipio': row[0], 'nom_municipio': row[1]})

    conn.close()
    return municipios        