import mysql.connector

def create_user_student_tables():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="student_management_system",
        charset="utf8mb4"
    )

    cursor = conn.cursor()

    # ===== USERS =====
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            role VARCHAR(20) NOT NULL
        )
    """)

    # ===== STUDENTS =====
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INT PRIMARY KEY,
            full_name VARCHAR(100) NOT NULL,
            user_id INT UNIQUE,
            class_id INT,
            FOREIGN KEY (user_id)
                REFERENCES users(user_id)
                ON DELETE CASCADE,
            FOREIGN KEY (class_id)
                REFERENCES classes(class_id)
                ON DELETE SET NULL
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("Users & Students tables created")

if __name__ == "__main__":
    create_user_student_tables()
