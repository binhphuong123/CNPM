from authentication.authorization import check_role, ADMIN

class StudentService:
    def __init__(self, conn):
        self.conn = conn

    def add_student(self, admin, student_id, full_name, class_id):
        check_role()

        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO students (student_id, full_name, class_id)
            VALUES (%s, %s, %s)
            """,
            (student_id, full_name, class_id)
        )
        self.conn.commit()
        print("Student added")

    def update_student(self, admin, student_id, full_name, class_id):
        check_role()

        cursor = self.conn.cursor()
        cursor.execute(
            """
            UPDATE students
            SET full_name=%s, class_id=%s
            WHERE student_id=%s
            """,
            (full_name, class_id, student_id)
        )
        self.conn.commit()
        print("Student updated")

    def delete_student(self, admin, student_id):
        check_role()

        cursor = self.conn.cursor()
        cursor.execute(
            "DELETE FROM students WHERE student_id=%s",
            (student_id,)
        )
        self.conn.commit()
        print("Student deleted")
