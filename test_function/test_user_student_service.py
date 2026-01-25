import mysql.connector
from authentication.login_logout import login
from authentication.authorization import ADMIN
from user_student.user_service import UserService
from user_student.student_service import StudentService


def show_menu():
    print("\n===== USER & STUDENT MANAGEMENT =====")
    print("1. Add user")
    print("2. Update user")
    print("3. Delete user")
    print("4. Add student")
    print("5. Update student")
    print("6. Delete student")
    print("0. Exit")


def main():
    # ===== CONNECT DB (GIỐNG HÙNG – GIỐNG LECTURER) =====
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="student_management_system",
        charset="utf8mb4"
    )

    user_service = UserService()
    student_service = StudentService(conn)

    # ===== LOGIN =====
    print("===== LOGIN =====")
    username = input("Username: ")
    password = input("Password: ")

    current_user = login(username, password)
    if not current_user:
        print("Login failed")
        return

    print("Login success")

    # ===== MENU LOOP =====
    while True:
        show_menu()
        choice = input("Choose: ")

        try:
            # ===== USER =====
            if choice == "1":
                user_service.add_user(
                    current_user,
                    input("Username: "),
                    input("Password: "),
                    input("Role (ADMIN / STUDENT): ")
                )

            elif choice == "2":
                user_service.update_user(
                    current_user,
                    input("Username: "),
                    input("New password: ")
                )

            elif choice == "3":
                user_service.delete_user(
                    current_user,
                    input("Username: ")
                )

            # ===== STUDENT =====
            elif choice == "4":
                student_service.add_student(
                    current_user,
                    int(input("Student ID: ")),
                    input("Full name: "),
                    int(input("Class ID: "))
                )

            elif choice == "5":
                student_service.update_student(
                    current_user,
                    int(input("Student ID: ")),
                    input("New full name: "),
                    int(input("New class ID: "))
                )

            elif choice == "6":
                student_service.delete_student(
                    current_user,
                    int(input("Student ID: "))
                )

            elif choice == "0":
                print("Exit")
                break

            else:
                print("Invalid choice")

        except ValueError:
            print("Error: ID phải là số")

        except Exception as e:
            print("Error:", e)

    conn.close()


if __name__ == "__main__":
    main()
