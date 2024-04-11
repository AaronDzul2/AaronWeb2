import pymysql

def conectar_db():
    # Configuración de la conexión a la base de datos
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",  # Aquí coloca la contraseña de tu base de datos si la has configurado
        database="usuarios"
    )
    return db


