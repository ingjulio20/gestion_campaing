from app.database import db

def list_etnias():
    etnias = []
    conn = db.connection()
    operation = """ SELECT cod_etnia, nom_etnia FROM etnias """
    with conn.cursor() as cursor:
        cursor.execute(operation)
        result = cursor.fetchall()
        for row in result:
            etnias.append({'cod_etnia': row[0], 'nom_etnia': row[1]})

    conn.close()
    return etnias       