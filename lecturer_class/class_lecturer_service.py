from authentication.authorization import check_role, ADMIN

class LecturerClassService:
    def __init__(self, conn):
        self.conn = conn

    # ===== LECTURER =====
    def add_lecturer(self, user, lecturer_id, full_name):
        check_role()

        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO lecturers VALUES (%s, %s)",
            (lecturer_id, full_name)
        )
        self.conn.commit()
        print("Lecturer added")

    def update_lecturer(self, user, lecturer_id, full_name):
        check_role()

        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE lecturers SET full_name=%s WHERE lecturer_id=%s",
            (full_name, lecturer_id)
        )
        self.conn.commit()
        print("Lecturer updated")

    def delete_lecturer(self, user, lecturer_id):
        check_role()

        cursor = self.conn.cursor()
        cursor.execute(
            "DELETE FROM lecturers WHERE lecturer_id=%s",
            (lecturer_id,)
        )
        self.conn.commit()
        print("Lecturer deleted")

    # ===== CLASS =====
    def create_class(self, admin, class_id, class_name):
        check_role()

        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO classes (class_id, class_name, lecturer_id)
            VALUES (%s, %s, NULL)
            """,
            (class_id, class_name)
        )
        self.conn.commit()
        print("Class created")

    def update_class(self, user, class_id, class_name):
        check_role()

        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE classes SET class_name=%s WHERE class_id=%s",
            (class_name, class_id)
        )
        self.conn.commit()
        print("Class updated")

    def delete_class(self, user, class_id):
        check_role()

        cursor = self.conn.cursor()
        cursor.execute(
            "DELETE FROM classes WHERE class_id=%s",
            (class_id,)
        )
        self.conn.commit()
        print("Class deleted")

    def assign_lecturer_to_class(self, user, lecturer_id, class_id):
        check_role()

        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE classes SET lecturer_id=%s WHERE class_id=%s",
            (lecturer_id, class_id)
        )
        self.conn.commit()
        print("Lecturer assigned to class")
