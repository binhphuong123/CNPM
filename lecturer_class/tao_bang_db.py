import mysql.connector
from connectdb.connectMySQL import connect_mysql

def create_lecturer_class_tables():
    conn = connect_mysql()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lecturers (
            lecturer_id INT PRIMARY KEY,
            full_name VARCHAR(100) NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS classes (
            class_id INT PRIMARY KEY,
            class_name VARCHAR(100) NOT NULL,
            lecturer_id INT,
            FOREIGN KEY (lecturer_id)
                REFERENCES lecturers(lecturer_id)
                ON DELETE SET NULL
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

    print("Lecturer & Class tables created")

if __name__ == "__main__":
    create_lecturer_class_tables()
