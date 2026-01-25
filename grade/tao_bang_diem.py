import mysql.connector

def create_grade_table():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="student_management_system",
        charset="utf8mb4"
    )
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS grades (
            grade_id INT AUTO_INCREMENT PRIMARY KEY,
            student_id INT NOT NULL,
            class_id INT NOT NULL,
            score FLOAT NOT NULL,
            FOREIGN KEY (student_id)
                REFERENCES students(student_id)
                ON DELETE CASCADE,
            FOREIGN KEY (class_id)
                REFERENCES classes(class_id)
                ON DELETE CASCADE,
            UNIQUE(student_id, class_id)
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("Grades table created")

if __name__ == "__main__":
    create_grade_table()
