from connectdb.connectMySQL import connect_mysql
from security.password_hash import hash_password


def init_default_accounts():
    conn = connect_mysql()
    cursor = conn.cursor()

    # ===== ADMIN =====
    cursor.execute("""
        INSERT IGNORE INTO users (username, password, role)
        VALUES (%s, %s, %s)
    """, ("admin", hash_password("admin123"), "ADMIN"))

    # ===== STUDENT USER =====
    cursor.execute("""
        INSERT IGNORE INTO users (username, password, role)
        VALUES (%s, %s, %s)
    """, ("student1", hash_password("student123"), "STUDENT"))

    cursor.execute("""
        SELECT user_id FROM users WHERE username=%s
    """, ("student1",))
    student_user_id = cursor.fetchone()[0]

    cursor.execute("""
        INSERT IGNORE INTO students (student_id, full_name, user_id)
        VALUES (%s, %s, %s)
    """, (1, "Default Student", student_user_id))

    # ===== LECTURER USER =====
    cursor.execute("""
        INSERT IGNORE INTO users (username, password, role)
        VALUES (%s, %s, %s)
    """, ("lecturer1", hash_password("lecturer123"), "LECTURER"))

    cursor.execute("""
        SELECT user_id FROM users WHERE username=%s
    """, ("lecturer1",))
    lecturer_user_id = cursor.fetchone()[0]

    cursor.execute("""
        INSERT IGNORE INTO lecturers (lecturer_id, full_name)
        VALUES (%s, %s)
    """, (1, "Default Lecturer"))

    conn.commit()
    cursor.close()
    conn.close()

    print("Khởi tạo admin / student / lecturer thành công")


if __name__ == "__main__":
    init_default_accounts()
