import mysql.connector
from mysql.connector import Error

def connect():
    """Conectando a la Base de Datos"""

    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            database="login",
            user="root",
            password="12345678"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            print('Conexion Exitosa a la Base de Datos')
            return connection, connect

    except Exception as e:
        print('Error en la conexion a la Base de Datos', e)
        return None, None


def disconnect(connection, cursor):
    """Desconectar de la Base de Datos"""

    if cursor:
        cursor.close()
    if connection:
        connection.close()
    print('Desconexion Existo de la Base de Datos')

if __name__ == "__main__":
    connection, connect = connect()
    if connection and cursor:
        disconnect(connection, cursor)
    
    
