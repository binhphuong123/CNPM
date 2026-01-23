import mysql.connector
from mysql.connector import Error

def connect_mysql():
    """
    Tao ket noi mysql
    """
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            charset="utf8mb4",
            database="student_management_system"
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(" Loi connect MySQL:", e)
        return None
