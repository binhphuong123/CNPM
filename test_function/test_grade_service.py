import mysql.connector
from authentication.login_logout import login
from grade.Grade_service import GradeService

def main():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="student_management_system",
        charset="utf8mb4"
    )

    grade_service = GradeService(conn)

    print("===== LOGIN =====")
    user = login(input("Username: "), input("Password: "))
    if not user:
        return

    while True:
        print("\n===== GRADE MANAGEMENT =====")
        print("1. Enter grade")
        print("2. View student grades")
        print("0. Exit")

        choice = input("Choose: ")

        try:
            if choice == "1":
                grade_service.enter_grade(
                    user,
                    int(input("Student ID: ")),
                    int(input("Class ID: ")),
                    float(input("Score: "))
                )

            elif choice == "2":
                grade_service.view_grades_by_student(
                    int(input("Student ID: "))
                )

            elif choice == "0":
                break
        except Exception as e:
            print("Error:", e)

    conn.close()

if __name__ == "__main__":
    main()
