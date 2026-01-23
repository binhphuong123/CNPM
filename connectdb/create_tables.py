from connectdb.connectMySQL import connect_mysql
from security.password_hash import hash_password


def create_users_table():
    """
    Tạo bảng để phục vụ đăng nhập & phân quyền
    """
    conn = connect_mysql()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            role ENUM('ADMIN', 'LECTURER', 'STUDENT') NOT NULL
        )
    """)
    


    cursor.close()
    conn.close()


def create_default_admin():
    """
    Tạo tài khoản admin mặc định
    """
    conn = connect_mysql()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT IGNORE INTO users (username, password, role)
        VALUES (%s, %s, %s)
    """, ("admin", hash_password("admin123"), "ADMIN"))

    conn.commit()


    cursor.close()
    conn.close()


if __name__ == "__main__":
    create_users_table()
    create_default_admin()
    print(" Khởi tạo table hệ thống hoàn tất")
