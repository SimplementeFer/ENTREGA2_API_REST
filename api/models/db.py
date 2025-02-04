import pymysql
import os

def get_db_connection():
    try:
        connection = pymysql.connect(
            host=os.environ.get('DB_HOST', 'db'),
            user=os.environ.get('DB_USER', 'root'),
            password=os.environ.get('DB_PASSWORD', 'example'),
            database=os.environ.get('DB_NAME', 'reviews_db'),
            port=int(os.environ.get('DB_PORT', 3306)),
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except pymysql.MySQLError as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None
