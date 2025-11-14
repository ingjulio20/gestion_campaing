from app.database import db

#Nueva Campaña Electoral
def insert_camp_electoral(nom_camp, meta_votantes, meta_votos):
    conn = db.connection()
    query = """ INSERT INTO camp_electoral (nom_camp, meta_votantes, meta_votos) VALUES (%s, %s, %s) """
    params = (nom_camp, meta_votantes, meta_votos)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Modificar Datos de Campaña Electoral
def update_camp_electoral(nom_camp, meta_votantes, meta_votos, id_camp):
    conn = db.connection()
    query = """ UPDATE camp_electoral SET nom_camp = %s, meta_votantes = %s, meta_votos = %s WHERE id_camp = %s """
    params = (nom_camp, meta_votantes, meta_votos, id_camp)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        conn.close()

#Eliminar Campaña Electoral
def delete_camp_electoral(id_camp):
    conn = db.connection()
    query = """ DELETE FROM camp_electoral WHERE id_camp = %s """
    with conn.cursor() as cursor:
        cursor.execute(query, (id_camp, ))
        conn.commit()
        conn.close()

#Listar Campañas
def list_camp_electorales():
    camps = []
    conn = db.connection()
    query = """ SELECT id_camp, nom_camp, meta_votantes, meta_votos FROM camp_electoral """
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            camps.append({'ID': row[0], 'nombre': row[1], 'votantes': row[2], 'votos': row[3]})

    conn.close()
    return camps

#Listar Campaña por ID
def list_camp_id(id_camp):
    camp = None
    conn = db.connection()
    query = """ SELECT * FROM camp_electoral WHERE id_camp = %s """
    with conn.cursor() as cursor:
        cursor.execute(query, (id_camp, ))
        result = cursor.fetchone()
        camp = result

    conn.close()
    return camp    