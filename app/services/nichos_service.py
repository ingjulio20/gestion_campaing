from app.database import db

#Nuevo Nicho
def insert_nicho(nom_nicho):
    conn = db.connection()
    query = """ INSERT INTO nichos (nom_nicho) VALUES (%s) """
    with conn.cursor() as cursor:
        cursor.execute(query, (nom_nicho, ))
        conn.commit()
        conn.close()

#Editar Nicho
def update_nicho(nom_nicho, cod_nicho):
    conn = db.connection()
    query = """ UPDATE nichos SET nom_nicho = %s WHERE cod_nicho = %s """
    params = (nom_nicho, cod_nicho)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Eliminar Nicho
def delete_nicho(cod_nicho):
    conn = db.connection()
    query = """ DELETE FROM nichos WHERE cod_nicho = %s """
    with conn.cursor() as cursor:
        cursor.execute(query, (cod_nicho, ))
        conn.commit()
        conn.close()

#Listar Nichos
def list_nichos():
    nichos = []
    conn = db.connection()
    query = """ SELECT cod_nicho, nom_nicho FROM nichos """
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            nichos.append({'cod_nicho': row[0], 'nom_nicho': row[1]})

    conn.close()
    return nichos

#Listar nicho por codigo
def list_nicho_cod(cod_nicho):
    nicho = None
    conn = db.connection()
    query = """ SELECT * FROM nichos WHERE cod_nicho = %s """
    with conn.cursor() as cursor:
        cursor.execute(query, (cod_nicho, ))
        result = cursor.fetchone()
        nicho = result

    conn.close()
    return nicho    