import mysql.connector
from authentication.authorization import check_role, ADMIN
from connectdb.connectMySQL import connect_mysql
from security.password_hash import hash_password


class UserService:
    """
    User Management
    Actor: Administrator
    """

    def __init__(self):
        pass

    def add_user(self, admin, username, password, role):
        check_role()

        conn = connect_mysql()
        cursor = conn.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO users (username, password, role)
                VALUES (%s, %s, %s)
                """,
                (username, hash_password(password), role)
            )
            conn.commit()
            print("Đã thêm user")

        except mysql.connector.Error as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()

    def update_user(self, admin, username, new_password):
        check_role()

        conn = connect_mysql()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE users
            SET password = %s
            WHERE username = %s
            """,
            (hash_password(new_password), username)
        )

        conn.commit()
        cursor.close()
        conn.close()
        print("Đã cập nhật user")

    def delete_user(self, admin, username):
        check_role()

        conn = connect_mysql()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM users WHERE username = %s",
            (username,)
        )

        conn.commit()
        cursor.close()
        conn.close()
        print("Đã xoá user")
