from app.database import db

def list_tipoDocumentos():
    tipos = []
    conn = db.connection()
    operation = """ SELECT cod_tipo, nom_tipo FROM tipos_documento """
    with conn.cursor() as cursor:
        cursor.execute(operation)
        result = cursor.fetchall()
        for row in result:
            tipos.append({'cod_tipo': row[0], 'nom_tipo': row[1]})

    conn.close()
    return tipos        