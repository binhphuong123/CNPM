from authentication.authorization import check_role, ADMIN

class GradeService:
    def __init__(self, conn):
        self.conn = conn

    def enter_grade(self, user, student_id, class_id, score):
        check_role()

        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO grades (student_id, class_id, score)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE score=%s
        """, (student_id, class_id, score, score))

        self.conn.commit()
        print("Grade saved")

    def view_grades_by_student(self, student_id):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT c.class_name, g.score
            FROM grades g
            JOIN classes c ON g.class_id = c.class_id
            WHERE g.student_id = %s
        """, (student_id,))

        rows = cursor.fetchall()

        if not rows:
            print("No grades found")
            return

        print("\n--- Your Grades ---")
        for r in rows:
            print(f"{r['class_name']} : {r['score']}")


